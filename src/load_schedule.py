import nfl_data_py as nfl
import pandas as pd


# STEP 1: Load NFL Schedule

def load_schedule(season):
    """
    Loads the Nfl schedule for a given season.
    Example: 2023
    """
    schedule = nfl.import_schedules([season])
    return schedule


if __name__ == "__main__":
    # Load the schedule for the 2023 season
    season = 2023
    print(f"Loading NFL schedule for the {season} season...")

    schedule = load_schedule(season)
    print("\nFirst 5 rows:")
    print(schedule.head())

    print("\nColumns in the schedule:")
    print(schedule.columns)

    output_path = "data/raw/schedule.csv"
    schedule.to_csv(output_path, index=False)

    print(f"\nSchedule saved to {output_path}")
