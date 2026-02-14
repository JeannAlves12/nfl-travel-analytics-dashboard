import pandas as pd
import matplotlib.pyplot as plt

# Load ranking dataset
df = pd.read_csv("data/processed/team_travel_ranking.csv")

#Select top 10 teams
top10 = df.head(10)
print("Top 10 teams loaded:\n")
print(top10)

#Plot
plt.figure(figsize=(10,6))

plt.bar(top10["team"], top10["total_miles"])

plt.title("Top 10 NFL Teams That Traveled the Most (2023 Season)")
plt.xlabel("Team")
plt.ylabel("Total Miles Traveled")

plt.show()
