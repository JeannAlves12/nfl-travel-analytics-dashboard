# 🏈 NFL Travel Optimization & Analytics Dashboard (2023)

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Pandas](https://img.shields.io/badge/Data-Pandas-success)
![Streamlit](https://img.shields.io/badge/Dashboard-Streamlit-red)
![NFL Analytics](https://img.shields.io/badge/Project-NFL%20Operations-black)

An end-to-end **NFL travel analytics** project focused on team logistics, fatigue, and performance impact during the 2023 season.

This project simulates the type of work done by **NFL front offices** in:

- Team Operations  
- Travel & Scheduling Logistics  
- Sports Data Analytics  

---

## 🚀 Project Motivation

NFL teams travel thousands of miles every season.  
Travel impacts:

- player recovery  
- fatigue and jet lag  
- logistics planning  
- away-game performance  

This project answers key questions such as:

- Which NFL teams traveled the most in 2023?
- What were the longest road trips?
- Which teams faced the toughest travel fatigue stretches?
- Does long-distance travel reduce away win probability?

---

## 📊 Key Analyses

### 🏆 Team Travel Ranking
Ranks all 32 teams by total miles traveled as the away team.

### ✈️ Longest Trips of the Season
Identifies the top 10 longest road travel games.

Example (2023):
- Chargers → Patriots (~2587 miles)

### 🔥 Travel Fatigue Index
Measures the worst **3-game consecutive away travel stretch** for each team.

### 📉 Travel Distance vs Performance
Analyzes away-team win rate grouped by travel distance buckets.

---

## 📌 Sample Insights (2023 Season)

- The Chargers ranked #1 in travel fatigue due to repeated long-distance away stretches.
- Coast-to-coast matchups produced the longest travel demands.
- Away win rates decrease as travel distance increases, suggesting measurable fatigue effects.

---

## 🖥️ Interactive Streamlit Dashboard

This project includes a full interactive dashboard with:

- Team Travel Ranking  
- Fatigue Index  
- Longest Trips  
- Win Rate vs Distance  

Run locally:

streamlit run dashboard/app.py

Dashboard opens at:

http://localhost:8501

---

## 📷 Dashboard Preview

Add a screenshot here after running Streamlit:

![Dashboard Preview](assets/dashboard_preview.png)

(You can create an `assets/` folder and save an image named `dashboard_preview.png`)

---

## ⚙️ Installation

Install dependencies:

pip install -r requirements.txt

Or manually:

pip install pandas matplotlib streamlit nfl_data_py geopy

---

## 📌 Data Sources

- NFL official schedule data via `nfl_data_py`
- Franchise home city coordinates dataset (team locations)

---

## 🔮 Future Improvements

- Add playoff travel analysis  
- Include rest days + time zones  
- Predict performance impact using Machine Learning  
- Build an optimized schedule model to reduce fatigue  
- Expand into equipment + travel cost optimization  

---

## 👤 Author

**Jeann Garconi Alves**  
Computer Science Student | Data Analytics & Sports Logistics  

Dream: Work in the NFL in Data Science or Team Operations.

---

## ⭐ If you found this project interesting

Feel free to connect with me on LinkedIn and check out the full dashboard.
