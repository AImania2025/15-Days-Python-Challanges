import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="💰 Travel Expense Splitter", page_icon="💰", layout="centered")

# --- TITLE ---
st.markdown("<h2 style='text-align:center; color:#1E90FF;'>💰 Travel Expense Splitter</h2>", unsafe_allow_html=True)
st.write("Easily split shared trip costs between Ravi, Somu, Ramu, and Ramesh!")

# --- MEMBERS ---
members = ["Ravi", "Somu", "Ramu", "Ramesh"]

# --- EXPENSE INPUT SECTION ---
st.markdown("### ✍️ Enter Trip Expenses")

car_travel = st.number_input("🚗 Car Travel Expenses (₹)", min_value=0.0, step=100.0)
food = st.number_input("🍽️ Food Expenses (₹)", min_value=0.0, step=100.0)
parking = st.number_input("🅿️ Parking Charges (₹)", min_value=0.0, step=50.0)
boating = st.number_input("🚤 Boating Charges (₹)", min_value=0.0, step=50.0)
room = st.number_input("🏨 Room Accommodation (₹)", min_value=0.0, step=100.0)

# --- TOTAL CALCULATION ---
total_expense = car_travel + food + parking + boating + room
num_people = len(members)
share_per_person = total_expense / num_people if num_people else 0

# --- DISPLAY TOTAL ---
st.markdown("---")
st.markdown(f"### 💵 **Total Trip Expense:** ₹ {total_expense:,.2f}")
st.markdown(f"### 👥 **Each Person Pays:** ₹ {share_per_person:,.2f}")

# --- BREAKDOWN TABLE ---
st.markdown("#### 📊 Expense Breakdown")
st.write({
    "Car Travel": f"₹ {car_travel:,.2f}",
    "Food": f"₹ {food:,.2f}",
    "Parking": f"₹ {parking:,.2f}",
    "Boating": f"₹ {boating:,.2f}",
    "Room": f"₹ {room:,.2f}"
})

# --- OPTIONAL: WHO PAID ---
st.markdown("### 💳 Who Paid What?")
who_paid = st.radio("Select who paid the bill:", members)
st.write(f"👉 {who_paid} initially paid ₹ {total_expense:,.2f}. Others owe ₹ {share_per_person:,.2f} each to {who_paid}.")

# --- FOOTER ---
st.markdown("---")
st.markdown("<p style='text-align:center; color:gray;'>Developed with ❤️ using Streamlit</p>", unsafe_allow_html=True)
