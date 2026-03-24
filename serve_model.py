from flask import Flask, request, jsonify
import joblib
import numpy as np
import os

app = Flask(__name__)

# Load model safely
model_path = os.path.join(os.path.dirname(__file__), 'iris_model.pkl')
model = joblib.load(model_path)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    prediction = model.predict(np.array(data['input']).reshape(1, -1))
    return jsonify({'prediction': str(prediction[0])})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)