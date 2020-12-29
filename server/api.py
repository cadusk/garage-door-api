from flask import Response, jsonify

from .app import app
from garage import GarageDoorBuilder

garage_door = GarageDoorBuilder.build(app.config["GARAGE_DOOR_CONFIG"])

@app.route("/", methods=['GET'])
def status():
  result = garage_door.status
  return jsonify(status=result)

@app.route("/close", methods=['GET'])
def close():
  garage_door.close()
  return Response(status=200)

@app.route("/open", methods=['GET'])
def open():
  garage_door.open()
  return Response(status=200)

