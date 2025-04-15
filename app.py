from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome to My Flask App</h1><p>Home Page</p>"

@app.route('/login')
def login():
    return "<h1>Login Page</h1><p>User authentication goes here.</p>"

@app.route('/dashboard')
def dashboard():
    return "<h1>Dashboard</h1><p>User activities and analytics.</p>"

@app.route('/profile')
def profile():
    return "<h1>Profile Page</h1><p>User details and settings.</p>"

@app.route('/checkout')
def checkout():
    return "<h1>Checkout Page</h1><p>Complete your purchase here.</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)