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

with st.expander("Disclaimer"):
    st.markdown(f"""
        **IMPORTANT NOTICE:** This web application is a prototype developed for educational purposes only. The information provided here is NOT intended for real-world usage and should not be relied upon for making any decisions, especially those related to financial, legal, or healthcare matters.

        Furthermore, please be aware that the LLM may generate inaccurate or incorrect information. You assume full responsibility for how you use any generated output.

        Always consult with qualified professionals for accurate and personalized advice.
    """)