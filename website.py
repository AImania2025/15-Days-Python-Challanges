import streamlit as st

# Set website title
st.set_page_config(page_title="TravelWith Sow", page_icon="🌍", layout="wide")

# Header section
st.title("🌍 TravelWith Sow")
st.subheader("Your Personal Travel Planner ✈️")

st.markdown("---")

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Plan a Trip", "About"])

# Home Page
if page == "Home":
    st.header("Welcome to TravelWith Sow!")
    st.write("""
    Plan your dream trip with ease.  
    Choose destinations, set travel dates, and get recommendations.  
    Start planning today and make your journey unforgettable! 🚀
    """)
    st.image("https://images.unsplash.com/photo-1507525428034-b723cf961d3e", caption="Let's Explore the World!")

# Plan a Trip Page
elif page == "Plan a Trip":
    st.header("🗺️ Plan Your Trip")

    destination = st.text_input("Enter Destination")
    start_date = st.date_input("Start Date")
    end_date = st.date_input("End Date")
    travelers = st.number_input("Number of Travelers", min_value=1, step=1)

    interests = st.multiselect(
        "What are you interested in?",
        ["Beaches", "Mountains", "Historical Sites", "Adventure Sports", "Food & Culture", "Shopping"]
    )

    if st.button("Generate Travel Plan"):
        st.success(f"✈️ Trip planned to **{destination}** from **{start_date}** to **{end_date}** for **{travelers} traveler(s)**.")
        if interests:
            st.write("Your interests include:", ", ".join(interests))
        else:
            st.write("No specific interests selected.")

# About Page
elif page == "About":
    st.header("ℹ️ About TravelWith Sow")
    st.write("""
    TravelWith Sow is a simple travel planner built with **Streamlit**.  
    It helps you organize your trips, explore destinations, and plan according to your interests.  

    💡 Developed as a fun project using Python & Streamlit.
    """)
    st.markdown("**Happy Travels! 🌍✨**")
