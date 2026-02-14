import pandas as pd


# Load game travel distances

df = pd.read_csv("data/processed/game_travel_distances.csv")

print("Dataset loaded!")
print(f"Total games: {len(df)}")

# Sort by longest distance

longest = df.sort_values("distance_miles", ascending=False)

print("\n✈️ Top 10 Longest Trips of the 2023 NFL Season:\n")
print(longest.head(10))

# Save report

output_path = "data/processed/longest_trips.csv"
longest.head(10).to_csv(output_path, index=False)

print(f"\n✅ Saved Top 10 longest trips to: {output_path}")
