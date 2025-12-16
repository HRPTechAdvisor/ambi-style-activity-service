\# METRICS.md — ambi-style-activity-service



This document describes all Prometheus metrics defined in `app/core/metrics.py`.



\## 1. REQUEST\_COUNT

\- \*\*Type\*\*: Counter

\- \*\*Purpose\*\*: Counts all HTTP requests processed by the service.

\- \*\*Labels\*\*:

&nbsp; - `method` → HTTP method (GET, POST, etc.)

&nbsp; - `endpoint` → normalized route path

&nbsp; - `status` → HTTP status code

\- \*\*Usage\*\*: Incremented in request middleware on every HTTP request.



\## 2. REQUEST\_LATENCY

\- \*\*Type\*\*: Histogram

\- \*\*Purpose\*\*: Tracks request duration for latency analysis.

\- \*\*Labels\*\*:

&nbsp; - `method`

&nbsp; - `endpoint`

\- \*\*Usage\*\*: Observed in middleware for each request to compute latency metrics.



\### Notes

\- Metrics names follow Prometheus naming conventions.

\- Labels are chosen to support SLI/SLO definitions and error analysis.

\- All timestamps are ISO-8601 where relevant.



