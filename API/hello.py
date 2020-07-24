from flask import Flask
from graph import *

app = Flask(__name__)


@app.route("/")
def hello():
    G = Graph(10, 10, [], (0, 0), (3, 2))
    G.run_algorithm("a")
    G = Graph(10, 10, [(2,0),(1,0),(2,2),(0,1),(3,0),(2,1)], (0, 0), (3, 2))
    G.run_algorithm("a")
    return
    #return "hello world"
