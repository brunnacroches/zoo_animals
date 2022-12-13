from flask import Flask, jsonify, request

from .server import app

# * JEITO 2 *
animals = {
    'gorila': {
        'nome': 'Gorila',
        'idade': 10,
        'comida_preferida': 'banana'
    },
    'leão': {
        'nome': 'Leão',
        'idade': 5,
        'comida_preferida': 'carne'
    },
    'cavalo': {
        'nome': 'Cavalo',
        'idade': 7,
        'comida_preferida': 'feno'
    },
    'girafa': {
        'nome': 'Girafa',
        'idade': 8,
        'comida_preferida': 'folhas'
    }
}

@app.route('/animal/<animal_name>', methods=['POST'])
def verificar_comida_preferida(animal_name):
    animal = animals.get(animal_name)
    if not animal:
        return 'Animal não encontrado', 404

    comida = request.json.get('comida')
    if not comida:
        return 'Comida não informada', 400

    if comida == animal['comida_preferida']:
        return 'Comida de preferência', 200
    else:
        return 'Comida não é de preferência', 400

