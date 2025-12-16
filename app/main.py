"""

main.py

Main FastAPI application

Purpose:
- Serve API endpoints
- Integrate Prometheus metrics middleware
"""

from fastapi import FastAPI, Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
from prometheus_client import CONTENT_TYPE_LATEST, generate_latest
import time

from app.core.metrics import REQUEST_COUNT, REQUEST_LATENCY

app = FastAPI(title="ambi-style-activity-service")

# ---- Metrics Middleware ----
class MetricsMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start = time.time()
        response = await call_next(request)
        REQUEST_COUNT.labels(
            method=request.method,
            endpoint=request.url.path,
            status=str(response.status_code)
        ).inc()
        REQUEST_LATENCY.labels(
            method=request.method,
            endpoint=request.url.path
        ).observe(time.time() - start)
        return response

app.add_middleware(MetricsMiddleware)

# ---- Prometheus metrics endpoint ----
@app.get("/metrics")
async def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)
