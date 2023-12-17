import pickle

from flask import Flask
from flask import request
from flask import jsonify

model_file = 'model.bin'

with open(model_file, 'rb') as f_in:
    dv, model = pickle.load(f_in)

app = Flask('house_price')


@app.route('/predict', methods=['POST'])
def predict():
    data_json = request.get_json()
    X = dv.transform([data_json])
    prediction = model.predict(X)

    result = {
        'predicted_price': float(prediction)
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)
