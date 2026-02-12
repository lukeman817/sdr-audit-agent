# 🤖 SDR Audit Agent: The "Vibe Coding" Security Experiment

### **Executive Summary**
This project demonstrates the **Velocity vs. Validation Gap**—the paradox where AI-assisted development tools accelerate shipping speeds by 10x while simultaneously creating invisible security debt. I built this functional SDR Audit Agent to observe how rapid development can introduce critical vulnerabilities into the software development life cycle (SDLC) if automated guardrails are not prioritized.

**Live Demo:** [https://sdr-audit-agent.onrender.com](https://sdr-audit-agent.onrender.com)

---

### **The Technical Receipt**
* **IDE:** Cursor (AI-Native Code Editor)
* **Language:** Python / Flask
* **LLM:** Google Gemini 1.5 Pro / Flash
* **Deployment:** Render
* **Validation:** Verified via **Aikido Security**

---

### **Practitioner Insights (The "Audit" Perspective)**
As a Technical AE, I believe you can't effectively sell security without understanding the developer's friction. By auditing my own AI-generated build, I identified three critical vulnerabilities that represent major business risks for AI-native companies:

#### **1. BOLA / IDOR (Broken Object Level Authorization)**
The lead retrieval logic relied on predictable integer IDs without session validation. 
* **Business Risk:** Unauthorized extraction of sensitive PII, representing a critical failure in GDPR/SOC2 compliance.
* **Status:** Identified in lead retrieval routes.

![BOLA Vulnerability Screenshot](BOLA_IDOR_Vulnerability.png)

#### **2. Prompt Injection & AI Logic Manipulation**
The agent appends unsanitized user notes directly to the system prompt.
* **Business Risk:** Allows an attacker to manipulate automated business logic or exfiltrate internal system instructions.
* **Status:** Identified in `app.py`.

![Secret Leak and Prompt Injection](Secret_Leak_Vulnerability.png)

#### **3. Secret Sprawl & Latent Risk**
The rapid development phase led to hardcoded API keys directly in the source code.
* **Business Risk:** Hardcoded credentials are a primary vector for supply chain attacks and unauthorized API usage.

---

### **Continuous Validation & Scaling**
To ensure this build meets enterprise standards, I integrated this repository with **Aikido Security** for automated assessment.

* **100% Endpoint Coverage:** The scan audited all 6 endpoints, including the logic-heavy `/chat` route.
* **Agentic AI Attacker Agents:** I utilized AI-native attacker agents to perform hardening checks, mirroring the new standard for rapid security validation.

![Aikido AI Agent Logic](Aikido_AI_Agent_Logic.png)

---

### **Deployment Status**
The application is continuously deployed via **Render**, providing a live environment to test these vulnerabilities in a real-world setting.

![Render Deployment Status](Render_Deployment_Status.png)

---

### **Why I Built This**
The next generation of security disruption isn't just about finding bugs—it's about **automated guardrails**. As development moves at the speed of Agentic AI, the security industry must provide tools that integrate seamlessly into the developer's workflow (like Cursor) to ensure we aren't shipping "vulnerable by design" software.

---

### **Getting Started**
1.  **Clone the repo:** `git clone https://github.com/lukeman817/sdr-audit-agent`
2.  **Install requirements:** `pip install -r requirements.txt`
3.  **Environment Variables:** Add your API key to a `.env` file (not provided in repo).
4.  **Run locally:** `python app.py`

---

### **Connect with me**
**LinkedIn:** [linkedin.com/in/fergusonluke](https://www.linkedin.com/in/fergusonluke/) | **Email:** lukeferguson817@gmail.com

---
*Disclaimer: This application is intentionally vulnerable and was built for educational and demonstration purposes. Do not use this code in a production environment without implementing proper security guardrails.*
