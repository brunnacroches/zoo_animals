from flask import Flask

app = Flask(__name__)

@app.route('/animal/<animal_name>', methods=['POST'])
def check_food(animal_name):
  # Obter o corpo da solicitação HTTP
  food = request.get_json()['food']

  # Verificar se a comida é a preferida do animal
  if animal_name == 'gorila' and food == 'banana':
    return '', 200
  elif animal_name == 'leão' and food == 'carne':
    return '', 200
  elif animal_name == 'cavalo' and food == 'feno':
    return '', 200
  elif animal_name == 'girafa' and food == 'folhas':
    return '', 200
  else:
    return '', 400

if __name__ == '__main__':
  app.run()
