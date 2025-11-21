# PROJECT VARIABLES
PY=uv run python
BACKEND=app/main.py
FRONTEND=app/frontend/main.py

# BACKEND
run-backend:
	uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

format:
	uv run ruff check --fix .
	uv run black .

migrate:
	$(PY) scripts/init_db.py

# FRONTEND
run-frontend:
	$(PY) -m app.frontend.main

# DOCKER
compose-up:
	docker compose up --build

compose-down:
	docker compose down