from flask import jsonify, request

from .server import app

ANIMALS = {
    "gorila": {
        "nome": "Gorila",
        "idade": 10,
        "comida_preferida": "banana"
    },
    "leao": {
        "nome": "Leão",
        "idade": 8,
        "comida_preferida": "carne"
    },
    "cavalo": {
        "nome": "Cavalo",
        "idade": 5,
        "comida_preferida": "feno"
    },
    "girafa": {
        "nome": "Girafa",
        "idade": 12,
        "comida_preferida": "folhas"
    }
}

@app.route("/animal/gorila", methods=["POST"])
def gorila():
    # Obter informação de comida do corpo da requisição
    comida = request.json["comida"]
    if comida == "banana":
        return "Comida de preferência do gorila!"
    else:
        return "Comida não é de preferência do gorila."

@app.route("/animal/leao", methods=["POST"])
def leao():
    # Obter informação de comida do corpo da requisição
    comida = request.json["comida"]
    if comida == "carne":
        return "Comida de preferência do leão!"
    else:
        return "Comida não é de preferência do leão."

@app.route("/animal/cavalo", methods=["POST"])
def cavalo():
    # Obter informação de comida do corpo da requisição
    comida = request.json["comida"]
    if comida == "feno":
        return "Comida de preferência do cavalo!"
    else:
        return "Comida não é de preferência do cavalo."

@app.route("/animal/girafa", methods=["POST"])
def girafa():
    # Obter informação de comida do corpo da requisição
    comida = request.json["comida"]
    if comida == "carne":
        return "Comida de preferência da girafa!"
    else:
        return "Comida não é de preferência da girafa."

