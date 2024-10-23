import streamlit as st  # Import Streamlit for creating the app interface
import pandas as pd  # Import pandas for data manipulation and display
from logics.baby_bonus_query_handler import calculate_baby_bonus  # Import the function to calculate baby bonus details
from helper_functions.utility import check_password  # Import the function for checking password protection

# Function to set up the introductory section explaining the Baby Bonus Scheme
def setup_intro(intro):
    # Display information about the Baby Bonus Scheme, including the cash gift and CDA benefits
    intro.markdown(f"""
        The Baby Bonus Scheme is designed to assist parents in managing the financial costs associated with raising a child. The scheme includes two key components:
        1. Baby Bonus Cash Gift (BBCG): A cash gift provided to parents to help with early-stage child-rearing expenses.
        2. Child Development Account (CDA) benefits, which offer:
            - A First Step Grant to kickstart the child's savings.
            - Government co-matching of parents’ contributions to the CDA, helping to grow the savings further for the child’s developmental needs.

        In 2023, the scheme was enhanced to provide greater benefits for families, specifically for children born on or after 14 February 2023, making it even more beneficial for new parents.
    """)
    intro.subheader("Calculate the baby bonus that you can receive!")  # Subtitle for the section

# Function to set up the input form for user data and handle form submissions
def setup_form(input, result):
    # Section for entering birth-related information
    input.subheader("Birth Information")
    col1, col2 = input.columns(2)  # Create two columns for user inputs
    birth_order = col1.number_input(label="Birth Order", min_value=1, step=1)  # User inputs the birth order of the child
    birth_date = col2.date_input(label="Birth Date")  # User inputs the child's birth date

    # Section for entering CDA savings information
    input.subheader("Saving for CDA Government Co-matching")
    col1, col2, col3 = input.columns(3)  # Create three columns for user inputs
    cda_saving_amount = col1.number_input(label="Amount ($)", value=0, min_value=0, step=100)  # User inputs the amount saved for CDA
    cda_saving_date = col2.date_input(label="Date")  # User inputs the date of saving
    cda_saving_occurrence = col3.selectbox("Occurrence", ("One time", "Yearly", "Monthly", "Weekly", "Daily"))  # User selects the saving frequency

    # Section for calculating results
    input.subheader("Calculate")
    as_of = input.date_input(label="Baby Bonus received as of")  # User inputs the calculation date
    submitted = input.form_submit_button("Calculate")  # Button to submit the form and trigger calculation

    # When the form is submitted, calculate the Baby Bonus and CDA based on the input values
    if submitted:
        bbcg, cda = calculate_baby_bonus(
            birth_order=birth_order, birth_date=birth_date, 
            cda_saving_amount=cda_saving_amount, cda_saving_date=cda_saving_date, cda_saving_occurrence=cda_saving_occurrence,
            as_of=as_of
        )  
        # Update the result container with the calculated values
        update_result(result, bbcg, cda)                  

# Function to update and display the results in the result container
def update_result(result, bbcg, cda):
    # Section to display Baby Bonus Cash Gift (BBCG) information
    result.subheader("Baby Bonus Cash Gift (BBCG)")
    result.html(bbcg["Overview"])  # Display an overview of the BBCG scheme
    bbcg_timeline = pd.DataFrame(bbcg["Timeline"])  # Convert the timeline of BBCG payments into a pandas DataFrame
    bbcg_timeline.set_index("Date", inplace=True)  # Set the date column as the index for the timeline
    bbcg_timeline['Amount'] = bbcg_timeline['Amount'].apply(lambda x: f"${x:,.0f}")  # Format the amount as currency
    result.dataframe(bbcg_timeline)  # Display the BBCG timeline as a table
    result.write(f"Total amount: ${bbcg['Total Amount']:,.0f}")  # Display the total BBCG amount
    result.html(bbcg["Summary"])  # Display a summary of the BBCG scheme

    # Section to display Child Development Account (CDA) information
    result.subheader("Child Development Account (CDA)")
    result.html(cda["Overview"])  # Display an overview of the CDA scheme
    cda_timeline = pd.DataFrame(cda["Timeline"]).reset_index(drop=True)  # Convert the CDA timeline into a pandas DataFrame
    cda_timeline.set_index("Date", inplace=True)  # Set the date column as the index for the CDA timeline
    cda_timeline['Amount'] = cda_timeline['Amount'].apply(lambda x: f"${x:,.0f}")  # Format the amount as currency
    result.dataframe(cda_timeline)  # Display the CDA timeline as a table
    result.write(f"Total Personal Saving: ${cda['Total Personal Saving']:,.0f}")  # Display the total personal savings in the CDA
    result.write(f"Total Government Contribution: ${cda['Total Government Contribution']:,.0f}")  # Display the total government contribution
    result.write(f"Total CDA Amount: ${cda['Total CDA Amount']:,.0f}")  # Display the total amount in the CDA
    result.html(cda["Summary"])  # Display a summary of the CDA scheme

# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",  # Center the layout for better display on the page
    page_title="Baby Benefits Calculator"  # Set the page title
)
# endregion <--------- Streamlit App Configuration --------->

# Display the main title of the app
st.title("👶 Baby Bonus Calculator")

# Use password protection to check if the user is authorized to access the app
if not check_password():  
    st.stop()  # Stop the app if the password is incorrect

# Create containers for the introduction, input form, and results
intro = st.container()
input = st.form('form')
result = st.container(border=True)

# Set up the introduction and input form
setup_intro(intro)
setup_form(input, result)