import streamlit as st
import random

st.title("Dental Practice Career Mode")

# ---------- STATE ----------
if "state" not in st.session_state:
    st.session_state.state = {
        "month": 1,
        "cash": 90000,
        "stress": 30,
        "reputation": 60,
        "locations": 1,
        "growth": 0
    }

s = st.session_state.state

st.write(f"Month {s['month']}")
st.write(f"Cash: ${s['cash']}")
st.write(f"Stress: {s['stress']}")
st.write(f"Reputation: {s['reputation']}")
st.write(f"Locations: {s['locations']}")
st.write(f"Growth: {s['growth']}")

st.divider()

# ---------- EVENT LOGIC ----------
if s["cash"] < 20000:
    event = {
        "text": "Cash is getting tight.",
        "choices": [
            ("Take bank loan", {"cash": 50000, "stress": 5}),
            ("Cut staff", {"cash": 10000, "reputation": -5}),
            ("Work more", {"stress": 8}),
            ("Do nothing", {"stress": 3})
        ]
    }

elif s["stress"] > 70:
    event = {
        "text": "You are burning out.",
        "choices": [
            ("Take week off", {"stress": -15, "cash": -5000}),
            ("Hire associate", {"cash": -7000, "stress": -10}),
            ("Push through", {"stress": 10}),
            ("Sell practice", {"cash": 200000})
        ]
    }

elif s["growth"] > 50:
    event = {
        "text": "Practice is booming. Expansion time?",
        "choices": [
            ("Open second location", {"cash": -80000, "locations": 1, "stress": 10}),
            ("Hire more staff", {"cash": -10000, "growth": 10}),
           
