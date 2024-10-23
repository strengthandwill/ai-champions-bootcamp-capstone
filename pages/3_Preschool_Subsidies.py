import streamlit as st
import pandas as pd
from logics.preschool_subsidies_query_handler import calculate_preschool_subsidies  # Import the function to calculate preschool subsidies
from helper_functions.utility import check_password  # Import password check function

# Function to set up the introduction section
def setup_intro(intro):
    # Markdown explaining the preschool subsidies for parents of Singapore Citizen children
    intro.markdown(f"""
        Parents of Singapore Citizen children enrolled in licensed childcare centres can access financial support through government subsidies. The Basic Subsidy provides:
        - Up to $600 per month for full-day infant care.
        - Up to $300 per month for full-day childcare.
        
        Working mothers with a gross monthly household income of $12,000 or below are eligible for the Additional Subsidy, offering further assistance. Lower-income families qualify for higher subsidies.
                   
        Families with **five or more members**, including three non-working dependants, can opt to calculate their subsidy based on **per capita income (PCI)** to access higher subsidies.
    """)
    intro.subheader("Calculate the preschool subsidies that you can receive!")  # Subtitle for the form
    return  # Optional, but used to signify the end of the function

# Function to set up the form for user input and display results
def setup_form(input, result):
    # Section to collect financial information
    input.subheader("Financial status")
    father_gross_monthly_income = input.number_input(label="Father's Monthly Income ($)", min_value=0, step=100)  # Input for father's income
    col1, col2 = input.columns(2)  # Create two columns for mother information
    mother_working_status = col1.selectbox("Mother Working Status", ("Working Mothers", "Non-Working Mothers"))  # Input for mother's working status
    mother_gross_monthly_income = col2.number_input(label="Mother's Monthly Income ($)", min_value=0, step=100)  # Input for mother's income

    # Section to collect baby information
    input.subheader("Baby info")
    col1, col2 = input.columns(2)  # Create two columns for baby information
    baby_birth_date = col1.date_input(label="Birth Date")  # Input for baby's birth date
    baby_citizenship = col2.selectbox("Citizenship", ("Singapore Citizen", "Singapore Permanent Residents", "Foreigners"))  # Input for baby's citizenship

    # Section to trigger the calculation
    input.subheader("Calculate")
    as_of = input.date_input(label="As of")  # Input for the date as of when the calculation is done
    submitted = input.form_submit_button("Calculate")  # Button to submit the form

    # If the form is submitted, calculate the preschool subsidies using the input values
    if submitted:
        household_income, baby_details, subsidies, enrollment_fees = calculate_preschool_subsidies(
            father_gross_monthly_income, mother_gross_monthly_income, mother_working_status,
            baby_birth_date, baby_citizenship,
            as_of
        )  
        # Update the result container with the calculated values
        update_result(result, household_income, baby_details, subsidies, enrollment_fees)

# Function to update and display the results
def update_result(result, household_income, baby_details, subsidies, enrollment_fees):
    # Display household income details
    result.subheader("Household Income")
    result.html(household_income["Overview"])  # Display an overview of household income
    result.write(f"Gross Monthly Household Income: ${household_income['Gross Monthly Household Income']:,.0f}")  # Display gross monthly household income
    result.write(f"Gross Monthly Per Capita Income (PCI): ${household_income['Gross Monthly Per Capita Income']:,.0f}")  # Display PCI
    result.html(household_income["Summary"])  # Display a summary of the household income

    # Display baby details
    result.subheader("Baby Details")
    result.write(f"Baby's Age: {baby_details['Baby Age']}")  # Display baby's age
    result.write(f"Preschool Programme: {baby_details['Preschool Programme']}")  # Display preschool programme the baby is enrolled in
    result.html(baby_details["Summary"])  # Display a summary of baby details

    # Display subsidy details
    result.subheader("Subsidies")
    if subsidies["Basic Subsidy"] is not None:
        result.write(f"Basic Subsidy: ${subsidies['Basic Subsidy']:,.0f}")  # Display basic subsidy amount if available
    if subsidies["Additional Subsidy"] is not None:
        result.write(f"Additional Subsidy: ${subsidies['Additional Subsidy']:,.0f}")  # Display additional subsidy amount if available
    if subsidies["Max KiFAS"] is not None:
        result.write(f"Max KiFAS: ${subsidies['Max KiFAS']:,.0f}")  # Display maximum KiFAS if available
    result.html(subsidies["Summary"])  # Display a summary of the subsidies

    # Display enrollment fee details
    result.subheader("Enrollment Fees")
    result.html(enrollment_fees["Overview"])  # Display an overview of enrollment fees
    enrollment_fees_by_preschools = pd.DataFrame(enrollment_fees["Preschools"]).T  # Convert the fees by preschools into a DataFrame
    enrollment_fees_by_preschools.index.name = 'Preschool'  # Set the index name to 'Preschool'
    enrollment_fees_by_preschools['With Subsidies'] = enrollment_fees_by_preschools['With Subsidies'].apply(lambda x: f"${x:,.0f}")  # Format 'With Subsidies' fees
    enrollment_fees_by_preschools['Without Subsidies'] = enrollment_fees_by_preschools['Without Subsidies'].apply(lambda x: f"${x:,.0f}")  # Format 'Without Subsidies' fees
    result.dataframe(enrollment_fees_by_preschools)  # Display the enrollment fees as a table
    result.html(enrollment_fees["Summary"])  # Display a summary of the enrollment fees

# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="Baby Benefits Calculator"
)
# endregion <--------- Streamlit App Configuration --------->

# Display app title
st.title("🏫 Preschool Subsidies Calculator")

# Check if the user is authorized using a password check
if not check_password():
    st.stop()  # Stop the app if the password is incorrect

# Create containers for the introduction, input form, and results
intro = st.container()
input = st.form('form')
result = st.container(border=True)

# Set up the introduction and input form
setup_intro(intro)
setup_form(input, result)