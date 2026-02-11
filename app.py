import streamlit as st
import random

st.title("Dental Empire Career Mode")

# ---------- STATE ----------
if "state" not in st.session_state:
    st.session_state.state = {
        "month": 1,
        "cash": 120000,
        "patients": 1400,
        "reputation": 60,
        "staff_morale": 55,
        "operatories": 4,
        "hygienists": 1,
        "assistants": 2,
        "associates": 0,
        "stress": 25,
        "locations": 1,
        "loan": 300000
    }

s = st.session_state.state

# ---------- DASHBOARD ----------
st.write(f"Month: {s['month']}")
st.write(f"Cash: ${s['cash']}")
st.write(f"Patients: {s['patients']}")
st.write(f"Locations: {s['locations']}")
st.write(f"Loan: ${s['loan']}")
st.write(f"Stress: {s['stress']}")
st.write(f"Staff morale: {s['staff_morale']}")

st.divider()

# ---------- RANDOM EVENT ----------
event = random.choice([
    "Hygienist wants a raise",
    "Schedule is packed",
    "Bank offers expansion loan",
    "Associate wants to join",
    "Lots of cancellations",
    "Equipment breaks"
])

st.subheader(f"Event: {event}")

# ---------- DECISIONS ----------
if st.button("Invest in growth"):
    s["operatories"] += 1
    s["loan"] += 50000
    s["cash"] -= 10000
    s["stress"] += 5
    s["month"] += 1
    st.rerun()

if st.button("Hire associate"):
    s["associates"] += 1
    s["cash"] -= 8000
    s["stress"] -= 2
    s["month"] += 1
    st.rerun()

if st.button("Focus on profit"):
    s["cash"] += 15000
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

if st.button("Take month slow"):
    s["stress"] -= 5
    s["month"] += 1
    st.rerun()

# ---------- MONTHLY MONEY ----------
production = s["patients"] * 12 + s["associates"] * 25000
expenses = s["hygienists"] * 4000 + s["assistants"] * 3000 + s["loan"] * 0.01

s["cash"] += production - expenses
