import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from config import DATA_DIR, UPLOADS_DIR
from routers import (
    auth,
    apps,
    admin_apps,
    admin_versions,
    admin_screenshots,
    admin_dashboard,
    admin_users,
    upload,
    categories,
    stats,
)

app = FastAPI(
    title="Torex Store API",
    description="Android Ilovalar Tarqatish Platformasi",
    version="1.0.0",
)

ALLOWED_ORIGINS = [
    "http://localhost:8080",
    "http://127.0.0.1:8080",
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/uploads", StaticFiles(directory=str(UPLOADS_DIR)), name="uploads")

app.include_router(auth.router)
app.include_router(apps.router)
app.include_router(admin_apps.router)
app.include_router(admin_versions.router)
app.include_router(admin_screenshots.router)
app.include_router(admin_dashboard.router)
app.include_router(admin_users.router)
app.include_router(upload.router)
app.include_router(categories.router)
app.include_router(stats.router)


@app.get("/api/v1/health")
def health_check():
    return {"status": "ok"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app")
