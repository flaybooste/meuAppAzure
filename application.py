from flask import Flask, jsonify
from db import selectAll

app = Flask(__name__)

@app.route("/")
def hello():
    listadb = selectAll()
    return jsonify({listadb})
