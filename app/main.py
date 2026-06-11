from flask import Flask, jsonify
import joblib
import json
import os

app = Flask(__name__)

MODEL_PATH = os.path.join("models", "model.joblib")
METRICS_PATH = os.path.join("models", "metrics.json")

# Carrega o modelo treinado
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError("O arquivo 'model.joblib' não foi encontrado na pasta 'models/'.")
model = joblib.load(MODEL_PATH)

# Carrega as métricas (opcional)
if os.path.exists(METRICS_PATH):
    with open(METRICS_PATH, "r") as f:
        metrics = json.load(f)
else:
    metrics = {}

@app.route('/', methods=['GET'])
def hello_world():
    return jsonify({"message": "Hello World, Flask API is running!"})

@app.route('/health-check', methods=['GET'])
def health():
    return jsonify({"message": "OK"})

@app.route('/predict', methods=['GET'])
def predict():
    return jsonify({"message": "OK"})

if __name__ == '__main__':
    app.run(debug=True)
