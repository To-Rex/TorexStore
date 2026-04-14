from typing import Optional

from repositories.app_repository import AppRepository
from repositories.version_repository import VersionRepository
from repositories.user_repository import UserRepository


class DashboardService:
    @staticmethod
    def get_admin_dashboard() -> dict:
        apps = AppRepository.get_all()
        users = UserRepository.get_all()
        versions = VersionRepository.get_all()

        published = [a for a in apps if a.get("published")]
        draft = [a for a in apps if not a.get("published")]
        total_downloads = sum(a.get("totalDownloads", 0) for a in apps)
        publishers = [u for u in users if u["role"] == "publisher"]

        sorted_apps = sorted(apps, key=lambda a: a.get("updatedAt", ""), reverse=True)
        recent = sorted_apps[:5]
        recent_list = []
        for app in recent:
            latest = VersionRepository.get_latest(app["id"])
            recent_list.append(
                {
                    "id": app["id"],
                    "name": app["name"],
                    "icon": app.get("icon", ""),
                    "developer": app.get("developer", ""),
                    "latestVersion": latest["version"] if latest else "",
                    "totalDownloads": app.get("totalDownloads", 0),
                    "published": app.get("published", False),
                    "updatedAt": app.get("updatedAt", ""),
                }
            )

        return {
            "totalApps": len(apps),
            "publishedApps": len(published),
            "draftApps": len(draft),
            "totalDownloads": total_downloads,
            "totalUsers": len(users),
            "totalPublishers": len(publishers),
            "recentApps": recent_list,
        }

    @staticmethod
    def get_publisher_dashboard(user_id: str) -> dict:
        apps = AppRepository.get_all()
        versions = VersionRepository.get_all()

        user_apps = [a for a in apps if a.get("createdBy") == user_id]
        published = [a for a in user_apps if a.get("published")]
        draft = [a for a in user_apps if not a.get("published")]
        total_downloads = sum(a.get("totalDownloads", 0) for a in user_apps)

        sorted_apps = sorted(
            user_apps, key=lambda a: a.get("updatedAt", ""), reverse=True
        )
        recent = sorted_apps[:5]
        recent_list = []
        for app in recent:
            latest = VersionRepository.get_latest(app["id"])
            recent_list.append(
                {
                    "id": app["id"],
                    "name": app["name"],
                    "icon": app.get("icon", ""),
                    "developer": app.get("developer", ""),
                    "latestVersion": latest["version"] if latest else "",
                    "totalDownloads": app.get("totalDownloads", 0),
                    "published": app.get("published", False),
                    "updatedAt": app.get("updatedAt", ""),
                }
            )

        return {
            "totalApps": len(user_apps),
            "publishedApps": len(published),
            "draftApps": len(draft),
            "totalDownloads": total_downloads,
            "recentApps": recent_list,
        }
