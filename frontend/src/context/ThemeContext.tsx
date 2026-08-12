import { createContext, useContext, useState, useCallback, type ReactNode } from "react";

export type Theme = "light" | "dark" | "reading";
const THEME_KEY = "gls_theme";
const THEMES: Theme[] = ["light", "dark", "reading"];

function systemDefault(): Theme {
  return window.matchMedia?.("(prefers-color-scheme: dark)").matches ? "dark" : "light";
}

// Also called synchronously by the inline script in index.html (before
// React mounts) to set the same attribute pre-paint, so there's no
// flash-of-wrong-theme on load - keep the storage key/logic here as the
// single source of truth and mirror it there.
function loadStoredTheme(): Theme {
  const raw = localStorage.getItem(THEME_KEY);
  return raw && THEMES.includes(raw as Theme) ? (raw as Theme) : systemDefault();
}

interface ThemeContextValue {
  theme: Theme;
  setTheme: (theme: Theme) => void;
}

const ThemeContext = createContext<ThemeContextValue | undefined>(undefined);

export function ThemeProvider({ children }: { children: ReactNode }) {
  const [theme, setThemeState] = useState<Theme>(loadStoredTheme);

  const setTheme = useCallback((next: Theme) => {
    localStorage.setItem(THEME_KEY, next);
    document.documentElement.dataset.theme = next;
    setThemeState(next);
  }, []);

  return <ThemeContext.Provider value={{ theme, setTheme }}>{children}</ThemeContext.Provider>;
}

export function useTheme(): ThemeContextValue {
  const ctx = useContext(ThemeContext);
  if (!ctx) throw new Error("useTheme must be used within a ThemeProvider");
  return ctx;
}
