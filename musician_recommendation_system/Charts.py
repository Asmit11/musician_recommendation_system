import pandas as pd
import matplotlib.pyplot as plt

#  Check if dataset exists
try:
    musicians_df = pd.read_csv("datasets/musicians_data.csv") 
except FileNotFoundError:
    print(" Error: 'musicians_data.csv' not found. Ensure the file exists in the 'datasets/' folder.")
    exit()

# Ensure 'genre_preferences' column exists
if "genre_preferences" in musicians_df.columns:
    # Convert string representation of lists to actual lists
    musicians_df["genre_preferences"] = musicians_df["genre_preferences"].apply(lambda x: eval(x) if isinstance(x, str) else x)
    
    # 🔹 Get the Top 10 Music Genres
    genre_counts = musicians_df.explode("genre_preferences")["genre_preferences"].value_counts().head(10)
    
    # 🎵 Plot the Top 10 Genres
    plt.figure(figsize=(10, 5))
    genre_counts.plot(kind="bar", color="skyblue", title="Top 10 Most Popular Music Genres")
    plt.xlabel("Genre")
    plt.ylabel("Number of Musicians")
    plt.xticks(rotation=45)
    plt.show()
else:
    print(" Error: Column 'genre_preferences' not found in the dataset.")
