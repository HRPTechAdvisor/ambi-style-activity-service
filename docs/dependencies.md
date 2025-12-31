\# Dependencies



This service uses the following core dependencies:



\- \*\*FastAPI\*\*

&nbsp; Used as the application framework for defining HTTP APIs and lifecycle hooks.



\- \*\*Uvicorn\*\*

&nbsp; ASGI server used to run the FastAPI application in development and production.



\- \*\*prometheus-client\*\*

&nbsp; Provides counters, histograms, and an exposition endpoint for Prometheus-based observability.



All dependencies are pinned to exact versions to ensure reproducible builds and predictable runtime behavior, following AMBI.inc and BYU SRE best practices.



