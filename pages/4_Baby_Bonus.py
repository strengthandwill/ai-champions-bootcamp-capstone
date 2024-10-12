import streamlit as st
from logics.baby_bonus_query_handler import calculate_baby_bonus

# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="KK Streamlit App"
)
# endregion <--------- Streamlit App Configuration --------->

st.title("Baby Bonus Calculator")

st.write("This is a Streamlit App that calculates baby bonus.")

with st.form("bb_form"):
    birth_order = st.number_input(label="Birth Order", min_value=1, step=1)
    birth_date = st.date_input(label="Birth Date")
    as_of = st.date_input(label="Baby Bonus received as of")
    submitted = st.form_submit_button("Calculate")
    if submitted:
        amount = calculate_baby_bonus(birth_order=birth_order, birth_date=birth_date, as_of=as_of)
        st.write(amount)
        st.toast("Submitted")


