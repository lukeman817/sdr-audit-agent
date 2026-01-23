import sys
import urllib3
sys.modules['urllib3.packages.six.moves'] = urllib3.packages.six.moves
from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os

app = Flask(__name__)

# Secret Leak: Hardcoded API key directly in source code
GOOGLE_API_KEY = "AIzaSyD-Your-Dummy-Key-Here"
genai.configure(api_key=GOOGLE_API_KEY)

# In-memory storage for leads (for demonstration)
LEADS_DATABASE = {
    "1": {"name": "John Doe", "email": "john.doe@example.com", "notes": "Interested in enterprise plan"},
    "2": {"name": "Jane Smith", "email": "jane.smith@example.com", "notes": "Follow up next week"},
    "3": {"name": "Bob Johnson", "email": "bob.johnson@example.com", "notes": "Budget approved, ready to close"},
    "4": {"name": "Alice Williams", "email": "alice.williams@example.com", "notes": "Needs technical demo"},
    "5": {"name": "Charlie Brown", "email": "charlie.brown@example.com", "notes": "Decision maker, high priority"}
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    """
    Chat endpoint with prompt injection vulnerability.
    User input is directly appended to system instructions without sanitization.
    """
    try:
        data = request.json
        user_message = data.get('message', '')
        system_instructions = data.get('system_instructions', '')
        
        # AI Risk: Prompt Injection Vulnerability
        # User input is directly appended without sanitization
        full_prompt = system_instructions + "\n\nUser: " + user_message + "\nAssistant:"
        
        # Initialize the model
        model = genai.GenerativeModel('gemini-pro')
        
        # Generate response
        response = model.generate_content(full_prompt)
        
        return jsonify({
            'success': True,
            'response': response.text
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/leads/<lead_id>', methods=['GET'])
def get_lead(lead_id):
    """
    BOLA/IDOR Vulnerability: No authentication or authorization checks.
    Any user can access any lead by simply knowing the ID.
    """
    if lead_id in LEADS_DATABASE:
        return jsonify({
            'success': True,
            'lead': LEADS_DATABASE[lead_id]
        })
    else:
        return jsonify({
            'success': False,
            'error': 'Lead not found'
        }), 404

@app.route('/api/leads', methods=['GET'])
def list_leads():
    """
    List all leads - also vulnerable to BOLA/IDOR
    """
    return jsonify({
        'success': True,
        'leads': LEADS_DATABASE
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
