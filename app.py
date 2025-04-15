from flask import Flask
from opencensus.ext.azure.trace_exporter import AzureExporter
from opencensus.trace.samplers import ProbabilitySampler
from opencensus.trace.tracer import Tracer

app = Flask(__name__)

exporter = AzureExporter(connection_string="InstrumentationKey=f8c71174-072c-405e-9a41-e4f6c5f5c0bb")
tracer = Tracer(exporter=exporter, sampler=ProbabilitySampler(1.0))

@app.before_request
def before_request():
    tracer.start_span(name="Flask Request")

@app.after_request
def after_request(response):
    tracer.end_span()
    return response

@app.route('/')
def home():
    return """
    <h1>Welcome to My Flask App</h1>
    <p>Home Page</p>
    <ul>
        <li><a href="/login">Login</a></li>
    </ul>
    """

@app.route('/login')
def login():
    return """
    <h1>Login Page</h1>
    <p>User authentication goes here.</p>
    <ul>
        <li><a href="/">Home</a></li>
    </ul>
    """
