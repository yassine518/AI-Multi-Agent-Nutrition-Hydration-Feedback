import streamlit as st
import pandas as pd
from datetime import datetime
from multi_agent_system import MultiAgentSystem
from src.database import create_tables, log_intake, get_intake_history

# Initialize database
create_tables()  # Changed from init_db()

# Debug session state
st.write("Debug: Session state:", st.session_state)

# Initialize session state
if "tracker_started" not in st.session_state:
    st.session_state.tracker_started = False

# Welcome section
if not st.session_state.tracker_started:
    st.title("Welcome to AI Water Tracker")
    st.markdown("""
        Track your daily hydration with help of AI assistant.
        Log your intake, get smart feedback, and stay healthy effortlessly
    """)
    if st.button("Start Tracking"):
        st.session_state.tracker_started = True
        st.rerun()
else:
    st.title("AI Water Tracker Dashboard")
    # Intake Input
    st.sidebar.header("Log Your Health Data")
    user_id = st.sidebar.text_input("User ID", value="user_123")
    intake_ml = st.sidebar.number_input("Water Intake (ml)", min_value=0, step=100)
    meal = st.sidebar.text_input("Meal")
    calories = st.sidebar.number_input("Calories", min_value=0, step=50)
    
    if st.sidebar.button("Submit"):
        if user_id and intake_ml > 0 and meal and calories > 0:
            try:
                log_intake(user_id, intake_ml)
                st.success(f"Logged {intake_ml}ml for {user_id}")
                
                multi_agent_system = MultiAgentSystem()
                meal_data = {"meal": meal, "calories": calories}
                health_analysis = multi_agent_system.analyze_health_data(intake_ml, meal_data)
                
                st.info(f"AI Water Intake Feedback: {health_analysis['water_analysis']}")
                st.info(f"AI Meal Tracker Feedback: {health_analysis['meal_analysis']['message']}")
            except Exception as e:
                st.error(f"Error logging intake: {e}")

    # Divider
    st.markdown("---")

    # History Section
    st.header("Water Intake History")
    if user_id:
        try:
            history = get_intake_history(user_id)
            st.write("Debug: History data:", history)
            if history:
                dates = [datetime.strptime(row[1], "%Y-%m-%d") for row in history]
                values = [row[0] for row in history]
                df = pd.DataFrame({
                    "Date": dates,
                    "Water Intake (ml)": values
                })
                st.dataframe(df)
                st.line_chart(df, x="Date", y="Water Intake (ml)")
            else:
                st.warning("No water intake data found. Please log your intake first.")
        except Exception as e:
            st.error(f"Error fetching history: {e}")
    else:
        st.warning("Please enter a User ID to view history.")
