Data Quality Dashboard (FastAPI + PostgreSQL + NiceGUI)

A lightweight internal tool for uploading CSV datasets, analyzing basic data-quality metrics, and visualizing results through a simple NiceGUI dashboard.
Designed to demonstrate end-to-end engineering across backend, frontend, DevOps, and AWS architecture.

How to run backend:
uv sync 

uv run uvicorn app.main:app --reload

How to run frontend:

uv run python -m app.frontend.main

