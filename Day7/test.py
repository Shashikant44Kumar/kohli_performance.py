import pandas as pd

data = {
    "apples": [4, 3, 6,1],
    "oranges": [3, 7, 4, 1]
}

indes_titles = [
    "Aaron", "Shaun", "James", "Wilson"
]
df = pd.DataFrame(data,index=indes_titles)

print(df)
# print(df.loc["Aaron"]["apples"])
print(df["oranges"].iloc[1:])
print(type(df))