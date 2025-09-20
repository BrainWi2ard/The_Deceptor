# The_Deceptor

A modular framework for orchestrating AI agents, social engineering, phishing, and data collection microservices. Includes Docker and Kubernetes deployment, monitoring, and security.

## Quickstart

1. Clone the repo and install Python requirements.
2. Configure environment files in `config/`.
3. Launch with Docker Compose for local, or Helm for Kubernetes.

## Structure

- `src/agents/` — Microservice agents (social engineering, phishing, data collection)
- `monitoring/` — Prometheus and Grafana configs
- `config/` — Environment and secrets setup
- `helm/` — Kubernetes deployment charts
- `docs/` — Blueprint and scenario documentation

## Deployment

### Local (Docker Compose)

```
docker-compose up --build
```

### Kubernetes (Helm)

```
helm install deceptor ./helm
```

## Monitoring

- Prometheus: `/monitoring/prometheus.yml`
- Grafana Dashboards: `/monitoring/grafana/dashboards/`

## Security

- OAuth2/JWT endpoints
- TLS/SSL via proxy/ingress

## Agents

- Social Engineering Agent
- Phishing Agent
- Data Collector Agent

See `docs/BLUEPRINT.md` for architecture, and `docs/SCENARIO.md` for use cases.