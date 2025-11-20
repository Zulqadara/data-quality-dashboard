import fastapi
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends
from app.core.database import get_session
from sqlalchemy import text

router = fastapi.APIRouter(tags=["health"])

@router.get("/health")
async def health_check(session: AsyncSession = Depends(get_session)):
    db_health = 'unknown'

    try:
        await session.execute(text("SELECT 1"))
        db_health = 'connected'
    except Exception as e:
        db_health = 'DB error'

    return {
        "app status": "ok",
        "DB Status": db_health
    }