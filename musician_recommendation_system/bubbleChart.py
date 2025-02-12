import pandas as pd
import matplotlib.pyplot as plt

# ✅ Load dataset with error handling
try:
    musicians_df = pd.read_csv("datasets/musicians_data.csv")  # Update path if needed
except FileNotFoundError:
    print("Error: 'musicians_data.csv' not found. Ensure the file exists in the 'datasets/' folder.")
    exit()

# ✅ Ensure required columns exist
if {"genre_preferences", "years_of_experience", "skill_level"}.issubset(musicians_df.columns):
    # Convert string representation of lists to actual lists if needed
    musicians_df["genre_preferences"] = musicians_df["genre_preferences"].apply(lambda x: eval(x) if isinstance(x, str) else x)
    
    # Explode dataset to count individual genres
    genre_expanded = musicians_df.explode("genre_preferences")

    # Map skill level to numeric values for bubble size
    skill_mapping = {"Beginner": 1, "Intermediate": 2, "Advanced": 3, "Professional": 4}
    genre_expanded["skill_numeric"] = genre_expanded["skill_level"].map(skill_mapping)

    # Aggregate by genre to get avg experience and musician count
    genre_summary = genre_expanded.groupby("genre_preferences").agg(
        avg_experience=("years_of_experience", "mean"),
        musician_count=("genre_preferences", "count"),
        avg_skill=("skill_numeric", "mean")
    ).reset_index()

    # 🎵 Bubble Chart: Genre Popularity vs. Experience Level
    plt.figure(figsize=(10, 6))
    plt.scatter(
        genre_summary["avg_experience"],
        genre_summary["musician_count"],
        s=genre_summary["avg_skill"] * 100,  # Bubble size based on skill level
        alpha=0.6,
        color="blue",
        edgecolors="black"
    )
    
    # Label each genre on the chart
    for i, row in genre_summary.iterrows():
        plt.text(row["avg_experience"], row["musician_count"], row["genre_preferences"], fontsize=9)

    # Chart Labels and Title
    plt.xlabel("Average Years of Experience")
    plt.ylabel("Number of Musicians")
    plt.title("Bubble Chart: Musician Popularity by Genre & Experience")
    plt.grid(True)
    plt.show()
else:
    print("Error: Required columns not found in the dataset.")
