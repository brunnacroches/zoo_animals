from flask import Flask, request

app = Flask(__name__)

@app.route('/animal/<string:animal>', methods=['POST'])
def animal(animal):
    data = request.get_json()
    food = data['food']

    if animal == 'gorila':
        if food == 'banana':
            return 'Success', 200
        else:
            return 'Failure', 400

    elif animal == 'leao':
        if food == 'carne':
            return 'Success', 200
        else:
            return 'Failure', 400

    elif animal == 'cavalo':
        if food == 'feno':
            return 'Success', 200
        else:
            return 'Failure', 400

    elif animal == 'girafa':
        if food == 'folhas':
            return 'Success', 200
        else:
            return 'Failure', 400

    else:
        return 'Invalid animal', 400

if __name__ == '__main__':
    app.run()
 