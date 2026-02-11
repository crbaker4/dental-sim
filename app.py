import streamlit as st
import random

st.title("Dental Practice Career Mode")

# ---------- STARTING STATE ----------
if "state" not in st.session_state:
    st.session_state.state = {
        "month": 1,
        "cash": 80000,
        "patients": 1200,
        "reputation": 60,
        "staff_morale": 55,
        "operatories": 4,
        "hygienists": 1,
        "assistants": 1,
        "associates": 0,
        "stress": 30,
        "locations": 1
    }

s = st.session_state.state

# ---------- DISPLAY DASHBOARD ----------
st.write(f"Month: {s['month']}")
st.write(f"Cash: ${s['cash']}")
st.write(f"Patients: {s['patients']}")
st.write(f"Reputation: {s['reputation']}")
st.write(f"Staff morale: {s['staff_morale']}")
st.write(f"Stress: {s['stress']}")
st.write(f"Operatories: {s['operatories']}")
st.write(f"Locations: {s['locations']}")

st.divider()
st.subheader("Choose your move")

# ---------- ACTIONS ----------
if st.button("Hire Hygienist"):
    s["hygienists"] += 1
    s["cash"] -= 5000
    s["staff_morale"] += 5
    s["month"] += 1
    st.rerun()

if st.button("Expand Operatories"):
    s["operatories"] += 1
    s["cash"] -= 25000
    s["stress"] += 5
    s["month"] += 1
    st.rerun()

if st.button("Open Second Location"):
    if s["cash"] > 100000:
        s["locations"] += 1
        s["cash"] -= 100000
        s["stress"] += 10
    else:
        st.warning("Not enough cash")
    s["month"] += 1
    st.rerun()

if st.button("Run Marketing Campaign"):
    gain = random.randint(20, 60)
    s["patients"] += gain
    s["cash"] -= 3000
    s["reputation"] += 3
    s["month"] += 1
    st.rerun()

if st.button("Do Nothing"):
    s["month"] += 1
    st.rerun()

# ---------- MONTHLY EFFECTS ----------
production = s["patients"] * 15
expenses = (s["hygienists"] * 4000) + (s["assistants"] * 3000)

s["cash"] += production - expenses
