from flask import Flask, jsonify, request

from .server import app

ANIMAL_FOODS = {
    "gorila": "banana",
    "leão": "carne",
    "cavalo": "feno",
    "girafa": "folhas"
}

@app.route('/animal/<string:animal>', methods=['POST'])
def check_food(animal):
    animal = animal.lower()
    if animal not in ANIMAL_FOODS:
        return jsonify({"error": "Animal não encontrado"}), 404
    
    data = request.get_json()
    if "comida" not in data:
        return jsonify({"error": "Comida não especificada"}), 400

    comida = data["comida"].lower()
    if comida == ANIMAL_FOODS[animal]:
        return jsonify({"status": "sucesso"}), 200
    else:
        return jsonify({"status": "falha"}), 400

if __name__ == '__main__':
    app.run()

