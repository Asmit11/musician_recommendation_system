import pandas as pd
from surprise import Dataset, Reader, SVD
from surprise.model_selection import train_test_split, cross_validate

# Load dataset
musicians_df = pd.read_csv("datasets/musicians_data.csv")
collaborations_df = pd.read_csv("datasets/collaborations_data.csv")

# Convert ratings to proper format
reader = Reader(rating_scale=(1, 5))
data = Dataset.load_from_df(collaborations_df[["musician_id_a", "musician_id_b", "collaboration_rating"]], reader)

# Split dataset into training and test sets
trainset, testset = train_test_split(data, test_size=0.2)

# Train Collaborative Filtering Model
model = SVD()
model.fit(trainset)

# Test Model Performance
predictions = model.test(testset)

# Show sample prediction
print(predictions[:5])

# Save trained model for later use
import pickle
with open("models/collaborative_model.pkl", "wb") as f:
    pickle.dump(model, f)

print(" Model trained and saved successfully!")
