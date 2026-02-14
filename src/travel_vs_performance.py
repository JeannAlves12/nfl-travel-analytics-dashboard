import pandas as pd
import matplotlib.pyplot as plt


# Load datasets
travel_df = pd.read_csv("data/processed/game_travel_distances.csv")
schedule_df = pd.read_csv("data/raw/schedule.csv")

print("Datasets loaded!")

# Merge travel + game results
merged = pd.merge(
    travel_df,
    schedule_df,
    on=["week", "away_team", "home_team"],
    how="inner"
)

print("\nMerged dataset sample:")
print(merged.head())

# Determine if away team won
merged["away_win"] = merged["away_score"] > merged["home_score"]

# Convert boolean to int
merged["away_win"] = merged["away_win"].astype(int)

# Create distance buckets
merged["distance_bucket"] = pd.cut(
    merged["distance_miles"],
    bins=[0, 500, 1000, 1500, 2000, 3000],
    labels=[
        "0-500 miles",
        "500-1000 miles",
        "1000-1500 miles",
        "1500-2000 miles",
        "2000-3000 miles"
    ]
)

# Win rate per bucket
bucket_stats = merged.groupby("distance_bucket")["away_win"].mean().reset_index()

bucket_stats["away_win_rate"] = bucket_stats["away_win"] * 100

print("\n🏆 Away Team Win Rate by Travel Distance:\n")
print(bucket_stats)

# Plot win rate
plt.figure(figsize=(10,6))

plt.bar(bucket_stats["distance_bucket"], bucket_stats["away_win_rate"])

plt.title("Away Team Win Rate vs Travel Distance (NFL 2023)")
plt.xlabel("Travel Distance Bucket")
plt.ylabel("Away Win Rate (%)")

plt.show()

# Save output
output_path = "data/processed/travel_vs_performance.csv"
bucket_stats.to_csv(output_path, index=False)

print(f"\n✅ Saved results to: {output_path}")
