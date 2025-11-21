from nicegui import ui
import httpx


API_URL = "http://localhost:8000"  # FastAPI backend


async def fetch_datasets():
    async with httpx.AsyncClient() as client:
        r = await client.get(f"{API_URL}/datasets")
        return r.json()


async def upload_file(e):
    file = e.content

    async with httpx.AsyncClient() as client:
        r = await client.post(
            f"{API_URL}/upload",
            files={"file": (file.name, file)}
        )

    ui.notify("Upload complete", type='positive')
    ui.open("/")


def home_page():

    ui.label("📊 Data Quality Dashboard").classes("text-2xl mb-4 font-bold")

    # Upload section
    with ui.card().classes("mb-6 p-6"):
        ui.label("Upload a CSV file").classes("text-lg")
        ui.upload(on_upload=upload_file, auto_upload=True, label="Upload CSV")

    # Dataset list
    with ui.card().classes("p-6 w-full"):
        ui.label("Uploaded Datasets").classes("text-lg mb-3 font-bold")

        table = ui.table(
            columns=[
                {"name": "id", "label": "ID", "field": "id"},
                {"name": "filename", "label": "Filename", "field": "filename"},
                {"name": "row_count", "label": "Rows", "field": "row_count"},
            ],
            rows=[],
            row_key="id",
            on_select=lambda e: ui.open(f"/dataset/{e['id']}")
        ).classes("w-full")

        async def load():
            table.rows = await fetch_datasets()

        ui.timer(0.1, load, once=True)
