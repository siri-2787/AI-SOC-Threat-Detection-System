import sys
import os
import datetime
import joblib
import numpy as np
from flask import Flask, request, jsonify

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.alert import generate_alert
from src.logger import log_event

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model = joblib.load(os.path.join(BASE_DIR, "..", "models", "model.pkl"))
scaler = joblib.load(os.path.join(BASE_DIR, "..", "models", "scaler.pkl"))


# ---------------- THREAT SCORE ----------------
def compute_score(is_attack, data):
    if not is_attack:
        return np.random.randint(5, 40)

    score = 50

    if float(data.get("serror_rate", 0)) > 0.5:
        score += 25

    if float(data.get("count", 0)) > 200:
        score += 15

    if float(data.get("src_bytes", 0)) > 20000:
        score += 10

    return min(score, 100)


# ---------------- SAFE GET ----------------
def safe_float(val, default=0):
    try:
        return float(val)
    except:
        return default


# ---------------- PREDICT ----------------
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        # SAFE FEATURE EXTRACTION
        raw_features = np.array([[ 
            safe_float(data.get("duration")),
            safe_float(data.get("protocol_type"), 1),
            safe_float(data.get("service"), 1),
            safe_float(data.get("src_bytes")),
            safe_float(data.get("dst_bytes")),
            safe_float(data.get("count")),
            safe_float(data.get("srv_count")),
            safe_float(data.get("serror_rate")),
            safe_float(data.get("srv_serror_rate")),
            safe_float(data.get("same_srv_rate"), 1)
        ]])

        # SCALE
        scaled = scaler.transform(raw_features)

        # PREDICT
        pred = model.predict(scaled)[0]
        is_attack = int(pred) == 1

        # DEFAULT RESPONSE
        severity = "LOW"
        attack_type = "Normal"
        reason = "Normal network behavior"

        if is_attack:
            if safe_float(data.get("serror_rate")) > 0.5:
                attack_type = "DoS Attack"
                severity = "HIGH"
                reason = "High error rate → possible DoS"
            elif safe_float(data.get("count")) > 200:
                attack_type = "Port Scan"
                severity = "MEDIUM"
                reason = "High connection count → scanning"
            else:
                attack_type = "Anomaly"
                severity = "MEDIUM"
                reason = "Unusual pattern detected"

        score = compute_score(is_attack, data)

        response = {
            "result": "ATTACK" if is_attack else "NORMAL",
            "attack_type": attack_type,
            "severity": severity,
            "reason": reason,
            "score": score,
            "timestamp": datetime.datetime.now().strftime("%H:%M:%S"),
            "alert": generate_alert(int(pred))
        }

        log_event(data, response["result"])

        return jsonify(response)

    except Exception as e:
        return jsonify({
            "result": "ERROR",
            "attack_type": "UNKNOWN",
            "severity": "UNKNOWN",
            "score": 0,
            "error": str(e)
        })


if __name__ == "__main__":
    print("🚀 API running at http://127.0.0.1:5000")
    app.run(debug=True, port=5000)