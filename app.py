import streamlit as st
import requests

# ---------------------------------
# PAGE CONFIG
# ---------------------------------
st.set_page_config(
    page_title="Currency Converter",
    page_icon="💱",
    layout="wide"
)

# ---------------------------------
# HEADER FUNCTION (Colourful)
# ---------------------------------
def colored_header(title, color="#4F46E5"):
    st.markdown(
        f"""
        <h1 style='color:{color}; text-align:center; margin-top:0px;'>{title}</h1>
        """,
        unsafe_allow_html=True
    )

# ---------------------------------
# CARD STYLE (Metrics)
# ---------------------------------
def style_metric_cards():
    st.markdown("""
        <style>
            [data-testid="stMetric"] {
                background-color: #EEF2FF;
                padding: 25px;
                border-radius: 14px;
                box-shadow: 0px 3px 12px rgba(0,0,0,0.08);
                margin: 10px;
            }
        </style>
    """, unsafe_allow_html=True)


# ---------------------------------
# API FUNCTION
# Using https://api.exchangerate-api.com/
# ---------------------------------
def convert_currency(from_curr, to_curr, amount):
    url = f"https://api.exchangerate-api.com/v4/latest/{from_curr}"
    response = requests.get(url)

    if response.status_code != 200:
        return None

    rates = response.json().get("rates", {})
    if to_curr not in rates:
        return None

    return round(amount * rates[to_curr], 2)


# ---------------------------------
# TITLE
# ---------------------------------
colored_header("💱 Currency Converter", "#0EA5E9")

st.write("### Convert money instantly with real-time exchange rates 🌍")

# ---------------------------------
# SIDEBAR (currency selection)
# ---------------------------------
st.sidebar.title("🌐 Currency Options")

currency_list = [
    "USD", "INR", "EUR", "GBP", "AED", "JPY", "AUD", "CAD",
    "SGD", "CHF", "CNY", "NZD", "ZAR", "HKD"
]

from_currency = st.sidebar.selectbox("From Currency", currency_list)
to_currency = st.sidebar.selectbox("To Currency", currency_list)

amount = st.sidebar.number_input("Amount", min_value=0.0, value=1.0)

st.sidebar.markdown("---")
st.sidebar.write("Made by ❤️ Streamlit + Python")

# ---------------------------------
# MAIN SECTION
# ---------------------------------
if st.button("Convert Now"):
    st.info(f"Converting {amount} {from_currency} to {to_currency} ...")

    result = convert_currency(from_currency, to_currency, amount)

    if result is None:
        st.error("❌ Conversion failed. Try again.")
    else:
        col1, col2 = st.columns(2)

        with col1:
            st.metric("Input Amount", f"{amount} {from_currency}")
        with col2:
            st.metric("Converted Amount", f"{result} {to_currency}")

        style_metric_cards()

        st.success("🎉 Conversion Successful!")


# ---------------------------------
# FOOTER
# ---------------------------------
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align:center; color:gray;'>Real-time currency conversion using ExchangeRate API</p>",
    unsafe_allow_html=True
)
