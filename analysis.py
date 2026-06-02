import pandas as pd

df = pd.read_csv("data/Dummy Data.csv")

print(
    df.groupby("Hook_Type")["Views"].mean().sort_values(ascending = True)
)