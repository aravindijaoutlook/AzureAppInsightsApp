from flask import Flask, render_template, redirect, url_for
from opencensus.ext.azure.log_exporter import AzureLogHandler
import logging

app = Flask(__name__)

# Azure Application Insights integration
logger = logging.getLogger(__name__)
logger.addHandler(AzureLogHandler(connection_string='InstrumentationKey=f8c71174-072c-405e-9a41-e4f6c5f5c0bb'))

@app.route('/')
def home():
    logger.info("Home page accessed")
    return render_template('home.html')

@app.route('/login')
def login():
    logger.info("Login page accessed")
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    logger.info("Dashboard page accessed")
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)
