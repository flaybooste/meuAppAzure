from flask import Flask, jsonify
import db
app = Flask(__name__)

@app.route("/")
def hello():
    listadb = db.selecionarTbl()
    return jsonify(listadb)