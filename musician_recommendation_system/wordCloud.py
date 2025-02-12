import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Load datasets
musicians_df = pd.read_csv("datasets/musicians_data.csv")
collaborations_df = pd.read_csv("datasets/collaborations_data.csv")

# Extract relevant text data for the word cloud
genre_text = " ".join(musicians_df["genre_preferences"].astype(str))
instruments_text = " ".join(musicians_df["instruments"].astype(str))
collab_text = " ".join(collaborations_df["project_genre"].astype(str))

# Combine all text data
combined_text = genre_text + " " + instruments_text + " " + collab_text

# Generate the word cloud
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(combined_text)

# Plot the word cloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.title("Word Cloud for Musician Dataset")
plt.show()
