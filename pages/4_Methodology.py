import streamlit as st

st.title("Methodology")
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

## Flowcharts
Below are the flowcharts representing the process for each use case:
""")

st.image('./images/baby_bonus_flowchart.png', caption="Baby Bonus Scheme Calculator Flowchart")
st.image('./images/preschool_subsidy_flowchart.png', caption="Preschool Subsidy Calculator Flowchart")