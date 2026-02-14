import streamlit as st
import pandas as pd

# Page Config
st.set_page_config(
    page_title="NFL Travel Analytics Dashboard",
    layout="wide"
)

st.title("🏈 NFL Travel Analytics Dashboard (2023)")
st.write("An analytics project focused on team travel distance, fatigue, and performance.")

# Load Data
ranking = pd.read_csv("data/processed/team_travel_ranking.csv")
fatigue = pd.read_csv("data/processed/travel_fatigue_index.csv")
longest = pd.read_csv("data/processed/longest_trips.csv")
performance = pd.read_csv("data/processed/travel_vs_performance.csv")

# Sidebar
st.sidebar.header("Dashboard Sections")
section = st.sidebar.radio(
    "Choose Analysis:",
    [
        "🏆 Team Travel Ranking",
        "🔥 Travel Fatigue Index",
        "✈️ Longest Trips",
        "📉 Travel vs Performance"
    ]
)

# Section 1: Ranking
if section == "🏆 Team Travel Ranking":
    st.subheader("🏆 Teams That Traveled the Most")

    st.dataframe(ranking.head(15))

    st.bar_chart(
        ranking.set_index("team").head(10)["total_miles"]
    )

# Section 2: Fatigue Index
elif section == "🔥 Travel Fatigue Index":
    st.subheader("🔥 Worst 3-Game Away Stretch (Fatigue Index)")

    st.dataframe(fatigue.head(15))

    st.bar_chart(
        fatigue.set_index("team").head(10)["worst_3_game_stretch_miles"]
    )

# Section 3: Longest Trips
elif section == "✈️ Longest Trips":
    st.subheader("✈️ Top 10 Longest Away Trips of 2023")

    st.dataframe(longest)

# Section 4: Performance
elif section == "📉 Travel vs Performance":
    st.subheader("📉 Away Win Rate vs Travel Distance")

    st.dataframe(performance)

    st.bar_chart(
        performance.set_index("distance_bucket")["away_win_rate"]
    )

st.success("Dashboard loaded successfully!")
