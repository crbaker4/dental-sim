import streamlit as st
import random

st.title("Dental Practice Career Mode")

# ---------- START STATE ----------
if "state" not in st.session_state:
    st.session_state.state = {
        "month": 1,
        "cash": 90000,
        "patients": 1500,
        "reputation": 60,
        "staff_morale": 55,
        "operatories": 4,
        "hygienists": 1,
        "assistants": 2,
        "associates": 0,
        "stress": 30,
        "locations": 1,
        "expansion_pressure": 20
    }

s = st.session_state.state

# ---------- DASHBOARD ----------
st.write(f"Month: {s['month']}")
st.write(f"Cash: ${s['cash']}")
st.write(f"Patients: {s['patients']}")
st.write(f"Locations: {s['locations']}")
st.write(f"Reputation: {s['reputation']}")
st.write(f"Stress: {s['stress']}")
st.write(f"Expansion pressure: {s['expansion_pressure']}")

st.divider()

# ---------- RANDOM EVENT ----------
events = [
    "Your brother wants to expand faster",
    "Hygienist might quit",
    "Schedule is overloaded",
    "Bank offers loan",
    "Lots of new patients coming in",
    "Staff burnout rising"
]

event = random.choice(events)
st.subheader(event)

st.write("What do you do?")

# ---------- CHOICES ----------
if st.button("Expand capacity"):
    s["operatories"] += 1
    s["cash"] -= 20000
    s["stress"] += 5
    s["expansion_pressure"] -= 5
    s["month"] += 1
    st.rerun()

if st.button("Hire associate"):
    s["associates"] += 1
    s["cash"] -= 7000
    s["stress"] -= 2
    s["month"] += 1
    st.rerun()

if st.button("Focus on profit"):
    s["cash"] += 12000
    s["reputation"] -= 2
    s["month"] += 1
    st.rerun()

if st.button("Open second location"):
    if s["cash"] > 80000:
        s["locations"] += 1
        s["cash"] -= 80000
        s["stress"] += 12
    else:
        st.warning("Need more cash")
    s["month"] += 1
    st.rerun()

if st.button("Stabilize team"):
    s["staff_morale"] += 5
    s["stress"] -= 3
    s["month"] += 1
    st.rerun()

# ---------- MONTHLY ECONOMY ----------
production = s["patients"] * 10 + s["associates"] * 22000
expenses = s["hygienists"] * 4000 + s["assistants"] * 3000 + s["locations"] * 15000

s["cash"] += production - expenses
s["expansion_pressure"] += random.randint(1,4)
