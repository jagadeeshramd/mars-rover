from flask import Flask, jsonify, request
from graph import *
import json

app = Flask(__name__)


@app.route("/getPath", methods=['POST'])
def hello():
    parsedData = json.loads(request.data)
    height = int(parsedData['boardHeight'])
    width = int(parsedData['boardWidth'])
    wallsList = parsedData['wallsList']
    startPoint = parsedData['startPoint']
    endPoint = parsedData['endPoint']
    algorithm = parsedData['algorithm']

    shortestPath = Graph(height, width, wallsList, startPoint,
                         endPoint).run_algorithm(algorithm)
    return json.dumps(shortestPath)
