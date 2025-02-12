import streamlit as st
import pandas as pd
import pickle
import random

# Load dataset
musicians_df = pd.read_csv("datasets/musicians_data.csv")

# Load trained model
with open("models/collaborative_model.pkl", "rb") as f:
    model = pickle.load(f)

# Streamlit UI Header
st.title(" Musician Recommendation System")

# Select a musician from dropdown
musician = st.selectbox("Select a Musician:", musicians_df["name"].unique())

# Display musician details
selected_musician_df = musicians_df[musicians_df["name"] == musician]
st.write(selected_musician_df)

# Recommendation button
if st.button("Get Recommendations"):
    st.write("Generating recommendations...")

    # Pick a random musician as the "target" for prediction (improving this later)
    random_musician_id = random.choice(musicians_df["user_id"].values)

    # Make prediction (User = selected musician, Item = random musician)
    predicted_collab = model.predict(uid=selected_musician_df.iloc[0]["user_id"], iid=random_musician_id)

    # Get recommended musician details
    recommended_musician = musicians_df[musicians_df["user_id"] == predicted_collab.iid]

    # Display recommendation result
    st.write(" **Recommended Musician:**")
    st.write(recommended_musician)

    # Show predicted collaboration rating
    st.write(f"**Predicted Collaboration Rating:** {predicted_collab.est:.2f}")
    
    
