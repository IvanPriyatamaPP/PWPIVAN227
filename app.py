from flask import Flask, render_template, jsonify, request, render_template, session, flash
from app.models import User

# Create the Flask app
app = Flask(__name__)

# Define routes
@app.route('/')
def login():
    return render_template('login.html')

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
