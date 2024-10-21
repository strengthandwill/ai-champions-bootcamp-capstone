# Set up and run this Streamlit App
import streamlit as st

# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="Baby Benefits Calculator"
)
# endregion <--------- Streamlit App Configuration --------->

st.title("🎁 Baby Benefits Calculator")

st.page_link("pages/2_Baby_Bonus.py", label="Baby Bonus Calculator", icon="👶")
st.page_link("pages/3_Preschool_Subsidies.py", label="Preschool Subsidies Calculator", icon="🏫")