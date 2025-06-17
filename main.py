from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, supports_credentials=True)  # Enables CORS

# Dummy user database (replace with a secure database)
users_db = {"praharshitha345@gmail.com": "password123"}

@app.route('/login', methods=['OPTIONS', 'POST'])
def login():
    if request.method == "OPTIONS":
        return jsonify({"status": "ok"}), 200  # Handle preflight request

    data = request.get_json()

    # Validate request data
    if not data or 'email' not in data or 'password' not in data:
        return " Invalid request format. Please enter email and password.", 400

    email = data.get("email")
    password = data.get("password")

    if users_db.get(email) == password:
        return "Login successful. Welcome!", 200

    return "Invalid credentials. Please try again.", 401
if __name__ == '__main__':
    print("🚀 Flask server starting on http://127.0.0.1:5000")
    app.run(debug=True)
