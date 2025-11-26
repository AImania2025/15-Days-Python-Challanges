import streamlit as st
from datetime import datetime, timedelta
import pandas as pd

# ---------------------------
# Mock data
def fetch_workout_data():
    return [
        {"date": "2025-09-01", "type": "Run", "duration_min": 45, "calories": 400},
        {"date": "2025-09-08", "type": "Yoga", "duration_min": 30, "calories": 150},
        {"date": "2025-09-15", "type": "Strength Training", "duration_min": 60, "calories": 500},
        {"date": "2025-10-05", "type": "Cycling", "duration_min": 90, "calories": 700},
    ]

def check_missed_workouts(latest_date):
    today = datetime.now().date()
    if latest_date < today:
        return True
    return False
# ---------------------------

# Initialize session state
if 'workouts' not in st.session_state:
    initial_data = fetch_workout_data()
    st.session_state.workouts = pd.DataFrame(initial_data)
    st.session_state.workouts['date'] = pd.to_datetime(st.session_state.workouts['date'])

# Page setup
st.set_page_config(page_title="Gym Logger", layout="wide", page_icon="🏋️‍♂️")

# Sidebar navigation
st.sidebar.title("Gym Tracker Menu")
menu = st.sidebar.radio("Select Page", ["Dashboard", "Log Workout", "Analysis", "Settings"])

df = st.session_state.workouts

# ---------------------------
# Dashboard
if menu == "Dashboard":
    st.title("🏋️‍♀️ Gym Workout Dashboard")

    today = datetime.now().date()
    today_workouts = df[df['date'].dt.date == today]

    if not today_workouts.empty:
        total_time = today_workouts['duration_min'].sum()
        total_cal = today_workouts['calories'].sum()
        st.success(f"You have worked out for **{total_time} minutes** today and burnt **{total_cal} calories**! 🎉")
    else:
        st.warning("You haven't logged any workout today. Don't forget to exercise! 💪")

    latest_date = df['date'].max().date()
    if check_missed_workouts(latest_date):
        st.error("You missed a workout! Stay consistent. 📅")

    st.subheader("Today's Workouts")
    st.dataframe(today_workouts)

    st.subheader("All Workouts")
    st.dataframe(df.sort_values(by='date', ascending=False))

# ---------------------------
# Log Workout
elif menu == "Log Workout":
    st.title("📝 Log Today's Workout")

    with st.form("workout_form"):
        date = st.date_input("Date", datetime.now())
        workout_type = st.selectbox("Workout Type", ["Run", "Walk", "Yoga", "Stretching", "Strength Training", "Cycling", "Other"])
        duration = st.number_input("Duration (in minutes)", min_value=1, max_value=300, value=30)
        calories = st.number_input("Calories Burnt", min_value=1, max_value=3000, value=200)
        submit = st.form_submit_button("Save Workout")

        if submit:
            new_entry = pd.DataFrame([{
                "date": date.strftime("%Y-%m-%d"),
                "type": workout_type,
                "duration_min": duration,
                "calories": calories
            }])
            new_entry['date'] = pd.to_datetime(new_entry['date'])
            st.session_state.workouts = pd.concat([st.session_state.workouts, new_entry], ignore_index=True)
            st.success("Workout logged successfully! ✅")

# ---------------------------
# Analysis
elif menu == "Analysis":
    st.title("📊 Workout Analysis")

    period = st.radio("Select Period", ["Daily", "Weekly", "Yearly"])

    if df.empty:
        st.warning("No workout data available to analyze.")
    else:
        df_indexed = df.set_index('date')

        if period == "Daily":
            grouped = df.groupby(df['date'].dt.date)[['duration_min', 'calories']].sum()
        elif period == "Weekly":
            grouped = df_indexed.resample('W').sum()
        else:  # Yearly
            grouped = df_indexed.resample('Y').sum()

        if grouped.empty or grouped.isnull().all().all():
            st.warning(f"No data available for {period.lower()} analysis. Please log more workouts.")
        else:
            st.write(f"Grouped data by {period.lower()}:")
            st.dataframe(grouped)
            st.line_chart(grouped)

# ---------------------------
# Settings
elif menu == "Settings":
    st.title("⚙ Settings")
    st.write("""
    - Connect with external apps like **Strava**, **Garmin**, **Google Fit**, **Apple Health**.  
    - Set workout reminders.  
    - Customize goals and preferences.  
    """)
    st.info("API integration and reminders need backend services and proper authentication setups.")

# ---------------------------
# Footer
st.markdown("---")
st.markdown("© 2025 **Gym Logger by Sow**")
