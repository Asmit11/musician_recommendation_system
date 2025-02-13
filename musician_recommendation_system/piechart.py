import pandas as pd
import matplotlib.pyplot as plt

# Load dataset with error handling
try:
    musicians_df = pd.read_csv("datasets/musicians_data.csv")  
except FileNotFoundError:
    print("Error: 'musicians_data.csv' not found. Ensure the file exists in the correct folder.")
    exit()

# Ensure required column exists for the pie chart
if "primary_role" in musicians_df.columns:
    # Count occurrences of each musician role
    role_counts = musicians_df["primary_role"].value_counts()

    # 🎵 Pie Chart: Distribution of Musician Roles
    plt.figure(figsize=(8, 8))
    plt.pie(role_counts, labels=role_counts.index, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
    plt.title("Distribution of Musician Roles")
    plt.show()
else:
    print("Error: Column 'primary_role' not found in the dataset.")
