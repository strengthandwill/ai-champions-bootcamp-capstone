import streamlit as st
import pandas as pd
from logics.preschool_subsidies_query_handler import calculate_preschool_subsidies
from helper_functions.utility import check_password

def setup_intro(intro):
    intro.markdown(f"""
        Parents of Singapore Citizen children enrolled in licensed childcare centres can access financial support through government subsidies. The Basic Subsidy provides:
        - Up to $600 per month for full-day infant care.
        - Up to $300 per month for full-day childcare.
        
        Working mothers with a gross monthly household income of $12,000 or below are eligible for the Additional Subsidy, offering further assistance. Lower-income families qualify for higher subsidies.
                   
        Families with **five or more members**, including three non-working dependants, can opt to calculate their subsidy based on **per capita income (PCI)** to access higher subsidies.
    """)
    intro.subheader("Calculate the preschool subsidies that you can receive!")
    return

def setup_form(input, result):
    input.subheader("Financial status")
    father_gross_monthly_income = input.number_input(label="Father's Monthly Income ($)", min_value=0, step=100)
    col1, col2 = input.columns(2)    
    mother_working_status = col1.selectbox("Mother Working Status", ("Working Mothers", "Non-Working Mothers"),)  
    mother_gross_monthly_income = col2.number_input(label="Mother's Monthly Income ($)", min_value=0, step=100)
    

    input.subheader("Baby info")
    col1, col2 = input.columns(2)    
    baby_birth_date = col1.date_input(label="Birth Date")
    baby_citizenship = col2.selectbox("Citizenship", ("Singapore Citizen", "Singapore Permanent Residents", "Foresigners"),)

    input.subheader("Calculate")
    as_of = input.date_input(label="As of")
    submitted = input.form_submit_button("Calculate")
    if submitted:
        household_income, baby_details, subsidies, enrollment_fees = calculate_preschool_subsidies(
            father_gross_monthly_income, mother_gross_monthly_income, mother_working_status,
            baby_birth_date, baby_citizenship,
            as_of)  
        update_result(result, household_income, baby_details, subsidies, enrollment_fees)                  
            

def update_result(result, household_income, baby_details, subsidies, enrollment_fees ):
    result.subheader("Household Income")
    result.html(household_income["Overview"])  
    result.write(f"Gross Monthly Household Income: ${household_income["Gross Monthly Household Income"]:,.0f}")  
    result.write(f"Gross Monthly Per Capita Income (PCI): ${household_income["Gross Monthly Per Capita Income"]:,.0f}")      
    result.html(household_income["Summary"])

    result.subheader("Baby Details")
    result.write(f"Baby's Age: {baby_details["Baby Age"]}")  
    result.write(f"Preschool Programme: {baby_details["Preschool Programme"]}")  
    result.html(baby_details["Summary"])  

    result.subheader("Subsidies")
    if (subsidies["Basic Subsidy"] is not None):
        result.write(f"Basic Subsidy: ${subsidies["Basic Subsidy"]:,.0f}")  
    if (subsidies["Additional Subsidy"] is not None):
        result.write(f"Additional Subsidy: ${subsidies["Additional Subsidy"]:,.0f}")          
    if (subsidies["Max KiFAS"] is not None):
        result.write(f"Max KiFAS: ${subsidies["Max KiFAS"]:,.0f}")                  
    result.html(subsidies["Summary"])   

    result.subheader("Enrollment Fees")
    result.html(enrollment_fees["Overview"])
    enrollment_fees_by_preschools = pd.DataFrame(enrollment_fees["Preschools"]).T
    enrollment_fees_by_preschools.index.name = 'Preschool'
    enrollment_fees_by_preschools['With Subsidies'] = enrollment_fees_by_preschools['With Subsidies'].apply(lambda x: f"${x:,.0f}")
    enrollment_fees_by_preschools['Without Subsidies'] = enrollment_fees_by_preschools['Without Subsidies'].apply(lambda x: f"${x:,.0f}")
    result.dataframe(enrollment_fees_by_preschools)
    result.html(enrollment_fees["Summary"])   
 

# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="KK Streamlit App"
)
# endregion <--------- Streamlit App Configuration --------->

st.title("Preschool Subsidies Calculator")

# Check if the password is correct.  
if not check_password():  
    st.stop()

intro = st.container()
input = st.form('form')
result = st.container(border=True)

setup_intro(intro)
setup_form(input, result)