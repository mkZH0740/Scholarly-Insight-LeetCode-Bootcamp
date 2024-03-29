from flask import Flask
from flask_restful import Api

from arxiv_api import ArxivQuery

app = Flask(__name__)
api = Api(app)

api.add_resource(ArxivQuery, "/arxiv")


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
