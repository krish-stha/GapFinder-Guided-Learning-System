import { useState, type FormEvent } from "react";
import { useNavigate, Link } from "react-router-dom";
import { useAuth } from "../context/AuthContext";
import { ApiError } from "../api/client";
import { homePathForRole } from "../utils/roles";
import type { Role } from "../types";
import AuthLayout from "../components/AuthLayout";

export default function RegisterPage() {
  const { register } = useAuth();
  const navigate = useNavigate();
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [role, setRole] = useState<Role>("student");
  const [grade, setGrade] = useState("");
  const [stream, setStream] = useState("");
  const [teacherInviteCode, setTeacherInviteCode] = useState("");
  const [classJoinCode, setClassJoinCode] = useState("");
  const [error, setError] = useState<string | null>(null);
  const [submitting, setSubmitting] = useState(false);

  async function handleSubmit(e: FormEvent) {
    e.preventDefault();
    setError(null);
    setSubmitting(true);
    try {
      const student = await register({
        name,
        email,
        password,
        role,
        grade: role === "student" && grade ? Number(grade) : undefined,
        stream: role === "student" && stream ? stream : undefined,
        teacher_invite_code: role === "teacher" ? teacherInviteCode : undefined,
        class_join_code: role === "student" && classJoinCode ? classJoinCode : undefined,
      });
      navigate(homePathForRole(student.role));
    } catch (err) {
      setError(err instanceof ApiError ? err.message : "Something went wrong. Try again.");
    } finally {
      setSubmitting(false);
    }
  }

  return (
    <AuthLayout>
      <form className="auth-form" onSubmit={handleSubmit}>
        <h1>Create an account</h1>
        <label>
          Name
          <input value={name} onChange={(e) => setName(e.target.value)} required />
        </label>
        <label>
          Email
          <input type="email" value={email} onChange={(e) => setEmail(e.target.value)} required />
        </label>
        <label>
          Password
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            minLength={8}
            required
          />
        </label>
        <label>
          I am a…
          <select value={role} onChange={(e) => setRole(e.target.value as Role)}>
            <option value="student">Student</option>
            <option value="teacher">Teacher</option>
          </select>
        </label>
        {role === "teacher" && (
          <label>
            Teacher invite code
            <input
              value={teacherInviteCode}
              onChange={(e) => setTeacherInviteCode(e.target.value)}
              placeholder="Ask your administrator for this"
              required
            />
          </label>
        )}
        {role === "student" && (
          <>
            <label>
              Grade (optional)
              <select value={grade} onChange={(e) => setGrade(e.target.value)}>
                <option value="">Not set</option>
                <option value="11">Grade 11</option>
                <option value="12">Grade 12</option>
              </select>
            </label>
            <label>
              Stream (optional)
              <select value={stream} onChange={(e) => setStream(e.target.value)}>
                <option value="">Not set</option>
                <option value="Science">Science</option>
                <option value="Management">Management</option>
                <option value="Humanities">Humanities</option>
              </select>
            </label>
            <label>
              Class code (optional)
              <input
                value={classJoinCode}
                onChange={(e) => setClassJoinCode(e.target.value)}
                placeholder="Ask your teacher for this"
              />
            </label>
          </>
        )}
        {error && <p className="form-error">{error}</p>}
        <button type="submit" disabled={submitting}>
          {submitting ? "Creating account…" : "Register"}
        </button>
        <p className="auth-switch">
          Already have an account? <Link to="/login">Log in</Link>
        </p>
      </form>
    </AuthLayout>
  );
}
