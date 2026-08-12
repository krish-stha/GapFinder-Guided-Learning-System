import { Navigate, Outlet } from "react-router-dom";
import { useAuth } from "../context/AuthContext";
import { homePathForRole } from "../utils/roles";
import type { Role } from "../types";

export default function ProtectedRoute({ role }: { role?: Role }) {
  const { isAuthenticated, student } = useAuth();
  if (!isAuthenticated) return <Navigate to="/login" replace />;
  if (role && student && student.role !== role) return <Navigate to={homePathForRole(student.role)} replace />;
  return <Outlet />;
}
