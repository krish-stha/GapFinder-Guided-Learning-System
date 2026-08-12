import { useEffect, useRef, useState } from "react";
import { useSearchParams, Link } from "react-router-dom";
import { authApi } from "../api/auth";
import { ApiError } from "../api/client";
import { useAuth } from "../context/AuthContext";
import AuthLayout from "../components/AuthLayout";

export default function VerifyEmailPage() {
  const [searchParams] = useSearchParams();
  const token = searchParams.get("token");
  const { student, updateStudent } = useAuth();

  const [state, setState] = useState<"loading" | "done" | "error">("loading");
  const [message, setMessage] = useState("");
  // The token is single-use server-side, so this effect must fire exactly
  // once per token even under React StrictMode's dev-mode double-invoke -
  // otherwise the second call always sees "already used" and shows a
  // false error right after a true success.
  const requestedTokenRef = useRef<string | null>(null);

  useEffect(() => {
    if (!token) {
      setState("error");
      setMessage("This link is missing its verification token.");
      return;
    }
    if (requestedTokenRef.current === token) return;
    requestedTokenRef.current = token;
    authApi
      .verifyEmail(token)
      .then((res) => {
        setMessage(res.detail);
        setState("done");
        // if the verifying student happens to be logged in on this device,
        // reflect the change immediately without requiring a re-login
        if (student && !student.email_verified) updateStudent({ email_verified: true });
      })
      .catch((err) => {
        setMessage(err instanceof ApiError ? err.message : "Could not verify this email.");
        setState("error");
      });
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [token]);

  return (
    <AuthLayout>
      <div className="auth-form">
        <h1>Email verification</h1>
        {state === "loading" && <p>Verifying…</p>}
        {state !== "loading" && <p className={state === "error" ? "form-error" : undefined}>{message}</p>}
        <p className="auth-switch">
          <Link to={student ? "/dashboard" : "/login"}>{student ? "Back to dashboard" : "Back to log in"}</Link>
        </p>
      </div>
    </AuthLayout>
  );
}
