from flask import jsonify, request
from view.action_view import (ActionViewCavalo, ActionViewGirafa,
                              ActionViewGorila, ActionViewLeao)

from server import app


@app.route("/animal/gorila", methods=["POST"])
def gorila():
    # Obter informação de comida do corpo da requisição
    action_view = ActionViewGorila()
    
    http_response = action_view.view_action(request)
    
    return jsonify(http_response["data"]), http_response["status_code"]


@app.route("/animal/leao", methods=["POST"])
def leao():
    # Obter informação de comida do corpo da requisição
    action_view = ActionViewLeao()
    
    http_response = action_view.view_action(request)
    
    return jsonify(http_response["data"]), http_response["status_code"]


@app.route("/animal/cavalo", methods=["PATCH"])
def cavalo():
    # Obter informação de comida do corpo da requisição
    action_view = ActionViewCavalo()
    
    http_response = action_view.view_action(request)
    
    return jsonify(http_response["data"]), http_response["status_code"]

@app.route("/animal/girafa", methods=["PATCH"])
def girafa():
    # Obter informação de comida do corpo da requisição
    action_view = ActionViewGirafa()
    
    http_response = action_view.view_action(request)
    
    return jsonify(http_response["data"]), http_response["status_code"]
