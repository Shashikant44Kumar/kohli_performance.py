import pandas as pd
df = pd.read_csv("Virat_Kohli.csv")

print(df.head(10))

# print(df.tail(10))

# df.info() 
# print(df.shape)

# print(df.describe())  
# print(df["Opposition"].describe())  

run_frequency = df["Opposition"].value_counts()
print(run_frequency)

new_df = df[["Runs", "SR", "Opposition"]]
print(new_df)

print(df["Opposition"] == "v Australia")
vs_aussies = df[df["Opposition"] == "v Australia"]
print(vs_aussies)

# find all the matches where virat kohli scored century

tons = df[df["Runs"] >= 100]
print(tons)


#  find all the matches where Virat's Strike Rate was > 100

ton_sr = df[df["SR"] > 100]
print(ton_sr)

# Find all the matches where Virat played with Srilanka and Scored a Century

sril_cent = df[
    (df["Opposition"] == "v Sri lanka") & (df["Runs"] >= 100)
]

print(sril_cent)

def find_centuries(x):
    if x>=100:
        return "OG"
    else:
        return "NOOB"

df["Centuries"] = df["Runs"].apply(find_centuries)
print(df.tail(10))
