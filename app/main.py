"""
main.py

Main FastAPI application

Purpose:
- Serve API endpoints
- Integrate Prometheus metrics middleware
- Include health check and structured logging
"""

from fastapi import FastAPI, Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
from prometheus_client import CONTENT_TYPE_LATEST, generate_latest
import time
import logging

from app.core.metrics import REQUEST_COUNT, REQUEST_LATENCY

# ---- Logging setup ----
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("uvicorn.access")

# ---- FastAPI app ----
app = FastAPI(title="ambi-style-activity-service")

# ---- Metrics Middleware ----
class MetricsMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start = time.time()
        response = await call_next(request)
        duration = time.time() - start

        # Update Prometheus metrics
        REQUEST_COUNT.labels(
            method=request.method,
            endpoint=request.url.path,
            status=str(response.status_code)
        ).inc()
        REQUEST_LATENCY.labels(
            method=request.method,
            endpoint=request.url.path
        ).observe(duration)

        # Structured logging
        logger.info(f"{request.method} {request.url.path} {response.status_code} {duration:.4f}s")
        return response

app.add_middleware(MetricsMiddleware)

# ---- Health endpoint ----
@app.get("/health")
async def health():
    return {"status": "ok"}

# ---- Prometheus metrics endpoint ----
@app.get("/metrics")
async def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)
