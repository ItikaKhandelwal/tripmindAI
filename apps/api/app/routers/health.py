from fastapi import APIRouter
from datetime import datetime
from app.db.client import get_supabase
from app.config import settings

router = APIRouter()

@router.get("/health")
async def health_check():
    """
    Health check endpoint.
    Verifies the API is running and Supabase is reachable.
    """
    db_status = "unreachable"

    try:
        # Try a lightweight query to confirm DB is connected
        supabase = get_supabase()
        supabase.table("categories").select("id").limit(1).execute()
        db_status = "connected"
    except Exception as e:
        db_status = f"error: {str(e)}"

    return {
        "status": "ok",
        "timestamp": datetime.utcnow().isoformat(),
        "environment": settings.app_env,
        "database": db_status,
        "version": "1.0.0"
    }