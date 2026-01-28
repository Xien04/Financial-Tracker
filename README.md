# Financial Tracker (FastAPI)

## Quick start

1) Create a virtual environment and install dependencies:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install fastapi uvicorn sqlalchemy pydantic
```

2) Copy env file:

```powershell
Copy-Item .env.example .env
```

3) Run the app:

```powershell
uvicorn app.main:app --reload
```

## Health check

GET /api/health
