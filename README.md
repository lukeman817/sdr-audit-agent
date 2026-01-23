# SDR-Audit-Agent

A Flask web application with intentionally included security vulnerabilities for security audit demonstration purposes.

## ⚠️ Security Notice

**This application contains intentional security vulnerabilities for educational and audit purposes only. Do NOT use in production environments.**

## Vulnerabilities Included

1. **Secret Leak**: Hardcoded Google API key in source code
2. **SCA/Vulnerable Dependencies**: Outdated packages with known vulnerabilities
3. **AI Risk (Prompt Injection)**: Unsanitized user input in system prompts
4. **BOLA/IDOR**: Unauthenticated access to lead data endpoints
5. **Technical Debt**: Dockerfile runs as root user

## Setup

### Prerequisites
- Python 3.9+
- Git (for version control)

### Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python app.py
```

3. Access the web interface:
- Open your browser to `http://localhost:5000`

## API Endpoints

- `GET /` - Web interface
- `POST /api/chat` - Chat endpoint (vulnerable to prompt injection)
- `GET /api/leads` - List all leads (BOLA/IDOR vulnerability)
- `GET /api/leads/<lead_id>` - Get specific lead (BOLA/IDOR vulnerability)

## Git Setup

To connect this repository to GitHub:

1. Run the setup script:
```powershell
.\setup-git.ps1
```

2. Push to GitHub:
```bash
git push -u origin main
```

Or if your default branch is `master`:
```bash
git push -u origin master
```

## Docker

Build and run with Docker:
```bash
docker build -t sdr-audit-agent .
docker run -p 5000:5000 sdr-audit-agent
```

**Note**: The Dockerfile intentionally runs as root for demonstration purposes.

## Repository

GitHub: https://github.com/lukeman817/sdr-audit-agent.git
