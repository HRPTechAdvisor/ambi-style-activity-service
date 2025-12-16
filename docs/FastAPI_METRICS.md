\# FastAPI\_METRICS.md — ambi-style-activity-service



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

