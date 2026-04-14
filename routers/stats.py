from fastapi import APIRouter

from services.stats_service import StatsService
from utils.response import success_response

router = APIRouter(prefix="/api/v1", tags=["Stats"])


@router.get("/stats")
def get_stats():
    stats = StatsService.get_stats()
    return success_response(stats)
