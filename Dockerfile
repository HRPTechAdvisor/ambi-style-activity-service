# ---- Base image ----
FROM python:3.12-slim

# ---- Environment ----
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# ---- System dependencies ----
RUN apt-get update \
    && apt-get install -y --no-install-recommends curl \
    && rm -rf /var/lib/apt/lists/*

# ---- Create non-root user ----
RUN useradd --create-home --shell /usr/sbin/nologin appuser

# ---- Workdir ----
WORKDIR /app

# ---- Install dependencies (cached layer) ----
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ---- Copy application code ----
COPY app ./app

# ---- Permissions ----
RUN chown -R appuser:appuser /app

# ---- Switch to non-root user ----
USER appuser

# ---- Expose port ----
EXPOSE 8000

# ---- Run service ----
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
