import os
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# ==========================================================
# SECURITY VULNERABILITY: Secret Leak (Hardcoded Key)
# This placeholder key is intended to be flagged by Secret Detection.
# ==========================================================
GOOGLE_API_KEY = "AIzaSyD-Your-Dummy-Key-Here"

# Mock database for demonstrating BOLA/IDOR risks
LEADS_DATABASE = {
    "1": {
        "name": "Sarah Jenkins",
        "email": "sarah.j@enterprise-tech.com",
        "notes": "Direct competitor. Working on a $500k deal renewal."
    },
    "2": {
        "name": "Michael Chen",
        "email": "m.chen@startup-growth.io",
        "notes": "High priority. Inquiring about bulk discount codes."
    },
    "3": {
        "name": "Elena Rodriguez",
        "email": "elena@global-logistics.org",
        "notes": "Internal: Draft of the Q3 security audit report."
    }
}

@app.route('/')
def index():
    """Renders the main SDR Agent chat interface."""
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    """
    SECURITY VULNERABILITY: AI Risk (Prompt Injection)
    
    System instructions are passed from the frontend and unsanitized.
    This logic allows an attacker to 'jailbreak' the agent by manipulating
    the system_instructions variable.
    """
    data = request.get_json()
    user_query = data.get('message', '')
    
    # Hidden variable passed from the frontend (vulnerable to tampering)
    system_instructions = data.get('system_instructions', 'You are a professional SDR.')
    
    # Intentional lack of input sanitization or model guardrails
    prompt = f"Instructions: {system_instructions}\nUser: {user_query}\nAgent Response:"
    
    # Simulation logic for the AI Pentest demo
    # The presence of the GOOGLE_API_KEY variable above triggers the secret scan.
    return jsonify({
        "status": "success",
        "response": f"AI processing based on: {prompt}"
    })

@app.route('/api/leads/<lead_id>', methods=['GET'])
def get_lead_data(lead_id):
    """
    SECURITY VULNERABILITY: BOLA / IDOR
    
    This endpoint returns sensitive lead data (PII) without requiring 
    any session authentication or token validation.
    """
    # Intentional lack of authorization checks
    lead = LEADS_DATABASE.get(str(lead_id))
    
    if lead:
        return jsonify(lead)
    
    return jsonify({"error": "Lead not found"}), 404

@app.route('/health')
def health_check():
    """Basic health check for deployment services like Render."""
    return jsonify({"status": "healthy"}), 200

# ==========================================================
# TECHNICAL DEBT: Debug Mode Enabled
# Running in debug mode in production-like environments allows 
# for potential remote code execution and is a major security flag.
# ==========================================================
if __name__ == '__main__':
