import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import { AuthProvider, useAuth } from "./context/AuthContext";
import { ThemeProvider } from "./context/ThemeContext";
import { StreakProvider } from "./context/StreakContext";
import ProtectedRoute from "./components/ProtectedRoute";
import Layout from "./components/Layout";
import LoginPage from "./pages/LoginPage";
import RegisterPage from "./pages/RegisterPage";
import ForgotPasswordPage from "./pages/ForgotPasswordPage";
import ResetPasswordPage from "./pages/ResetPasswordPage";
import VerifyEmailPage from "./pages/VerifyEmailPage";
import DashboardPage from "./pages/DashboardPage";
import ChaptersPage from "./pages/ChaptersPage";
import ChapterDetailPage from "./pages/ChapterDetailPage";
import ChapterLearningPage from "./pages/ChapterLearningPage";
import ExamPage from "./pages/ExamPage";
import QuickPracticePage from "./pages/QuickPracticePage";
import PerformancePage from "./pages/PerformancePage";
import ChapterAnalysisPage from "./pages/ChapterAnalysisPage";
import WeakAreasPage from "./pages/WeakAreasPage";
import LearningPathPage from "./pages/LearningPathPage";
import ProgressPage from "./pages/ProgressPage";
import AssistantPage from "./pages/AssistantPage";
import TeacherDashboardPage from "./pages/TeacherDashboardPage";
import CohortHeatmapPage from "./pages/CohortHeatmapPage";
import StudentDetailPage from "./pages/StudentDetailPage";
import ChapterAnalyticsPage from "./pages/ChapterAnalyticsPage";
import AssessmentManagementPage from "./pages/AssessmentManagementPage";
import LearningContentManagementPage from "./pages/LearningContentManagementPage";
import ClassManagementPage from "./pages/ClassManagementPage";
import { homePathForRole } from "./utils/roles";
import "./App.css";

function HomeRedirect() {
  const { student } = useAuth();
  return <Navigate to={student ? homePathForRole(student.role) : "/login"} replace />;
}

export default function App() {
  return (
    <ThemeProvider>
      <AuthProvider>
        <StreakProvider>
          <BrowserRouter>
            <Routes>
              <Route path="/login" element={<LoginPage />} />
              <Route path="/register" element={<RegisterPage />} />
              <Route path="/forgot-password" element={<ForgotPasswordPage />} />
              <Route path="/reset-password" element={<ResetPasswordPage />} />
              <Route path="/verify-email" element={<VerifyEmailPage />} />
              <Route element={<Layout />}>
                <Route element={<ProtectedRoute role="student" />}>
                  <Route path="/dashboard" element={<DashboardPage />} />
                  <Route path="/chapters" element={<ChaptersPage />} />
                  <Route path="/chapter/:chapterId" element={<ChapterDetailPage />} />
                  <Route path="/chapter/:chapterId/learn" element={<ChapterLearningPage />} />
                  <Route path="/practice/:courseId/:chapterId" element={<ExamPage />} />
                  <Route path="/mock-test/:courseId" element={<ExamPage />} />
                  <Route path="/diagnostic/:courseId" element={<ExamPage purpose="diagnostic" />} />
                  <Route path="/quick-practice" element={<QuickPracticePage />} />
                  <Route path="/quick-practice/:courseId" element={<ExamPage purpose="practice" />} />
                  <Route path="/quick-practice/:courseId/:chapterId" element={<ExamPage purpose="practice" />} />
                  <Route path="/performance" element={<PerformancePage />} />
                  <Route path="/chapter-analysis" element={<ChapterAnalysisPage />} />
                  <Route path="/weak-areas" element={<WeakAreasPage />} />
                  <Route path="/learning-path" element={<LearningPathPage />} />
                  <Route path="/progress" element={<ProgressPage />} />
                  <Route path="/assistant" element={<AssistantPage />} />
                </Route>
                <Route element={<ProtectedRoute role="teacher" />}>
                  <Route path="/teacher" element={<TeacherDashboardPage />} />
                <Route path="/teacher/classes" element={<ClassManagementPage />} />
                  <Route path="/teacher/heatmap" element={<CohortHeatmapPage />} />
                  <Route path="/teacher/students/:studentId" element={<StudentDetailPage />} />
                  <Route path="/teacher/chapters/:chapterId" element={<ChapterAnalyticsPage />} />
                  <Route path="/teacher/assessments" element={<AssessmentManagementPage />} />
                  <Route path="/teacher/content" element={<LearningContentManagementPage />} />
                </Route>
              </Route>
              <Route path="*" element={<HomeRedirect />} />
            </Routes>
          </BrowserRouter>
        </StreakProvider>
      </AuthProvider>
    </ThemeProvider>
  );
}
