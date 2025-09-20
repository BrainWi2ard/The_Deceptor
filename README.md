# The Veil Paradox – Agentic Fraud Simulator & Automation Platform

## Overview

**The Veil Paradox** is a modular agentic AI system for simulating and analyzing advanced fraud scenarios (BEC, romance scam, CEO fraud, etc.) in a controlled, ethical, and automated environment. It leverages microservices, n8n workflow automation, persona management, and monitoring for continuous improvement.

---

## Features

- Pluggable agent registry (phishing, OSINT, social engineer, data collector, persona manager, etc.)
- Dynamic YAML scenario blueprints (20+ fraud types, easy to add more)
- Persona system (create/upload/manage avatars, style transfer, video personas)
- n8n workflow automation (visual orchestration and monitoring)
- Knowledge/RAG integration for context-aware agent actions
- ComfyUI & MCP server for agent management and multi-agent orchestration (optional)
- Monitoring & analytics (Prometheus, Grafana, ELK/Loki)
- Secure REST APIs (JWT/OAuth2), role-based access, TLS-ready endpoints
- Developer-friendly, extensible, and fully containerized

---

## Installation Guide

### Prerequisites

- Docker & Docker Compose
- Python 3.10+
- Node.js (for n8n)
- (Optional) ComfyUI, MCP Server, Prometheus, Grafana

### Step-by-Step Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/BrainWi2ard/The_Deceptor.git
   cd The_Deceptor
   ```

2. **Configure `.env` files**
   - Edit files in `config/` directory
   - Use `.env.ui` for UI-based configuration (see livekithelp.org for examples)

3. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Build and start all services**
   ```bash
   docker-compose up --build
   ```

5. **Start n8n workflow automation**
   - Install n8n: `npm install n8n -g`
   - Start n8n: `n8n`
   - Import workflow from `n8n/workflows/veil_paradox_workflow.json`
   - Access n8n UI at `http://localhost:5678`

6. **(Optional) Monitoring & Analytics**
   - Start Prometheus/Grafana: `docker-compose up prometheus grafana`
   - Access Grafana at `http://localhost:3000`
   - Access Prometheus at `http://localhost:9090`
   - ELK/Loki for logs at `http://localhost:5601` or `http://localhost:3100`

---

## Debugging & Fixes

- Use `docker-compose logs` to check agent and orchestrator startup issues.
- Check n8n UI for workflow errors.
- Monitor Prometheus/Grafana dashboards for health and metrics.
- For API errors, check agent logs and ensure endpoints are correct.
- Confirm `.env` settings for correct API keys and endpoints.

---

## Demo Instructions

- Run a demo simulation by posting to `/simulate` on orchestrator:
  ```bash
  curl -X POST http://localhost:8000/simulate -H "Content-Type: application/json" \
    -d '{"scenario":"romance","target":"target_user"}'
  ```
- Use n8n UI to trigger and monitor workflows.
- Upload persona avatars via persona manager API:
  ```bash
  curl -X POST http://localhost:8020/upload_avatar -F "avatar=@path_to_image.jpg" -F "name=Alice" -F "characteristics=Charming"
  ```

---

## Proof of Concept

- The system demonstrates autonomous agentic simulation of 20+ fraud scenarios.
- Dynamic persona creation with avatars and style transfer.
- Realtime workflow orchestration and adaptive branching.
- Knowledge/RAG integration for advanced tactics.

---

## Important Considerations & Notices

- **Ethics:** Use only in controlled, client-approved environments. Never deploy against real users without explicit consent.
- **Security:** Store API keys, credentials, and sensitive data securely in `.env` files.
- **Customization:** All agents, scenarios, and personas can be extended via YAML and FastAPI microservices.
- **Scaling:** For enterprise deployments, use Kubernetes/Helm and secure ingress.

---

## References & Acknowledgements

- [List of types of fraud](https://en.m.wikipedia.org/wiki/List_of_types_of_fraud)
- [livekithelp.org](https://www.livekithelp.org/) – for LiveKit and .env UI examples
- [FastAPI](https://fastapi.tiangolo.com/)
- [n8n Workflow Automation](https://n8n.io/)
- [Prometheus](https://prometheus.io/)
- [Grafana](https://grafana.com/)
- [MCP Server](https://github.com/BrainWi2ard/mcp-server)
- [ComfyUI](https://github.com/comfyanonymous/ComfyUI)
- [NetworkX](https://networkx.org/)

**Special thanks** to all contributors and reference projects.

---

## Acknowledgements

- Open-source community
- Contributors and testers
- Cybersecurity researchers

---

## Notice

This project is for educational, research, and enterprise simulation purposes only.  
Misuse may result in legal consequences. Always operate within the ethical boundaries defined by your organization or client.
