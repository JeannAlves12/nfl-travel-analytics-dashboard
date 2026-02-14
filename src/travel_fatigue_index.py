import pandas as pd


# Load dataset
df = pd.read_csv("data/processed/game_travel_distances.csv")

print("Dataset loaded!")

# Function: rolling fatigue
fatigue_results = []

teams = df["away_team"].unique()

for team in teams:

    team_games = df[df["away_team"] == team].copy()

    # Sort by week
    team_games = team_games.sort_values("week")

    # Rolling sum of 3 consecutive away trips
    team_games["rolling_3_game_miles"] = (
        team_games["distance_miles"]
        .rolling(window=3)
        .sum()
    )

    # Get worst stretch
    max_row = team_games.loc[
        team_games["rolling_3_game_miles"].idxmax()
    ]

    fatigue_results.append({
        "team": team,
        "worst_3_game_stretch_miles": round(max_row["rolling_3_game_miles"], 2),
        "week_end": int(max_row["week"])
    })

# Ranking
fatigue_df = pd.DataFrame(fatigue_results)

fatigue_df = fatigue_df.sort_values(
    "worst_3_game_stretch_miles",
    ascending=False
)

print("\n🔥 Travel Fatigue Index (Worst 3 Away Trips in a Row):\n")
print(fatigue_df.head(10))

# Save output
output_path = "data/processed/travel_fatigue_index.csv"
fatigue_df.to_csv(output_path, index=False)

print(f"\n✅ Saved to: {output_path}")
