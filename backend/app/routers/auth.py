import os
import secrets
from datetime import datetime, timedelta

import bcrypt
import jwt
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.orm import Session

from ..database import get_db
from .. import models, schemas
from ..security import create_access_token, decode_student_id
from ..services.email import send_email

router = APIRouter(prefix="/auth", tags=["auth"])
bearer_scheme = HTTPBearer()

EMAIL_VERIFY_EXPIRE_HOURS = 24
PASSWORD_RESET_EXPIRE_HOURS = 1


def _frontend_url() -> str:
    return os.environ.get("FRONTEND_URL", "http://localhost:5173")


def _check_teacher_invite_code(code: str | None) -> None:
    expected = os.environ.get("TEACHER_INVITE_CODE")
    if not expected:
        # not configured - fail closed rather than silently letting anyone
        # register as teacher (that's the exact gap this check exists to close)
        raise HTTPException(500, "Teacher registration is not configured on this server.")
    if not code or not secrets.compare_digest(code, expected):
        raise HTTPException(403, "Invalid teacher invite code.")


def _find_class_by_code(db: Session, join_code: str) -> models.SchoolClass:
    # Unlike the single global TEACHER_INVITE_CODE above, this is DB-backed
    # (one class = one code, not a shared secret) so a plain lookup is the
    # right check here, not a constant-time comparison against one value.
    class_ = db.query(models.SchoolClass).filter_by(join_code=join_code.strip().upper()).first()
    if not class_:
        raise HTTPException(400, "Invalid class code.")
    return class_


def _issue_token(db: Session, student_id: int, purpose: str, expire_hours: int) -> str:
    token = secrets.token_urlsafe(32)
    db.add(models.VerificationToken(
        student_id=student_id, token=token, purpose=purpose,
        expires_at=datetime.utcnow() + timedelta(hours=expire_hours),
    ))
    db.commit()
    return token


def _redeem_token(db: Session, token: str, purpose: str) -> models.VerificationToken:
    record = db.query(models.VerificationToken).filter_by(token=token, purpose=purpose).first()
    if not record or record.used_at is not None or record.expires_at < datetime.utcnow():
        raise HTTPException(400, "Invalid or expired token")
    return record


def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()


def verify_password(password: str, password_hash: str) -> bool:
    return bcrypt.checkpw(password.encode(), password_hash.encode())


def get_current_student(
    creds: HTTPAuthorizationCredentials = Depends(bearer_scheme),
    db: Session = Depends(get_db),
) -> models.Student:
    invalid = HTTPException(401, "Could not validate credentials")
    try:
        student_id = decode_student_id(creds.credentials)
    except jwt.PyJWTError:
        raise invalid
    student = db.get(models.Student, student_id)
    if not student:
        raise invalid
    return student


def get_current_teacher(student: models.Student = Depends(get_current_student)) -> models.Student:
    if student.role != "teacher":
        raise HTTPException(403, "Teacher access required")
    return student


@router.post("/register", response_model=schemas.TokenResponse)
def register(payload: schemas.StudentCreate, db: Session = Depends(get_db)):
    if db.query(models.Student).filter_by(email=payload.email).first():
        raise HTTPException(400, "Email already registered")
    if payload.role == "teacher":
        _check_teacher_invite_code(payload.teacher_invite_code)
    student = models.Student(
        name=payload.name, email=payload.email,
        password_hash=hash_password(payload.password),
        grade=payload.grade, stream=payload.stream, role=payload.role,
    )
    if payload.role == "student" and payload.class_join_code:
        student.class_id = _find_class_by_code(db, payload.class_join_code).id
    db.add(student)
    db.commit()
    db.refresh(student)
    if payload.role == "teacher":
        admin_email = os.environ.get("ADMIN_EMAIL")
        if admin_email:
            send_email(
                admin_email, "New teacher account registered - GapFinder",
                f"<p>A new teacher account was registered with a valid invite code:</p>"
                f"<p><b>{student.name}</b> &lt;{student.email}&gt;</p>",
            )
    return schemas.TokenResponse(access_token=create_access_token(student.id), student=student)


@router.post("/login", response_model=schemas.TokenResponse)
def login(payload: schemas.StudentLogin, db: Session = Depends(get_db)):
    student = db.query(models.Student).filter_by(email=payload.email).first()
    if not student or not verify_password(payload.password, student.password_hash):
        raise HTTPException(401, "Invalid credentials")
    return schemas.TokenResponse(access_token=create_access_token(student.id), student=student)


@router.post("/request-email-verification", response_model=schemas.MessageOut)
def request_email_verification(
    db: Session = Depends(get_db),
    student: models.Student = Depends(get_current_student),
):
    if student.email_verified:
        return schemas.MessageOut(detail="Email already verified.")
    token = _issue_token(db, student.id, "email_verify", EMAIL_VERIFY_EXPIRE_HOURS)
    link = f"{_frontend_url()}/verify-email?token={token}"
    send_email(
        student.email, "Verify your email - GapFinder",
        f"<p>Hi {student.name},</p><p>Confirm your email by clicking the link below:</p>"
        f'<p><a href="{link}">{link}</a></p><p>This link expires in {EMAIL_VERIFY_EXPIRE_HOURS} hours.</p>',
    )
    return schemas.MessageOut(detail="Verification email sent.")


@router.get("/verify-email", response_model=schemas.MessageOut)
def verify_email(token: str, db: Session = Depends(get_db)):
    record = _redeem_token(db, token, "email_verify")
    student = db.get(models.Student, record.student_id)
    student.email_verified = True
    record.used_at = datetime.utcnow()
    db.commit()
    return schemas.MessageOut(detail="Email verified.")


@router.post("/forgot-password", response_model=schemas.MessageOut)
def forgot_password(payload: schemas.ForgotPasswordRequest, db: Session = Depends(get_db)):
    # Always return the same generic message regardless of whether the
    # email is registered, to avoid leaking which emails have accounts.
    generic = schemas.MessageOut(detail="If that email is registered, a reset link has been sent.")
    student = db.query(models.Student).filter_by(email=payload.email).first()
    if not student:
        return generic
    token = _issue_token(db, student.id, "password_reset", PASSWORD_RESET_EXPIRE_HOURS)
    link = f"{_frontend_url()}/reset-password?token={token}"
    send_email(
        student.email, "Reset your password - GapFinder",
        f"<p>Hi {student.name},</p><p>Reset your password by clicking the link below:</p>"
        f'<p><a href="{link}">{link}</a></p><p>This link expires in {PASSWORD_RESET_EXPIRE_HOURS} hour(s). '
        f"If you didn't request this, you can safely ignore this email.</p>",
    )
    return generic


@router.post("/reset-password", response_model=schemas.MessageOut)
def reset_password(payload: schemas.ResetPasswordRequest, db: Session = Depends(get_db)):
    record = _redeem_token(db, payload.token, "password_reset")
    student = db.get(models.Student, record.student_id)
    student.password_hash = hash_password(payload.new_password)
    record.used_at = datetime.utcnow()
    db.commit()
    return schemas.MessageOut(detail="Password reset. You can now log in with your new password.")


@router.post("/join-class", response_model=schemas.StudentOut)
def join_class(
    payload: schemas.JoinClassRequest,
    db: Session = Depends(get_db),
    student: models.Student = Depends(get_current_student),
):
    """Lets an already-registered student join (or switch) a class after
    signup - the only way the existing seeded demo accounts, or anyone who
    skipped the optional class code at registration, can ever get
    enrolled without recreating their account."""
    class_ = _find_class_by_code(db, payload.join_code)
    student.class_id = class_.id
    db.commit()
    db.refresh(student)
    return student
