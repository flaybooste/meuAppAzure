from flask import Flask, render_template, jsonify, Response
from flask_restful import Resource, Api
from flask_cors import CORS
from db import selectOne, selectAll
from json import dumps

app = Flask("meu app react", static_folder="./templates/static")
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
api = Api(app)

@app.route("/")
def index():
    return render_template("index.html")

#api
class SelectAll(Resource):
    def get(self):
        listadb = selectAll()
        return listadb

        
api.add_resource(SelectAll, "/api")


class SelectOne(Resource):
    def get(self, id):
        listadb = selectOne(id)
        id, title, desc, author  = listadb[0][0], listadb[0][1], listadb[0][2], listadb[0][3]
        return{
            "id" : id,
            "title" : title,
            "description" : desc,
            "author" : author
        }
api.add_resource(SelectOne, "/api/<int:id>")
