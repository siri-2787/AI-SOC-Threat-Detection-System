import joblib
from sklearn.ensemble import RandomForestClassifier

print("🔥 TRAIN MODEL FILE LOADED")

def train_model(X, y):
    print("🧠 Training started...")

    model = RandomForestClassifier(n_estimators=100)
    model.fit(X, y)

    joblib.dump(model, "models/model.pkl")

    print("✅ Model saved successfully")

    return model