from fastapi import APIRouter, HTTPException
from app.core.database import get_session
from app.models.dataset import Dataset
from app.models.dataset_column import DatasetColumn
from app.models.dataset_profile import DatasetProfile

router = APIRouter()

@router.get("/datasets")
async def list_datasets():
    async with get_session() as session:
        result = await session.execute(
            Dataset.__table__.select().order_by(Dataset.id.desc())
        )
        datasets = result.fetchall()

        return [
            {
                "id": d.id,
                "filename": d.original_filename,
                "uploaded_at": d.uploaded_at,
                "row_count": d.row_count,
            }
            for d in datasets
        ]
@router.get("/datasets/{dataset_id}")
async def get_dataset(dataset_id: int):
    async with get_session() as session:

        dataset = await session.get(Dataset, dataset_id)
        if not dataset:
            raise HTTPException(status_code=404, detail="Dataset not found")

        # columns
        col_result = await session.execute(
            DatasetColumn.__table__.select().where(
                DatasetColumn.dataset_id == dataset_id
            )
        )
        columns = col_result.fetchall()

        # profiling
        prof_result = await session.execute(
            DatasetProfile.__table__.select().where(
                DatasetProfile.dataset_id == dataset_id
            )
        )
        profiles = prof_result.fetchall()

        return {
            "dataset": {
                "id": dataset.id,
                "filename": dataset.original_filename,
                "uploaded_at": dataset.uploaded_at,
                "row_count": dataset.row_count,
            },
            "columns": [
                {
                    "id": c.id,
                    "name": c.name,
                    "data_type": c.data_type,
                }
                for c in columns
            ],
            "profile": [
                {
                    "column_name": p.column_name,
                    "inferred_type": p.inferred_type,
                    "missing_count": p.missing_count,
                    "unique_count": p.unique_count,
                }
                for p in profiles
            ],
        }

@router.get("/datasets/{dataset_id}/columns")
async def get_dataset_columns(dataset_id: int):
    async with get_session() as session:
        result = await session.execute(
            DatasetColumn.__table__.select().where(
                DatasetColumn.dataset_id == dataset_id
            )
        )
        cols = result.fetchall()

        return [
            {
                "id": c.id,
                "name": c.name,
                "data_type": c.data_type,
            }
            for c in cols
        ]

@router.get("/datasets/{dataset_id}/profile")
async def get_dataset_profile(dataset_id: int):
    async with get_session() as session:
        result = await session.execute(
            DatasetProfile.__table__.select().where(
                DatasetProfile.dataset_id == dataset_id
            )
        )
        profiles = result.fetchall()

        return [
            {
                "column_name": p.column_name,
                "inferred_type": p.inferred_type,
                "missing_count": p.missing_count,
                "unique_count": p.unique_count,
            }
            for p in profiles
        ]
