import streamlit as st
import pandas as pd
from logics.baby_bonus_query_handler import calculate_baby_bonus  # Import the function to calculate baby bonus
from helper_functions.utility import check_password  # Import password check function

# Function to set up the introduction section
def setup_intro(intro):
    # Markdown explaining the Baby Bonus Scheme details
    intro.markdown(f"""
        The Baby Bonus Scheme is designed to assist parents in managing the financial costs associated with raising a child. The scheme includes two key components:
        1. Baby Bonus Cash Gift (BBCG): A cash gift provided to parents to help with early-stage child-rearing expenses.
        2. Child Development Account (CDA) benefits, which offer:
            - A First Step Grant to kickstart the child's savings.
            - Government co-matching of parents’ contributions to the CDA, helping to grow the savings further for the child’s developmental needs.

        In 2023, the scheme was enhanced to provide greater benefits for families, specifically for children born on or after 14 February 2023, making it even more beneficial for new parents.
    """)
    intro.subheader("Calculate the baby bonus that you can receive!")  # Subtitle for the calculation form

# Function to set up the input form for user data and display results
def setup_form(input, result):
    # Section to collect birth information
    input.subheader("Birth Information")
    col1, col2 = input.columns(2)  # Create two columns for birth information
    birth_order = col1.number_input(label="Birth Order", min_value=1, step=1)  # User inputs birth order
    birth_date = col2.date_input(label="Birth Date")  # User inputs birth date

    # Section to collect information on CDA government co-matching
    input.subheader("Saving for CDA Government Co-matching")
    col1, col2, col3 = input.columns(3)  # Create three columns for saving details
    cda_saving_amount = col1.number_input(label="Amount ($)", value=0, min_value=0, step=100)  # User inputs saving amount
    cda_saving_date = col2.date_input(label="Date")  # User inputs saving date
    cda_saving_occurrence = col3.selectbox("Occurrence", ("One time", "Yearly", "Monthly", "Weekly", "Daily"))  # Select saving frequency

    # Section for calculating results
    input.subheader("Calculate")
    as_of = input.date_input(label="Baby Bonus received as of")  # User inputs date for bonus received calculation
    submitted = input.form_submit_button("Calculate")  # Button to submit form and trigger calculation

    # If form is submitted, calculate the Baby Bonus and CDA using the input values
    if submitted:
        bbcg, cda = calculate_baby_bonus(
            birth_order=birth_order, birth_date=birth_date, 
            cda_saving_amount=cda_saving_amount, cda_saving_date=cda_saving_date, cda_saving_occurrence=cda_saving_occurrence,
            as_of=as_of
        )  
        # Update the results in the result container
        update_result(result, bbcg, cda)                  

# Function to update and display the results
def update_result(result, bbcg, cda):
    # Display Baby Bonus Cash Gift (BBCG) details
    result.subheader("Baby Bonus Cash Gift (BBCG)")
    result.html(bbcg["Overview"])  # Overview of the BBCG scheme
    bbcg_timeline = pd.DataFrame(bbcg["Timeline"])  # Convert BBCG timeline into a DataFrame
    bbcg_timeline.set_index("Date", inplace=True)  # Set the date as the index
    bbcg_timeline['Amount'] = bbcg_timeline['Amount'].apply(lambda x: f"${x:,.0f}")  # Format the amount values
    result.dataframe(bbcg_timeline)  # Display the BBCG timeline as a table
    result.write(f"Total amount: ${bbcg['Total Amount']:,.0f}")  # Display total BBCG amount
    result.html(bbcg["Summary"])  # Display a summary of the BBCG

    # Display Child Development Account (CDA) details
    result.subheader("Child Development Account (CDA)")
    result.html(cda["Overview"])  # Overview of the CDA scheme
    cda_timeline = pd.DataFrame(cda["Timeline"]).reset_index(drop=True)  # Convert CDA timeline into a DataFrame
    cda_timeline.set_index("Date", inplace=True)  # Set the date as the index
    cda_timeline['Amount'] = cda_timeline['Amount'].apply(lambda x: f"${x:,.0f}")  # Format the amount values
    result.dataframe(cda_timeline)  # Display the CDA timeline as a table
    result.write(f"Total Personal Saving: ${cda['Total Personal Saving']:,.0f}")  # Display total personal savings
    result.write(f"Total Government Contribution: ${cda['Total Government Contribution']:,.0f}")  # Display total government contribution
    result.write(f"Total CDA Amount: ${cda['Total CDA Amount']:,.0f}")  # Display total CDA amount
    result.html(cda["Summary"])  # Display a summary of the CDA

# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="Baby Benefits Calculator"
)
# endregion <--------- Streamlit App Configuration --------->

# Display app title
st.title("👶 Baby Bonus Calculator")

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