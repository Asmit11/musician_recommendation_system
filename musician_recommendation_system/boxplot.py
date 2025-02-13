import pandas as pd
import matplotlib.pyplot as plt


musicians_df = pd.read_csv("datasets/musicians_data.csv") 


# Generate Box Plot: Skill Level vs. Years of Experience
plt.figure(figsize=(8, 6))
musicians_df.boxplot(column="years_of_experience", by="skill_level", grid=False, patch_artist=True)
plt.title("Skill Level vs. Years of Experience")
plt.xlabel("Skill Level")
plt.ylabel("Years of Experience")
plt.show()

