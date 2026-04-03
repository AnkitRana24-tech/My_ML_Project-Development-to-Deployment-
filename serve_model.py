#Import required libraries
from flask import Flask, request, jsonify
import joblib
import numpy as np
import os

app = Flask(__name__)

@app.route('/')   #When someone visits the root URL (/), run the function below
def home():       #This is the function that runs when the / route is accessed.
    return "ML API is running 🚀"   #This sends a simple text response back to the browser or user. So when someone opens your API URL, they see: "ML API is running 🚀"

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
