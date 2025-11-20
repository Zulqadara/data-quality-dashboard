from fastapi import APIRouter, UploadFile, File, HTTPException
import aiofiles
import uuid
import os

from app.core.database import get_session
from app.models.dataset import Dataset
from app.models.dataset_column import DatasetColumn
from app.services.data_reader import extract_columns

router = APIRouter()


UPLOAD_DIR = "storage/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/upload")
async def upload_dataset(file: UploadFile = File(...)):
    # Validation
    if not file.filename.endswith(".csv"):
        raise HTTPException(status_code=400, detail="Only CSV files are supported")

    # Generate a unique filename
    file_id = str(uuid.uuid4())
    stored_filename = f"{file_id}.csv"
    file_path = os.path.join(UPLOAD_DIR, stored_filename)

    # Save file
    try:
        async with aiofiles.open(file_path, "wb") as out_file:
            content = await file.read()
            await out_file.write(content)
    except Exception:
        raise HTTPException(status_code=500, detail="Failed to save file")

    # DB ops
    async with get_session() as session:
        try:
            dataset = Dataset(
                original_filename=file.filename,
                stored_filename=stored_filename,
            )
            session.add(dataset)
            await session.flush()  # get dataset.id

            try:
                column_names = await extract_columns(file_path)
            except Exception as e:
                raise HTTPException(status_code=500, detail=f"Column extraction failed: {str(e)}")

            for col in column_names:
                session.add(DatasetColumn(
                    dataset_id=dataset.id,
                    name=col,
                    data_type=None  # Day 3 will infer this
                ))

            await session.commit()
            await session.refresh(dataset)

        except Exception as e:
            await session.rollback()
            raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

    # Final response
    return {
        "message": "File uploaded successfully",
        "dataset_id": dataset.id,
        "filename": dataset.original_filename,
        "stored_file": stored_filename,
        "columns": column_names
    }
