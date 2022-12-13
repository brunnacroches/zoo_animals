from flask import Flask, jsonify, request

from .server import app

# Você pode criar uma API em Python usando o framework Flask. 
# O código abaixo demonstra como criar uma API que possui quatro rotas, 
# cada uma delas relativa a um dos animais da fazenda. 
# Cada rota aceita uma requisição HTTP do tipo 
# POST e espera que o cliente envie uma informação 
# de comida no corpo da mensagem (body). 
# Se a comida enviada for a preferida do animal em questão, 
# a API retorna um código de status 200 e uma mensagem de sucesso.
# Caso contrário, a API retorna um código de status 400 e uma mensagem
#  de falha.

# vamos criar as rotas da nossa API. As rotas são as URLs que serão 
# acessadas pelo cliente para acessar as diferentes funcionalidades 
# da nossa API. No nosso caso, precisamos criar uma rota para cada animal, 
# que será acessada através da 
# URL http://localhost:5000/animal/<nome_do_animal>.

# Para criar uma rota, precisamos utilizar o decorador @app.route e 
# passar como parâmetro a URL da rota:





# * JEITO 0 *

app = Flask(__name__)

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


