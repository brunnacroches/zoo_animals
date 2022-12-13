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



#####
# * JEITO 1 *

# animals = {
#     "gorila": {
#         "nome": "Gorila",
#         "idade": 10,
#         "comida_preferida": "banana"
#     },
#     "leao": {
#         "nome": "Leão",
#         "idade": 8,
#         "comida_preferida": "carne"
#     },
#     "cavalo": {
#         "nome": "Cavalo",
#         "idade": 5,
#         "comida_preferida": "feno"
#     },
#     "girafa": {
#         "nome": "Girafa",
#         "idade": 12,
#         "comida_preferida": "folhas"
#     }
# }

# @app.route("/animal/gorila", methods=["POST"])
# def gorila():
#     # Obter informação de comida do corpo da requisição
#     comida = request.json["comida"]
#     if comida == "banana":
#         return "Comida de preferência do gorila!"
#     else:
#         return "Comida não é de preferência do gorila."

# @app.route("/animal/leao", methods=["POST"])
# def leao():
#     # Obter informação de comida do corpo da requisição
#     comida = request.json["comida"]
#     if comida == "carne":
#         return "Comida de preferência do leão!"
#     else:
#         return "Comida não é de preferência do leão."

# @app.route("/animal/cavalo", methods=["POST"])
# def cavalo():
#     # Obter informação de comida do corpo da requisição
#     comida = request.json["comida"]
#     if comida == "feno":
#         return "Comida de preferência do cavalo!"
#     else:
#         return "Comida não é de preferência do cavalo."

# @app.route("/animal/girafa", methods=["POST"])
# def girafa():
#     # Obter informação de comida do corpo da requisição
#     comida = request.json["comida"]
#     if comida == "carne":
#         return "Comida de preferência da girafa!"
#     else:
#         return "Comida não é de preferência da girafa."

########




# * JEITO 2 *
# animals = {
#     'gorila': {
#         'nome': 'Gorila',
#         'idade': 10,
#         'comida_preferida': 'banana'
#     },
#     'leão': {
#         'nome': 'Leão',
#         'idade': 5,
#         'comida_preferida': 'carne'
#     },
#     'cavalo': {
#         'nome': 'Cavalo',
#         'idade': 7,
#         'comida_preferida': 'feno'
#     },
#     'girafa': {
#         'nome': 'Girafa',
#         'idade': 8,
#         'comida_preferida': 'folhas'
#     }
# }

# @app.route('/animal/<animal_name>', methods=['POST'])
# def verificar_comida_preferida(animal_name):
#     animal = animals.get(animal_name)
#     if not animal:
#         return 'Animal não encontrado', 404

#     comida = request.json.get('comida')
#     if not comida:
#         return 'Comida não informada', 400

#     if comida == animal['comida_preferida']:
#         return 'Comida de preferência', 200
#     else:
#         return 'Comida não é de preferência', 400

####
