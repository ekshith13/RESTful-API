from flask import Flask, request, jsonify
import pandas as pd
import joblib
from model import train_model, make_prediction

app = Flask(__name__)

# Store uploaded data and trained model globally
uploaded_data = None
trained_model = None

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Manufacturing Prediction API"})

# Endpoint to upload data
@app.route('/upload', methods=['POST'])
def upload_data():
    global uploaded_data
    if 'file' not in request.files:
        return jsonify({"error": "No file provided"}), 400

    file = request.files['file']
    try:
        uploaded_data = pd.read_csv(file)
        return jsonify({"message": "File uploaded successfully", "columns": list(uploaded_data.columns)})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Endpoint to train the model
@app.route('/train', methods=['POST'])
def train():
    global trained_model
    if uploaded_data is None:
        return jsonify({"error": "No data uploaded"}), 400

    try:
        trained_model, metrics = train_model(uploaded_data)
        return jsonify({"message": "Model trained successfully", "metrics": metrics})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Endpoint to make predictions
@app.route('/predict', methods=['POST'])
def predict():
    global trained_model
    if trained_model is None:
        return jsonify({"error": "Model not trained"}), 400

    try:
        input_data = request.get_json()
        prediction = make_prediction(trained_model, input_data)
        return jsonify(prediction)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
