from flask import Flask, request

app = Flask(__name__)

ANIMAIS = {
    "gorila": {"nome": "Gorila", "idade": 5, "comida_preferida": "banana"},
    "leao": {"nome": "Leão", "idade": 3, "comida_preferida": "carne"},
    "cavalo": {"nome": "Cavalo", "idade": 4, "comida_preferida": "feno"},
    "girafa": {"nome": "Girafa", "idade": 2, "comida_preferida": "folhas"},
}

@app.route('/animal/<animal>', methods=['POST'])
def animal(animal):
    if animal not in ANIMAIS:
        # Retorna um erro 404 caso o animal não exista
        return "Animal não encontrado", 404

    # Obtém a comida enviada pelo cliente
    comida = request.json.get('comida')
    if comida is None:
        # Retorna um erro 400 caso o cliente não envie a comida
        return "Comida não informada", 400

    animal_info = ANIMAIS[animal]
   
