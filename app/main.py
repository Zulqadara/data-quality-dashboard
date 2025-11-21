import fastapi
from app.api.health import router as health_router
from app.api.datasets import router as datasets_router
from app.api.upload import router as upload_router

app = fastapi.FastAPI(title="Data Quality Dashboard")

#Routes (Use more advanced routing for bigger apps)
app.include_router(health_router)
app.include_router(upload_router)
app.include_router(datasets_router)
