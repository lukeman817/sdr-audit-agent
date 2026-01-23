import os
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# ==========================================================
# SECURITY VULNERABILITY: Secret Leak (Hardcoded Key)
# ==========================================================
GOOGLE_API_KEY = "AIzaSyD-Your-Dummy-Key-Here"

# Mock database for demonstrating BOLA/IDOR risks
LEADS_DATABASE = {
    "1": {"name": "Sarah Jenkins", "email": "sarah.j@enterprise-tech.com", "notes": "Direct competitor. Working on a $500k deal renewal."},
    "2": {"name": "Michael Chen", "email": "m.chen@startup-growth.io", "notes": "High priority. Inquiring about bulk discount codes."},
    "3": {"name": "Elena Rodriguez", "email": "elena@global-logistics.org", "notes": "Internal: Draft of the Q3 security audit report."}
}

@app.route('/')
def index():
    return render_template('index.html')

# ==========================================================
# DOMAIN VERIFICATION ROUTE
# Replace 'YOUR_AIKIDO_STRING_HERE' with the code from Aikido
# ==========================================================
@app.route('/aikido.txt')
def aikido_verification():
    return "YOUR_AIKIDO_STRING_HERE"

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_query = data.get('message', '')
    system_instructions = data.get('system_instructions', 'You are a professional SDR.')
    prompt = f"Instructions: {system_instructions}\nUser: {user_query}\nAgent Response:"
    return jsonify({
        "status": "success",
        "response": f"AI processing based on: {prompt}"
    })

@app.route('/api/leads/<lead_id>', methods=['GET'])
def get_lead_data(lead_id):
    lead = LEADS_DATABASE.get(str(lead_id))
    if lead:
        return jsonify(lead)
    return jsonify({"error": "Lead not found"}), 404

@app.route('/health')
def health_check():
    return jsonify({"status": "healthy"}), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
