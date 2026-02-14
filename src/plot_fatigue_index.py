import pandas as pd
import matplotlib.pyplot as plt


# Load fatigue index dataset

df = pd.read_csv("data/processed/travel_fatigue_index.csv")

# Select Top 10
top10 = df.head(10)

print("Top 10 fatigue teams:\n")
print(top10)


# Plot
plt.figure(figsize=(10,6))

plt.bar(top10["team"], top10["worst_3_game_stretch_miles"])

plt.title("NFL Travel Fatigue Index (Worst 3 Away Trips in a Row)")
plt.xlabel("Team")
plt.ylabel("Miles Traveled (3-game stretch)")

plt.show()
