from fastapi import APIRouter

from services.category_service import CategoryService
from utils.response import success_response

router = APIRouter(prefix="/api/v1", tags=["Categories"])


@router.get("/categories")
def get_categories():
    categories = CategoryService.get_all()
    return success_response(categories)
