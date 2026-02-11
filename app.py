import streamlit as st

st.title("Dental Practice Career Mode")

if "month" not in st.session_state:
    st.session_state.month = 1
    st.session_state.cash = 60000
    st.session_state.reputation = 50

st.write(f"Month: {st.session_state.month}")
st.write(f"Cash: ${st.session_state.cash}")
st.write(f"Reputation: {st.session_state.reputation}")

st.write("Choose your move:")

if st.button("Hire Hygienist"):
    st.session_state.cash -= 4000
    st.session_state.reputation += 3
    st.session_state.month += 1
    st.rerun()

if st.button("Run Marketing"):
    st.session_state.cash -= 2000
    st.session_state.reputation += 5
    st.session_state.month += 1
    st.rerun()

if st.button("Do Nothing"):
    st.session_state.month += 1
    st.rerun()
