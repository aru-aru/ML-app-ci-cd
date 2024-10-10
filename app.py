# app.py
from flask import Flask, request, jsonify
import joblib
import numpy as np

# Load the trained model
model = joblib.load('model.pkl')

app = Flask(__name__)

@app.route('/')
def home():
    return "ML Model Prediction App"

@app.route('/predict', methods=['POST'])
def predict():
    # Expecting JSON input with features
    data = request.get_json()
    features = np.array([data['features']])
    
    # Make a prediction
    prediction = model.predict(features)
    
    # Return the prediction as JSON
    return jsonify({'prediction': int(prediction[0])})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
