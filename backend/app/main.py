from pathlib import Path
from dotenv import load_dotenv
# explicit path, not the frame-based auto-search dotenv does by default: under
# uvicorn --reload's Windows subprocess bootstrap, the auto-search can resolve
# from the wrong caller frame and silently find no .env at all.
load_dotenv(Path(__file__).resolve().parent.parent / ".env")  # must run before importing anything that reads env vars at import time

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import Base, engine, run_dev_migrations
from .routers import auth, content, practice, teacher

Base.metadata.create_all(bind=engine)
run_dev_migrations()

app = FastAPI(title="GapFinder")

# dev-only: the Vite dev server runs on a different origin than the API.
# Tighten this to the real deployed frontend origin before any production use.
# A regex (not a fixed allow_origins list) because Vite auto-increments past
# 5173 whenever that port's already taken - which happens easily in this
# project (multiple dev-server instances started across terminals/sessions)
# and previously caused every API call to silently CORS-fail with no useful
# error in the app's own UI. Still localhost-only.
app.add_middleware(
    CORSMiddleware,
    allow_origin_regex=r"http://(localhost|127\.0\.0\.1):517\d",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(content.router)
app.include_router(practice.router)
app.include_router(teacher.router)


@app.get("/health")
def health():
    return {"status": "ok"}
