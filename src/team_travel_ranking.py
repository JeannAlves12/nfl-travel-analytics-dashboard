import pandas as pd

#Load travel distances dataset
df = pd.read_csv("data/processed/game_travel_distances.csv")

print("Dataset loaded")
print(df.head())

#Total travel per team(away)
team_totals = (
    df.groupby("away_team")["distance_miles"]
    .sum()
    .sort_values(ascending=False)
    .reset_index()
)

team_totals.columns = ["team", "total_miles"]

print("\nTravel Ranking (Most Miles Traveled):\n")
print(team_totals)

#Save Ranking
output_path = "data/processed/team_travel_ranking.csv"
team_totals.to_csv(output_path, index=False)

print(f"\nRanking saved to: {output_path}")
