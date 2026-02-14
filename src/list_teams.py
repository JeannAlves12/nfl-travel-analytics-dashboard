import pandas as pd

#Load schedule CSV
schedule = pd.read_csv("data/raw/schedule.csv")
#Get all unique teams(home + away)
teams = pd.concat([
    schedule['home_team'], 
    schedule['away_team']
    ]).unique()

teams = sorted(teams)

print("NFL teams found in schedule:\n")

for team in teams:
    print(team)

print(f"\nTotal number of teams: {len(teams)}")
