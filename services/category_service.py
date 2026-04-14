from config import VALID_CATEGORIES, CATEGORY_LABELS
from repositories.app_repository import AppRepository


class CategoryService:
    @staticmethod
    def get_all() -> list[dict]:
        counts = AppRepository.get_by_category()
        result = []
        for cat in VALID_CATEGORIES:
            result.append(
                {
                    "id": cat.lower(),
                    "name": cat,
                    "labelUz": CATEGORY_LABELS.get(cat, cat),
                    "appCount": counts.get(cat, 0),
                }
            )
        return result
