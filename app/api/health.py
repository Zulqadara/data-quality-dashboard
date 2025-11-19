import fastapi

router = fastapi.APIRouter(tags=["health"])

@router.get("/health")
async def health_check():
    db_health = 'unknown'

    try:
        db_health = 'connected'
    except Exception as e:
        db_health = 'DB error'

    return {
        "app status": "ok",
        "DB Status": db_health
    }