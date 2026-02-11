import streamlit as st
import random

st.title("Dental Practice Career Mode")

# ----- STATE -----
if "state" not in st.session_state:
    st.session_state.state = {
        "month": 1,
        "cash": 100000,
        "stress": 30,
        "reputation": 60,
        "locations": 1
    }

s = st.session_state.state

st.write("Month", s["month"])
st.write("Cash", s["cash"])
st.write("Stress", s["stress"])
st.write("Reputation", s["reputation"])
st.write("Locations", s["locations"])

st.divider()

# ----- SCENARIOS -----
scenarios = [
    {
        "text": "Your hygienist might quit.",
        "choices": [
            ("Give raise", {"cash": -5000, "stress": -3}),
            ("Let them leave", {"stress": 5}),
            ("Hire new one", {"cash": -3000}),
            ("Ignore it", {"stress": 8})
        ]
    },
    {
        "text": "Your brother wants to expand.",
        "choices": [
            ("Open new location", {"cash": -80000, "locations": 1, "stress": 10}),
            ("Wait", {"stress": -2}),
            ("Take loan", {"cash": 50000, "stress": 5}),
            ("Say no", {"stress": 3})
        ]
    },
    {
        "text": "Schedule is overloaded.",
        "choices": [
            ("Hire associate", {"cash": -7000, "stress": -4}),
            ("Work more", {"stress": 6}),
            ("Raise prices", {"cash": 10000}),
            ("Do nothing", {"stress": 4})
        ]
    }
]

scenario = random.choice(scenarios)
st.subheader(scenario["text"])

# ----- BUTTONS -----
for label, effects in scenario["choices"]:
    if st.button(label):
        for k, v in effects.items():
            s[k] = s.get(k, 0) + v

        s["month"] += 1
        st.rerun()
