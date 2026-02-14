import pandas as pd
from geopy.distance import geodesic


#Load team locations
locations = pd.read_csv("data/raw/team_locations.csv")

#function to get coordinates of a team
def  get_team_coords(team_code):
    row = locations[locations["team"] == team_code]

    lat = row["lat"].values[0]
    lon = row["lon"].values[0]

    return (lat, lon)


#example: kansas city chiefs vc san francisco 49ers
team_a = "KC"
team_b = "SF"

coords_a = get_team_coords(team_a)
coords_b = get_team_coords(team_b)

distance_miles = geodesic(coords_a, coords_b).miles
print(f"Distance between {team_a} and {team_b}: {distance_miles:.2f} miles")