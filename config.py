import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

DATA_DIR = BASE_DIR / "data"
UPLOADS_DIR = DATA_DIR / "uploads"
ICONS_DIR = UPLOADS_DIR / "icons"
SCREENSHOTS_DIR = UPLOADS_DIR / "screenshots"
APKS_DIR = UPLOADS_DIR / "apks"
AVATARS_DIR = UPLOADS_DIR / "avatars"

USERS_JSON = DATA_DIR / "users.json"
APPS_JSON = DATA_DIR / "apps.json"
VERSIONS_JSON = DATA_DIR / "versions.json"

for d in [DATA_DIR, UPLOADS_DIR, ICONS_DIR, SCREENSHOTS_DIR, APKS_DIR, AVATARS_DIR]:
    d.mkdir(parents=True, exist_ok=True)

SECRET_KEY = os.getenv("SECRET_KEY", "torex-store-super-secret-key-2026")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60
REFRESH_TOKEN_EXPIRE_DAYS = 7

BASE_URL = os.getenv("BASE_URL", "http://127.0.0.1:8000/api/v1")

VALID_CATEGORIES = [
    "Productivity",
    "Communication",
    "Development",
    "Security",
    "Media",
    "Utilities",
    "Finance",
    "Education",
]

CATEGORY_LABELS = {
    "Productivity": "Samaradorlik",
    "Communication": "Aloqa",
    "Development": "Dasturlash",
    "Security": "Xavfsizlik",
    "Media": "Media",
    "Utilities": "Yordamchi",
    "Finance": "Moliya",
    "Education": "Ta'lim",
}
