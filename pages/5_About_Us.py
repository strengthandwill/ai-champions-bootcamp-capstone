import streamlit as st  # Import Streamlit for building the web app

# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="Baby Benefits Calculator"
)
# endregion <--------- Streamlit App Configuration --------->

# Set the title for the "About Us" section
st.title("😃 About Us")

# Markdown section to explain the scope, objectives, data sources, features, and repository link for the project
st.markdown("""
## Project Scope
The goal of this project is to help parents in Singapore plan for their child's future by calculating available financial assistance schemes such as the Baby Bonus and Preschool Subsidies.

## Objectives
1. **Baby Bonus Scheme Calculator**: Helps parents understand the amount of cash gift and government contributions to their child’s CDA based on birth order, CDA savings, and other parameters.
2. **Preschool Subsidies Calculator**: Calculates the basic and additional subsidies for childcare based on parental income and baby details.

## Data Sources
The data used in this application is derived from:
- Singapore Government Websites on **Baby Bonus Scheme**.
- Publicly available information on **Preschool Subsidies**.
- Enrollment fee structures from prominent preschools such as:
    - PCF Sparkletots
    - My First Skool
    - My World Preschool
    - Skool4Kidz
    - E-Bridge Preschool

## Features
- **Baby Bonus Calculator**: Users can input details such as birth order and CDA savings to get a detailed breakdown of cash gifts and government contributions over time.
- **Preschool Subsidies Calculator**: Users can calculate the fees for various preschools with and without subsidies.

## Repository
You can find the source code for this project on GitHub:
[AI Champions Bootcamp Capstone Repository](https://github.com/strengthandwill/ai-champions-bootcamp-capstone)            
""")