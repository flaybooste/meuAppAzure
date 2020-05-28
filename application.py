from flask import Flask, render_template, jsonify
from db import selectOne

app = Flask("meu app react", static_folder="./templates/static")

@app.route("/")
def index():
    return render_template("index.html")

#api
@app.route("/api/<id>")
def api(id):
    listadb = selectOne(id)
    id, title, desc, author  = listadb[0][0], listadb[0][1], listadb[0][2], listadb[0][3]
    return jsonify(
        id=id,
        title=title,
        description=desc,
        author=author
                   );