import pandas as pd
from geopy.distance import geodesic


# Load datasets

schedule = pd.read_csv("data/raw/schedule.csv")
locations = pd.read_csv("data/raw/team_locations.csv")

#Helper function
def get_team_coords(team_code):
    row = locations[locations["team"] == team_code]

    if row.empty:
        return None

    lat = row["lat"].values[0]
    lon = row["lon"].values[0]

    return (lat, lon)

#Calculate travel distance

travel_distances = []

for i, game in schedule.iterrows():
    away_team = game["away_team"]
    home_team = game["home_team"]

    away_coords = get_team_coords(away_team)
    home_coords = get_team_coords(home_team)

    if away_coords is None or home_coords is None:
        continue

    distance = geodesic(away_coords, home_coords).miles

    travel_distances.append({
        "week": game["week"],
        "away_team": away_team,
        "home_team": home_team,
        "distance_miles": distance
    })

#convert to dataframe
travel_df = pd.DataFrame(travel_distances)

print("Travel distances calculated!")
print(travel_df.head())

#Save the processed file
travel_df.to_csv("data/processed/game_travel_distances.csv", index=False)

print("\nSaved to: data/processed/game_travel_distances.csv")
