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
# Uvicorn access logger (structured)
logger = logging.getLogger("uvicorn.access")
logger.setlevel(logging.INFO)
logger.propagate = False # Prevent double formatting

# ---- FastAPI app ----
app = FastAPI(title="ambi-style-activity-service")

# ---- Metrics Middleware ----

class MetricsMiddleware(BaseHTTPMiddleware):
        """
    Middleware to record request metrics and log requests safely.

    Features:
    - Measures request latency and records Prometheus metrics
    - Counts requests by method, endpoint, and status
    - Logs request method, path, status, and duration
    - Avoids Uvicorn formatter conflicts
    """
    
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

       # ---- Structured log (string only to avoid formatting errors) ----
        log_message = f"{request.method} {request.url.path} {response.status_code} {duration:.4f}s"
        logger.info(log_message)

        return response
        
# Attach middleware
app.add_middleware(MetricsMiddleware)

# ---- Health endpoint ----
@app.get("/health")
async def health():
      """
    Liveness check endpoint.
    Returns a JSON response {"status": "ok"}.
    """
    return {"status": "ok"}

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
