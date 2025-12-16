\# FastAPI\_METRICS.md — ambi-style-activity-service


Purpose:

\- Explain how FastAPI is instrumented using centralized metrics.

\- Show how FastAPI app integrates with metrics.py

\- Explain middleware logic and /metrics endpoint

\- Provide educational context and operational insight


\## Integration Steps

1\. Import metrics from `app.core.metrics`:
2. Add `MetricsMiddleware` (wrap all incoming requests to update metrics automatically).

3\. Expose `/metrics` endpoint using Prometheus `generate\_latest()` and `CONTENT\_TYPE\_LATEST`.



\## Best Practices

\- Keep metric definitions separate from runtime logic

\- Middleware handles metric updates for all endpoints

\- Enables Prometheus to scrape metrics consistently



This document explains how to \*\*instrument FastAPI\*\* using the centralized metrics module.



\## 1. Middleware Integration



\- `MetricsMiddleware` wraps every request

\- Records:

&nbsp; - REQUEST\_COUNT

&nbsp; - REQUEST\_LATENCY

\- Automatically labels requests by method, endpoint, and status



\## 2. /metrics endpoint



\- Exposes all Prometheus metrics

\- Used by monitoring systems to scrape service metrics

\- Follows industry-standard format for Prometheus



\## 3. Benefits



\- Centralized metrics

\- Observability-first design

\- SRE-friendly

