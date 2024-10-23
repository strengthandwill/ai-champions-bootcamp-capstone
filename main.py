# Import Streamlit to build and run the app interface
import streamlit as st

# region <--------- Streamlit App Configuration --------->
# Set up the basic configuration for the Streamlit app
st.set_page_config(
    layout="centered",  # Layout centered for a neat display
    page_title="Baby Benefits Calculator"  # Set the title of the web page
)
# endregion <--------- Streamlit App Configuration --------->

# Main title displayed at the top of the app
st.title("🎁 Baby Benefits Calculator")

# Add links to different pages within the app for navigation
# Link to the "Baby Bonus Calculator" page with a baby icon
st.page_link("pages/2_Baby_Bonus.py", label="Baby Bonus Calculator", icon="👶")

# Link to the "Preschool Subsidies Calculator" page with a school icon
st.page_link("pages/3_Preschool_Subsidies.py", label="Preschool Subsidies Calculator", icon="🏫")

# Disclaimer section explaining that the app is for educational purposes only
# Uses an expander so users can expand/collapse the disclaimer
with st.expander("Disclaimer"):
    # Display the disclaimer text within a markdown block
    st.markdown(f"""
        **IMPORTANT NOTICE: This web application is a prototype developed for educational purposes only. The information provided here is NOT intended for real-world usage and should not be relied upon for making any decisions, especially those related to financial, legal, or healthcare matters.
        
        Furthermore, please be aware that the LLM may generate inaccurate or incorrect information. You assume full responsibility for how you use any generated output.

        Always consult with qualified professionals for accurate and personalized advice.
    """)