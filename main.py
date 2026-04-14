from src.preprocessing import load_data, preprocess_data
from src.train_model import train_model
import joblib
from src.anomaly import train_anomaly_model, detect_anomaly

print("🚀 MAIN STARTED")

# Load dataset
data = load_data("data/dataset.csv")
print("📊 Dataset loaded")

# Preprocess
X, y, scaler = preprocess_data(data)
print("⚙️ Preprocessing done")

# Train model
model = train_model(X, y)
print("🤖 ML model trained")

# Save scaler
joblib.dump(scaler, "models/scaler.pkl")
print("💾 Scaler saved")

# Train anomaly model
anomaly_model = train_anomaly_model(X)
print("🧪 Anomaly model trained")

# Detect anomalies
results = detect_anomaly(anomaly_model, X[:10])
print("🚨 Detection results:")
print(results)

print("🎯 PIPELINE COMPLETE")