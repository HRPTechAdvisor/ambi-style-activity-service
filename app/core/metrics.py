"""
metrics.py

Purpose:
- Define application-level metrics only
- Avoid side effects at import time
- Enable consistent observability across services
This module defines application-level metrics only.
It must not start servers or register routes.

This file attempts to follow AMBI.inc / BYU SRE Standards.
"""

from prometheus_client import Counter, Histogram

# ---- Request metrics ----

REQUEST_COUNT = Counter(
    name="http_requests_total",
    documentation="Total number of HTTP requests",
    labelnames=["method", "endpoint", "status"],
)

REQUEST_LATENCY = Histogram(
    name="http_request_duration_seconds",
    documentation="HTTP request latency in seconds",
    labelnames=["method", "endpoint"],
)
