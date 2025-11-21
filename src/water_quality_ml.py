import sqlite3
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import joblib

# --------------------------
# 1. TRAINING DATA
# --------------------------
training_data = np.array([
    [6.5, 2.1, 310, 24, 1],
    [7.0, 1.5, 280, 22, 1],
    [8.2, 4.5, 500, 29, 0],
    [5.5, 6.8, 650, 31, 0],
    [7.4, 2.8, 300, 25, 1],
    [6.1, 5.0, 590, 30, 0]
])

X = training_data[:, :4]
y = training_data[:, 4]

# --------------------------
# 2. TRAIN RANDOM FOREST
# --------------------------
print("Training Random Forest...")
model = RandomForestClassifier(n_estimators=60)
model.fit(X, y)
print("Model trained.")

# Save ML model
joblib.dump(model, "water_model.pkl")

# --------------------------
# 3. USER INPUT
# --------------------------
pH = 7.1
turbidity = 4.5
conductivity = 345
temperature = 26.5

sample = np.array([[pH, turbidity, conductivity, temperature]])

# --------------------------
# 4. PREDICTION
# --------------------------
pred = model.predict(sample)[0]
prob = model.predict_proba(sample)[0][1]

status = "Good Water" if pred == 1 else "Bad / Contaminated"

print(f"\nPrediction → {status} (p = {prob:.3f})")

# --------------------------
# 5. STORE IN SQLITE
# --------------------------
conn = sqlite3.connect("water_quality.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS results(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    pH REAL,
    turbidity REAL,
    conductivity REAL,
    temperature REAL,
    prediction INTEGER,
    probability REAL
)
""")

cur.execute("""
INSERT INTO results(pH, turbidity, conductivity, temperature, prediction, probability)
VALUES (?, ?, ?, ?, ?, ?)
""", (pH, turbidity, conductivity, temperature, pred, prob))

conn.commit()
conn.close()
print("✔ Saved to SQLite DB successfully.")
