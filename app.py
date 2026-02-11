import streamlit as st
import random

st.title("Dental Practice Career Mode")

# ---------- STATE ----------
if "state" not in st.session_state:
    st.session_state.state = {
        "month": 1,
        "cash": 100000,
        "stress": 30,
        "reputation": 60,
        "locations": 1
    }

s = st.session_state.state

st.write(f"Month {s['month']}")
st.write(f"Cash: ${s['cash']}")
st.write(f"Stress: {s['stress']}")
st.write(f"Reputation: {s['reputation']}")
st.write(f"Locations: {s['locations']}")

st.divider()

# ---------- SCENARIOS ----------
scenarios = [

{
"text": "Your hygienist says they might quit.",
"choices": [
("Give them a raise", {"cash": -5000, "stress": -3}),
("Let them leave", {"stress": 5}),
("Hire replacement", {"c
