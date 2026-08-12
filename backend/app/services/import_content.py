"""
Load the cleaned content-partner export (Stage 1-3 pipeline output) into the
application database. This is the CONTENT half of the pipeline described in
project brief Section 21 - raw files already validated/cleaned/filled by
clean_and_fill.py; this script just transforms into the app's own schema and
inserts.

Usage:
    python -m app.services.import_content /path/to/pipeline_out /path/to/courses.xlsx
"""
import sys, json
import pandas as pd
from pathlib import Path
from ..database import SessionLocal, engine, Base
from ..models import Course, Section, Question, QuestionChapter


def run(pipeline_dir: str, courses_xlsx: str):
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()

    print("Loading courses...")
    co = pd.read_excel(courses_xlsx, sheet_name="Result 1")
    for _, r in co.iterrows():
        db.merge(Course(id=int(r["id"]), name=r["name"], slug=r.get("slug")))
    db.commit()
    print(f"  {len(co)} courses")

    pdir = Path(pipeline_dir)

    print("Loading sections...")
    se = pd.read_csv(pdir / "clean_sections.csv")
    course_ids = {c.id for c in db.query(Course.id)}
    se = se[se["course_id"].isin(course_ids)]
    # insert in two passes so self-referencing parent_id never violates FK order
    for _, r in se.iterrows():
        db.merge(Section(
            id=int(r["id"]), name=r["name"], type=r["type"],
            parent_id=None, course_id=int(r["course_id"]),
        ))
    db.commit()
    for _, r in se.iterrows():
        if pd.notna(r["parent_id"]):
            sec = db.get(Section, int(r["id"]))
            sec.parent_id = int(r["parent_id"])
    db.commit()
    print(f"  {len(se)} sections")

    print("Loading questions...")
    q = pd.read_csv(pdir / "clean_questions.csv")
    batch = []
    for i, r in enumerate(q.itertuples(index=False), 1):
        batch.append(Question(
            id=int(r.id), body=r.body, answers_json=r.answers,
            correct_answer=None if pd.isna(r.correct_answer) else int(r.correct_answer),
            level=None if pd.isna(r.level) else int(r.level),
            difficulty_label=r.difficulty_label, question_type=r.question_type,
            source=r.source, scoreable=bool(r.scoreable),
        ))
        if len(batch) >= 2000:
            db.bulk_save_objects(batch); db.commit(); batch = []
    if batch:
        db.bulk_save_objects(batch); db.commit()
    print(f"  {len(q)} questions")

    print("Loading question-chapter links...")
    link = pd.read_csv(pdir / "question_chapter_map.csv")
    valid_q = {row[0] for row in db.query(Question.id)}
    valid_c = {row[0] for row in db.query(Section.id)}
    link = link[link["question_id"].isin(valid_q) & link["chapter_id"].isin(valid_c)]
    batch = []
    for r in link.itertuples(index=False):
        batch.append(QuestionChapter(question_id=int(r.question_id), chapter_id=int(r.chapter_id)))
        if len(batch) >= 5000:
            db.bulk_save_objects(batch); db.commit(); batch = []
    if batch:
        db.bulk_save_objects(batch); db.commit()
    print(f"  {len(link)} links")

    db.close()
    print("Import complete.")


if __name__ == "__main__":
    pipeline_dir = sys.argv[1] if len(sys.argv) > 1 else "../../Data/pipeline_out"
    courses_xlsx = sys.argv[2] if len(sys.argv) > 2 else "../../Data/courses.xlsx"
    run(pipeline_dir, courses_xlsx)
