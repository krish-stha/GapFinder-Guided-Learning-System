import { useState, type FormEvent } from "react";
import { Link } from "react-router-dom";
import { authApi } from "../api/auth";
import { ApiError } from "../api/client";
import AuthLayout from "../components/AuthLayout";

export default function ForgotPasswordPage() {
  const [email, setEmail] = useState("");
  const [message, setMessage] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [submitting, setSubmitting] = useState(false);

  async function handleSubmit(e: FormEvent) {
    e.preventDefault();
    setError(null);
    setSubmitting(true);
    try {
      const res = await authApi.forgotPassword(email);
      setMessage(res.detail);
    } catch (err) {
      setError(err instanceof ApiError ? err.message : "Something went wrong. Try again.");
    } finally {
      setSubmitting(false);
    }
  }

  return (
    <AuthLayout>
      <form className="auth-form" onSubmit={handleSubmit}>
        <h1>Forgot password</h1>
        {message ? (
          <p>{message}</p>
        ) : (
          <>
            <label>
              Email
              <input type="email" value={email} onChange={(e) => setEmail(e.target.value)} required />
            </label>
            {error && <p className="form-error">{error}</p>}
            <button type="submit" disabled={submitting}>
              {submitting ? "Sending…" : "Send reset link"}
            </button>
          </>
        )}
        <p className="auth-switch">
          <Link to="/login">Back to log in</Link>
        </p>
      </form>
    </AuthLayout>
  );
}
