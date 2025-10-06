# ---- Base Image ----
FROM python:3.10-slim

# ---- Working directory ----
WORKDIR /app

# ---- Copy dependencies and install ----
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ---- Copy backend source ----
COPY backend /app/backend
COPY frontend /app/frontend

# ---- Copy environment file (optional; Compose can also inject vars) ----
COPY backend/.env.example /app/.env

# ---- Expose FastAPI port ----
EXPOSE 8000

# ---- Run FastAPI with uvicorn ----
CMD ["uvicorn", "backend.app:app", "--host", "0.0.0.0", "--port", "8000"]

