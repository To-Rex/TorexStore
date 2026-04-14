from fastapi import APIRouter, Depends

from middleware.auth import get_current_user
from services.dashboard_service import DashboardService
from utils.response import success_response

router = APIRouter(prefix="/api/v1/admin", tags=["Admin Dashboard"])


@router.get("/dashboard")
def admin_dashboard(current_user: dict = Depends(get_current_user)):
    if current_user["role"] == "admin":
        data = DashboardService.get_admin_dashboard()
    else:
        data = DashboardService.get_publisher_dashboard(current_user["sub"])
    return success_response(data)
