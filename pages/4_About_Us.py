import streamlit as st

# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="My Streamlit App"
)
# endregion <--------- Streamlit App Configuration --------->

st.title("About Baby Benefits Calculator")

st.markdown("""
    Welcome to the **Baby Benefits Calculator**, a user-friendly tool designed to help you easily estimate the financial support you can receive through various baby benefit schemes.

    By leveraging the OpenAI API, this app quickly calculates the available benefits based on the information you provide.
""")

with st.expander("How to Use the Baby Benefits Calculator"):
    st.write("""
    1. Fill in the required information in the form.
    2. Click the 'Calculate' button to process your input.
    3. The calculator will instantly generate the baby benefits you may be eligible to receive.
    """)
