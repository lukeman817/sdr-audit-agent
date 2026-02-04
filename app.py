import os
from flask import Flask, render_template, request, jsonify, redirect, url_for

app = Flask(__name__)

# Mock database for authentication
USERS = {"admin@example.com": "password123", "user@example.com": "aikido_test"}

# ==========================================================
# SECURITY VULNERABILITY: Secret Leak (Hardcoded Key)
# ==========================================================
GOOGLE_API_KEY = "AIzaSyD-Your-Dummy-Key-Here"

# Mock database for BOLA/IDOR risks
LEADS_DATABASE = {
    "1": {"name": "Sarah Jenkins", "email": "sarah.j@enterprise-tech.com", "notes": "Renewal deal."},
    "2": {"name": "Michael Chen", "email": "m.chen@startup-growth.io", "notes": "High priority."},
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Simple mock login to satisfy pentest requirements."""
    if request.method == 'POST':
        # In a real app, you'd check a DB. Here we just redirect.
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <input type="text" name="email" placeholder="Email">
            <input type="password" name="password" placeholder="Password">
            <button type="submit">Login</button>
        </form>
    '''

@app.route('/aikido.txt')
def aikido_verification():
    return "validation.aikido.529a0524bf9df99dadb6275751336ca2"

# ... (Keep your /chat and /api/leads endpoints exactly as they were) ...

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
