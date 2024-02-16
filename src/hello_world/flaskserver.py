from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World from Flask!'

def run_flask() -> None:
    app.run(debug=True, port=8000)