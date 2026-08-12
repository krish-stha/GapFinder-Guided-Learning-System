import { useEffect, useState, type FormEvent } from "react";
import { teacherApi } from "../api/teacher";
import { contentApi } from "../api/content";
import { ApiError } from "../api/client";
import type { Course, SchoolClass, StudentSummary } from "../types";

export default function ClassManagementPage() {
  const [courses, setCourses] = useState<Course[]>([]);
  const [classes, setClasses] = useState<SchoolClass[] | null>(null);
  const [selectedClass, setSelectedClass] = useState<SchoolClass | null>(null);
  const [roster, setRoster] = useState<StudentSummary[] | null>(null);
  const [allStudents, setAllStudents] = useState<StudentSummary[]>([]);
  const [error, setError] = useState<string | null>(null);
  const [message, setMessage] = useState<string | null>(null);
  const [copiedId, setCopiedId] = useState<number | null>(null);

  const [name, setName] = useState("");
  const [courseId, setCourseId] = useState<number | "">("");
  const [addStudentId, setAddStudentId] = useState<number | "">("");

  useEffect(() => {
    contentApi.listCourses().then(setCourses).catch(() => undefined);
    teacherApi.listClasses().then(setClasses).catch((err) => setError(err instanceof ApiError ? err.message : "Could not load classes."));
  }, []);

  useEffect(() => {
    if (!selectedClass) return;
    setRoster(null);
    teacherApi.classRoster(selectedClass.id).then(setRoster).catch(() => setRoster([]));
    // Best-effort - only needed to populate the "add existing student"
    // picker, not worth failing the whole page over.
    teacherApi.studentsOverview().then(setAllStudents).catch(() => setAllStudents([]));
  }, [selectedClass]);

  async function createClass(e: FormEvent) {
    e.preventDefault();
    if (!courseId) return;
    setError(null);
    setMessage(null);
    try {
      const created = await teacherApi.createClass({ name, course_id: Number(courseId) });
      setClasses((c) => [...(c ?? []), created]);
      setName("");
      setCourseId("");
      setMessage(`"${created.name}" created - share join code ${created.join_code} with your students.`);
    } catch (err) {
      setError(err instanceof ApiError ? err.message : "Could not create the class.");
    }
  }

  async function deleteClass(cls: SchoolClass) {
    await teacherApi.deleteClass(cls.id);
    setClasses((c) => (c ?? []).filter((x) => x.id !== cls.id));
    if (selectedClass?.id === cls.id) {
      setSelectedClass(null);
      setRoster(null);
    }
  }

  async function addStudent() {
    if (!selectedClass || !addStudentId) return;
    await teacherApi.addStudentToClass(selectedClass.id, Number(addStudentId));
    const [updatedRoster, updatedClasses] = await Promise.all([
      teacherApi.classRoster(selectedClass.id),
      teacherApi.listClasses(),
    ]);
    setRoster(updatedRoster);
    setClasses(updatedClasses);
    setSelectedClass((c) => updatedClasses.find((x) => x.id === c?.id) ?? c);
    setAddStudentId("");
  }

  async function removeStudent(studentId: number) {
    if (!selectedClass) return;
    await teacherApi.removeStudentFromClass(selectedClass.id, studentId);
    const [updatedRoster, updatedClasses] = await Promise.all([
      teacherApi.classRoster(selectedClass.id),
      teacherApi.listClasses(),
    ]);
    setRoster(updatedRoster);
    setClasses(updatedClasses);
    setSelectedClass((c) => updatedClasses.find((x) => x.id === c?.id) ?? c);
  }

  function copyCode(cls: SchoolClass) {
    navigator.clipboard?.writeText(cls.join_code).then(() => {
      setCopiedId(cls.id);
      setTimeout(() => setCopiedId((id) => (id === cls.id ? null : id)), 1500);
    });
  }

  if (classes === null) return <p className="page-loading">Loading classes…</p>;

  const rosterIds = new Set((roster ?? []).map((s) => s.student_id));
  const availableStudents = allStudents.filter((s) => !rosterIds.has(s.student_id));

  return (
    <div className="teacher-page">
      <h1>Classes</h1>
      <p className="dashboard-subtitle">
        Create a class, share its join code with students, or add existing students directly.
      </p>

      {error && <p className="form-error">{error}</p>}
      {message && <p className="feedback-correct">{message}</p>}

      <section className="teacher-section">
        <h2>Create a class</h2>
        <form className="auth-form" onSubmit={createClass}>
          <label>
            Name
            <input value={name} onChange={(e) => setName(e.target.value)} placeholder="e.g. Grade 11 Science - Section A" required />
          </label>
          <label>
            Course
            <select value={courseId} onChange={(e) => setCourseId(e.target.value ? Number(e.target.value) : "")} required>
              <option value="">Select a course…</option>
              {courses.map((c) => (
                <option key={c.id} value={c.id}>{c.name}</option>
              ))}
            </select>
          </label>
          <button type="submit">Create class</button>
        </form>
      </section>

      <section className="teacher-section">
        <h2>Your classes</h2>
        {classes.length === 0 ? (
          <p className="page-loading">No classes yet - create one above.</p>
        ) : (
          <table className="teacher-table">
            <thead>
              <tr>
                <th>Name</th>
                <th>Course</th>
                <th>Join code</th>
                <th>Students</th>
                <th></th>
              </tr>
            </thead>
            <tbody>
              {classes.map((cls) => (
                <tr key={cls.id} className={selectedClass?.id === cls.id ? "selected-table-row" : undefined}>
                  <td>
                    <button type="button" className="picker-leaf-btn" onClick={() => setSelectedClass(cls)}>
                      {cls.name}
                    </button>
                  </td>
                  <td>{courses.find((c) => c.id === cls.course_id)?.name ?? `Course ${cls.course_id}`}</td>
                  <td>
                    <code>{cls.join_code}</code>{" "}
                    <button type="button" className="skip-button" onClick={() => copyCode(cls)}>
                      {copiedId === cls.id ? "Copied!" : "Copy"}
                    </button>
                  </td>
                  <td>{cls.student_count}</td>
                  <td>
                    <button type="button" className="skip-button" onClick={() => deleteClass(cls)}>
                      Delete
                    </button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        )}
      </section>

      {selectedClass && (
        <section className="teacher-section">
          <h2>Roster - {selectedClass.name}</h2>
          {roster === null ? (
            <p className="page-loading">Loading roster…</p>
          ) : roster.length === 0 ? (
            <p className="page-loading">No students enrolled yet.</p>
          ) : (
            <table className="teacher-table">
              <thead>
                <tr>
                  <th>Student</th>
                  <th>Grade / Stream</th>
                  <th></th>
                </tr>
              </thead>
              <tbody>
                {roster.map((s) => (
                  <tr key={s.student_id}>
                    <td>{s.student_name}</td>
                    <td>{s.grade ? `Grade ${s.grade}` : "-"}{s.stream ? ` · ${s.stream}` : ""}</td>
                    <td>
                      <button type="button" className="skip-button" onClick={() => removeStudent(s.student_id)}>
                        Remove
                      </button>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          )}

          <div className="option-input-row add-student-row">
            <select value={addStudentId} onChange={(e) => setAddStudentId(e.target.value ? Number(e.target.value) : "")}>
              <option value="">Add an existing student…</option>
              {availableStudents.map((s) => (
                <option key={s.student_id} value={s.student_id}>{s.student_name}</option>
              ))}
            </select>
            <button type="button" disabled={!addStudentId} onClick={addStudent}>
              Add
            </button>
          </div>
        </section>
      )}
    </div>
  );
}
