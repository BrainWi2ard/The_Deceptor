# Blueprint Documentation for The Deceptor (with Key Improvements)

Refer to [previous blueprint](https://github.com/BrainWi2ard/The_Deceptor/discussions/1) for full details.  
**Key improvements:**
- Scalable microservices with Docker/Kubernetes/Helm
- Open-source AI agents (Ollama, Whisper, TTS, Deepfake, Video)
- Workflow orchestration via n8n
- Vector DB (Qdrant)
- Real-time streaming (LiveKit bridge)
- Monitoring: Prometheus, Grafana, ELK/Loki
- Security: OAuth2/JWT, TLS/SSL
- MLOps: MLflow, Kubeflow (optional)

Included in this repo:
- `docker-compose.yml` for local development
- `helm/` for Kubernetes
- `src/` for agents and orchestrator
- `config/` for secrets and environment
- `monitoring/` for Prometheus/Grafana/Loki configs

## Quickstart

1. Clone repo + install Python requirements
2. Configure env files in `config/`
3. Launch with Docker Compose or Helm

## Monitoring & Security

- Prometheus and Grafana for metrics
- Loki/ELK for logs
- OAuth2/JWT endpoints
- TLS/SSL via proxy or ingress

See [README.md](../README.md) for more instructions.