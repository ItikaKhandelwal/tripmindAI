from fastapi import APIRouter, HTTPException

router = APIRouter(prefix="/trips", tags=["trips"])

@router.get("/")
async def list_trips():
    """List all trips for the current user."""
    # TODO: add auth + Supabase query
    return {"message": "list trips - coming soon"}

@router.post("/")
async def create_trip():
    """Create a new trip."""
    # TODO: add auth + Supabase insert
    return {"message": "create trip - coming soon"}

@router.get("/{trip_id}")
async def get_trip(trip_id: str):
    """Get a single trip by ID."""
    return {"message": f"get trip {trip_id} - coming soon"}

@router.patch("/{trip_id}")
async def update_trip(trip_id: str):
    """Update a trip."""
    return {"message": f"update trip {trip_id} - coming soon"}

@router.delete("/{trip_id}")
async def delete_trip(trip_id: str):
    """Delete a trip."""
    return {"message": f"delete trip {trip_id} - coming soon"}