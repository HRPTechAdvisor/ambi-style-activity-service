"""
metrics.py

Centralized Prometheus metrics definitions.

This module defines application-level metrics only.
It must not start servers or register routes.
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
