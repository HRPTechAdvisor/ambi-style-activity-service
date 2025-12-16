\# METRICS.md



\## 1. Purpose



\- Describe what each metric measures and why it exists

\- Central location for all metrics while it will explain the centralized metrics definitions

\- Avoids duplicate registrations

\- Enables consistent observability / Provide context for engineers or students learning observability


# Centralized Metrics — ambi-style-activity-service



\## 2. Metrics Defined



\### REQUEST\_COUNT

\- Type: Counter

\- Labels: method, endpoint, status

\- Purpose: track total number of HTTP requests



\### REQUEST\_LATENCY

\- Type: Histogram

\- Labels: method, endpoint

\- Purpose: track request latency in seconds



Explain the rationale for centralized metrics definitions.



\## Metrics Module (`app/core/metrics.py`)

\- `REQUEST\_COUNT`: Counter tracking total requests with labels `method`, `endpoint`, `status`

\- `REQUEST\_LATENCY`: Histogram tracking request duration per method/endpoint



\## Best Practices

\- Metrics defined once, imported elsewhere

\- No runtime behavior in the module

\- Promotes \*\*consistency and observability\*\* across services



\## References

\- Prometheus Python client: https://github.com/prometheus/client\_python

\- Google SRE Book: https://sre.google/sre-book/table-of-contents

\- Observability patterns: https://prometheus.io/docs/introduction/overview/



