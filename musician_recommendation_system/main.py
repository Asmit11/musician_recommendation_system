import pandas as pd

musicians_df = pd.read_csv("musicians_data.csv")
collaborations_df = pd.read_csv("collaborations_data.csv")

print(musicians_df.info())
print(collaborations_df.info())

# Fill missing values if necessary
musicians_df.fillna("", inplace=True)
collaborations_df.fillna(0, inplace=True)

