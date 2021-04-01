from flask import Flask, current_app
app = Flask(__name__)

@app.route('/')
def serve_js_plugin():
    return current_app.send_static_file('index.html')