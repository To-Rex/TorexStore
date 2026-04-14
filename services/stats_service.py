from repositories.app_repository import AppRepository
from repositories.version_repository import VersionRepository


class StatsService:
    @staticmethod
    def get_stats() -> dict:
        apps = AppRepository.get_all()
        versions = VersionRepository.get_all()
        total_downloads = sum(a.get("totalDownloads", 0) for a in apps)

        from config import VALID_CATEGORIES

        return {
            "totalApps": len(apps),
            "totalVersions": len(versions),
            "totalDownloads": total_downloads,
            "totalCategories": len(VALID_CATEGORIES),
        }
