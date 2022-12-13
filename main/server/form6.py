from flask import Flask, request

app = Flask(__name__)

animals = {
    'gorila': {
        'idade': 12,
        'comida_preferida': 'banana'
    },
    'leão': {
        'idade': 5,
        'comida_preferida': 'carne'
    },
    'cavalo': {
        'idade': 8,
        'comida_preferida': 'feno'
    },
    'girafa': {
        'idade': 3,
        'comida_preferida': 'folhas'
    }
}

@app.route('/animal/<string:nome>', methods=['POST'])
def animal(nome):
    animal = animals.get(nome)
    if not animal:
        return 'Animal não encontrado', 404
    
    comida = request.json.get('comida')
    if comida == animal['comida_preferida']:
        return 'Comida preferida encontrada', 200
    else:
        return 'Comida incorreta', 400

if __name__ == '__main__':
    app.run()
