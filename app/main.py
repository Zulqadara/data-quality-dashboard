import fastapi
from app.api.health import router as health_router

app = fastapi.FastAPI(title="Data Quality Dashboard")

#Routes (Use more advanced routing for bigger apps)
app.include_router(health_router)