import type { Role } from "../types";

export function homePathForRole(role: Role): string {
  return role === "teacher" ? "/teacher" : "/dashboard";
}
