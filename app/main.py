"""
main.py

Main FastAPI application

Purpose:
- Serve API endpoints
- Integrate Prometheus metrics middleware
- Include health check, readiness check, and structured logging
"""

from fastapi import FastAPI, Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
from prometheus_client import CONTENT_TYPE_LATEST, generate_latest
import json
import time
import logging

from app.core.metrics import REQUEST_COUNT, REQUEST_LATENCY

# ---- Logging setup ----
logger = logging.getLogger("app")
logger.setLevel(logging.INFO)

# ---- FastAPI app ----
app = FastAPI(title="ambi-style-activity-service")


# ---- Metrics Middleware ----
class MetricsMiddleware(BaseHTTPMiddleware):
    """
    Middleware to record request metrics and log requests safely.

    Features:
    - Measures request latency and records Prometheus metrics
    - Counts requests by method, endpoint, and status
    - Logs request method, path, status, duration, and client IP
    - Avoids Uvicorn formatter conflicts
    """

    async def dispatch(self, request: Request, call_next):
        start = time.time()
        response = await call_next(request)
        duration = time.time() - start

        # ---- Update Prometheus metrics ----
        REQUEST_COUNT.labels(
            method=request.method,
            endpoint=request.url.path,
            status=str(response.status_code),
        ).inc()

        REQUEST_LATENCY.labels(
            method=request.method,
            endpoint=request.url.path,
        ).observe(duration)

        # ---- Structured logging ----
        log_entry = {
            "method": request.method,
            "endpoint": request.url.path,
            "status": response.status_code,
            "duration": duration,
            "client": request.client.host,
        }
        print(json.dumps(log_entry))  # JSON output to stdout for centralized logging

        return response


# Attach metrics middleware
app.add_middleware(MetricsMiddleware)


# ---- Health endpoint ----
@app.get("/health")
async def health():
    """
    Liveness check endpoint.
    Returns a JSON response {"status": "ok"}.
    """
    return {"status": "ok"}


# ---- Readiness endpoint ----
@app.get("/ready")
async def ready():
    """
    Readiness check endpoint.
    Returns {"status": "ready"} if the app is ready to serve traffic.
    """
    return {"status": "ready"}


# ---- Prometheus metrics endpoint ----
@app.get("/metrics")
async def metrics():
    """
    Returns Prometheus metrics for this service.
    Example metrics:
      - http_requests_total
      - http_request_duration_seconds
    """
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)
