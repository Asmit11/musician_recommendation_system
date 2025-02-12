from flask import Flask, jsonify
import pickle

# Load trained model
with open("../models/collaborative_model.pkl", "rb") as f:
    model = pickle.load(f)

app = Flask(__name__)

@app.route("/recommend/<musician_id>")
def recommend(musician_id):
    predicted_collab = model.predict(musician_id, "MUS1234")  # Predict a sample
    return jsonify({"musician_id": musician_id, "recommended_musician": "MUS1234", "predicted_rating": predicted_collab.est})

if __name__ == "__main__":
    app.run(debug=True)
