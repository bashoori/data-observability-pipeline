# Data Observability Pipeline

This project demonstrates a basic ETL pipeline that extracts data from a public API, transforms it, and loads it into a SQLite database.  
It’s designed as the foundation for an observability-focused pipeline, where future steps will include Prometheus and Grafana integration.

## Tools Used
- Python
- Apache Airflow
- SQLite
- Docker + Codespaces

## Run Locally
```bash
pip install -r requirements.txt


docker-compose down -v
docker-compose up --build




Then open http://localhost:8080
 to access Airflow UI.

Next Steps

Phase 2 will include:

Prometheus metrics collection

Grafana dashboards for API latency and success rate
