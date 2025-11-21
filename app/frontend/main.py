from nicegui import ui
from app.frontend.pages.home import home_page
from app.frontend.pages.dataset_detail import dataset_detail_page


@ui.page('/')
def home():
    home_page()


@ui.page('/dataset/{dataset_id}')
def dataset_detail(dataset_id: int):
    dataset_detail_page(dataset_id)


ui.run(title='Data Quality Dashboard', port=8080)
