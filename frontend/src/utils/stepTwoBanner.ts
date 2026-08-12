// Persisted (not router-state) so the Dashboard's "Step 2" acknowledgement
// reliably shows on the NEXT time a student lands on a populated dashboard
// after finishing a diagnostic - regardless of which button/link/tab they
// actually used to get there. An earlier version carried this as
// react-router navigation state instead, which only fired if the student
// clicked one exact button on the results screen; closing the tab,
// navigating away first, or just clicking a sidebar link silently lost the
// acknowledgement even though the diagnostic had genuinely completed with
// real evidence - which is exactly the "nothing came" report this fixes.
function key(studentId: number): string {
  return `gls_step2_pending_${studentId}`;
}

export function markStepTwoPending(studentId: number) {
  localStorage.setItem(key(studentId), "1");
}

export function isStepTwoPending(studentId: number): boolean {
  return localStorage.getItem(key(studentId)) === "1";
}

export function clearStepTwoPending(studentId: number) {
  localStorage.removeItem(key(studentId));
}
