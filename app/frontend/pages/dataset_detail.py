from nicegui import ui
import httpx


API_URL = "http://localhost:8000"


async def fetch_dataset(dataset_id):
    async with httpx.AsyncClient() as client:
        r = await client.get(f"{API_URL}/datasets/{dataset_id}")
        return r.json()


def dataset_detail_page(dataset_id: int):

    ui.button("⬅ Back", on_click=lambda: ui.open('/')).classes("mb-4")

    data_container = ui.column().classes("w-full")

    async def load():
        data = await fetch_dataset(dataset_id)
        ds = data["dataset"]

        # Header
        with data_container:
            ui.label(f"📁 {ds['filename']}").classes("text-2xl font-bold mb-2")
            ui.label(f"Uploaded: {ds['uploaded_at']}")

        # Columns
        with data_container:
            ui.label("📌 Columns").classes("text-xl mt-6 mb-2")
            ui.table(
                columns=[
                    {"name": "name", "label": "Name", "field": "name"},
                    {"name": "data_type", "label": "Data Type", "field": "data_type"},
                ],
                rows=data["columns"],
            ).classes("w-full")

        # Profiling
        with data_container:
            ui.label("📊 Profiling").classes("text-xl mt-6 mb-2")
            ui.table(
                columns=[
                    {"name": "column_name", "label": "Column", "field": "column_name"},
                    {"name": "inferred_type", "label": "Type", "field": "inferred_type"},
                    {"name": "missing_count", "label": "Missing", "field": "missing_count"},
                    {"name": "unique_count", "label": "Unique", "field": "unique_count"},
                ],
                rows=data["profile"],
            ).classes("w-full")

    ui.timer(0.1, load, once=True)
