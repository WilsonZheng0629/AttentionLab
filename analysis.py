from turtle import st

import pandas as pd

df = pd.read_csv("data/Dummy Data.csv")

print(df.describe())

print(
    df.groupby("Category")["Views"].mean().sort_values(ascending = True)
)