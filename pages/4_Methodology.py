import streamlit as st  # Import Streamlit for building the web app

# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="Baby Benefits Calculator"
)
# endregion <--------- Streamlit App Configuration --------->

# Set the title of the page
st.title("Methodology")

# Markdown section to describe the data flow and methodology of the application
st.markdown("""
## Data Flow & Implementation
The application uses data from official government sources and preschool providers to calculate financial contributions and subsidies. Below is the breakdown of the implementation:

### Use Case 1: Baby Bonus Scheme Calculator
1. **User Inputs**: Birth order, CDA savings, etc.
2. **Processing**: Calculates cash gifts and government contributions based on input.
3. **Outputs**: Provides a timeline of disbursements and total amounts.

### Use Case 2: Preschool Subsidy Calculator
1. **User Inputs**: Parental income, baby’s age, citizenship, etc.
2. **Processing**: Calculates basic and additional subsidies and enrollment fees.
3. **Outputs**: Provides a breakdown of fees for various preschools with and without subsidies.
""")

# Explanation of the data flow for each use case
st.markdown("""
## Flowcharts
Below are the flowcharts representing the process for each use case:
""")

# Display the flowchart images for both calculators
st.image('./images/baby_bonus_flowchart.png', caption="Baby Bonus Scheme Calculator Flowchart")  # Baby Bonus Scheme flowchart
st.image('./images/preschool_subsidy_flowchart.png', caption="Preschool Subsidy Calculator Flowchart")  # Preschool Subsidy flowchart