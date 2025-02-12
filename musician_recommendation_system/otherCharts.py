import pandas as pd
import matplotlib.pyplot as plt

# ✅ Load dataset with error handling
try:
    musicians_df = pd.read_csv("datasets/musicians_data.csv")  # Update path if needed
except FileNotFoundError:
    print("Error: 'musicians_data.csv' not found. Ensure the file exists in the correct folder.")
    exit()


if {"years_of_experience", "primary_role", "skill_level"}.issubset(musicians_df.columns):
    
    
    experience_by_role = musicians_df.groupby("primary_role")["years_of_experience"].mean().sort_values()
    plt.figure(figsize=(10, 5))
    experience_by_role.plot(kind="bar", color="lightcoral", title="Average Years of Experience by Role")
    plt.xlabel("Role")
    plt.ylabel("Average Years of Experience")
    plt.xticks(rotation=45)
    plt.show()

    
    plt.figure(figsize=(8, 5))
    plt.hist(musicians_df["years_of_experience"], bins=10, color="teal", alpha=0.7, edgecolor="black")
    plt.title("Distribution of Years of Experience Among Musicians")
    plt.xlabel("Years of Experience")
    plt.ylabel("Number of Musicians")
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.show()


else:
    print("Error: Required columns not found in the dataset.")
