from flask import Flask

app = Flask(__name__)

@app.route("/")

def hola():
    return "<h1>Hola Mundo</h1>"