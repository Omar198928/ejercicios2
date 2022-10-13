from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve

app = Flask(__name__)
cors = CORS(app)


@app.route("/omar/<string:variable1>", methods=['GET'])
def omarPrueba(variable1):
    mensajeJson = {}
    mensajeJson["id_del_grupo"] = 25
    mensajeJson["idVariable"] = variable1
    return jsonify(mensajeJson)


def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data


if __name__ == '__main__':
    dataConfig = loadFileConfig()
    print("Server running : " + "http://" + dataConfig["url-backend"] + ":" + str(dataConfig["port"]))
    serve(app, host=dataConfig["url-backend"], port=dataConfig["port"])
