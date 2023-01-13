import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("Virat_Kohli.csv")
print(df.head())

# Total no. of runs Kohli has Scored
print("Total runs: ", df["Runs"].sum())

# Find out the Total no balls he has faced

print("Total Balls: ", df["BF"].sum())
# Find out the average strike rate of kohli

print("average strikerate: ", df["SR"].mean())

# Number of matches he has played at different positions
print(df["Pos"].head(10))
positions = df["Pos"].unique()
print(positions)

df["Pos"] = df["Pos"].map({
    3.0: "Batting at 3",
    4.0: "Batting at 4",
    2.0: "Batting at 2",
    1.0: "Batting at 1",
    7.0: "Batting at 7",
    5.0: "Batting at 5",
    6.0: "Batting at 6"
})
# print(df[["Runs", "Pos"]])
print(df.head(10))
pos_counts = df["Pos"].value_counts()
print(pos_counts)
print(type(pos_counts))

# Total runs scored in different positions
pos_counts_values = pos_counts.values
pos_counts_labels = pos_counts.index

fig = plt.figure(figsize=(10, 7))
plt.pie(pos_counts_values, labels=pos_counts_labels)
plt.show()

# Function to create 
def show_pie_plots(df, key):
    counts = df[key].value_counts()
    print(counts)
    count_values = counts.values
    count_labels = counts.index
    fig = plt.figure(figsize=(10, 7))
    plt.pie(count_values, labels=count_labels)
    plt.show()


# Number of matcheshe has played in different positions/opposition
show_pie_plots(df, "Opposition")

# Number of matches  he has played at grounds 
show_pie_plots(df, "Ground")


# Total sixes scored in different positions
runs_at_pos = df.groupby("Pos")["6s"].sum()
print(runs_at_pos, type(runs_at_pos))
runs_at_pos_values = runs_at_pos.values
runs_at_pos_labels = runs_at_pos.index

fig = plt.figure(figsize=(10, 7))
plt.bar(
    runs_at_pos_labels,
    runs_at_pos_values,
    color="green",
    width=0.3
)
plt.show()

# Total runs scored with different countries

runs_with_countries = df.groupby("Opposition")["Runs"].sum()
runs_with_countries_values = runs_with_countries.values
runs_with_countries_labels = runs_with_countries.index

fig = plt.figure(figsize=(10, 7))
plt.bar(
    runs_with_countries_labels,
    runs_with_countries_values,
    color="red",
    width=0.3
)
plt.show()




# Number of centuries scored by him in 1st and 2nd innings
centuries = df.query("Runs >= 100")
print(centuries)

innings = centuries["Inns"].value_counts()
print(innings)

plt.pie(innings.values, labels=innings.index)
plt.show()

# Calculate of the dismissals of kohli


# Against which teams he has scored most runs 

# Analyze the strike rate

# Kohli strike rate's in First innings vs Second Innings


