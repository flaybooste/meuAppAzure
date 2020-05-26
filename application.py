from flask import Flask, jsonify
from db import selectAll

app = Flask(__name__)

@app.route("/")
def hello():
    listadb = selectAll()
    id, title, desc, author  = listadb[0][0], listadb[0][1], listadb[0][2], listadb[0][3]
    return jsonify({
    "id":id,
    "title":title,
    "description":desc,
    "author": author
    })
