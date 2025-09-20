# The Deceptor — Autonomous Agentic AI System

## Overview

**The Deceptor** is a modular, open-source agentic AI system designed for autonomous goal-oriented actions and live simulation tasks. This update brings in the latest microservices, orchestration, and monitoring tools for improved scalability, security, and performance.

## Key Features

- **Microservices Architecture**: All components are containerized via Docker and Kubernetes.
- **Workflow Orchestration**: Managed by n8n for flexible, visual workflows.
- **Open-Source LLM**: Local LLMs via Ollama (e.g., Llama3, WizardLM).
- **Speech & Video Agents**: Whisper (STT), Coqui/ChatTTS (TTS), Deepfake Voice, and Video generation.
- **Vector Search**: Qdrant for fast embedding queries.
- **Streaming**: Real-time audio/video via LiveKit bridge.
- **Monitoring**: Prometheus, Grafana, ELK Stack/Loki.
- **Security**: OAuth2/JWT, TLS/SSL, encrypted DB.

## Getting Started

1. **Clone the Repo**
   ```bash
   git clone https://github.com/BrainWi2ard/The_Deceptor.git
   cd The_Deceptor
   ```

2. **Configure Environment Variables**
   - Edit files in `config/` (see examples provided).

3. **Install Python Requirements**
   ```bash
   pip install -r requirements.txt
   ```

4. **Spin Up Services**
   ```bash
   docker-compose up --build
   ```
   - For production, deploy with Kubernetes using the provided Helm chart.

5. **Access Workflows**
   - n8n UI is available at `http://localhost:5678`
   - Orchestrator API at `http://localhost:8000`

## File Structure

See [`docs/BLUEPRINT.md`](docs/BLUEPRINT.md) for architecture and details.

## Deployment

- **Kubernetes**: Use `helm/` for Helm charts and auto-scaling.
- **CI/CD**: Integrate with GitLab CI/CD or ArgoCD for automated deployments.

## Monitoring

- **Grafana**: Dashboards at `http://localhost:3000`
- **ELK/Loki**: Logs at `http://localhost:5601`

## Security

- OAuth2/JWT endpoints for agents and orchestrator.
- TLS/SSL enabled via reverse proxy or ingress.

## Contributing

PRs and issues welcome! See [CONTRIBUTING.md](docs/CONTRIBUTING.md) for guidelines.

## License

MIT License.