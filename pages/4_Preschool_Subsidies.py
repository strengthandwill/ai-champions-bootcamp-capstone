import streamlit as st
import pandas as pd
from logics.preschool_subsidies_query_handler import calculate_preschool_subsidies
from helper_functions.utility import check_password

def setup_intro(intro):
    # intro.markdown(f"""
    #     The Baby Bonus Scheme helps you manage the costs of raising a child. It consists of:            
    #     *   (i) Baby Bonus Cash Gift (BBCG) and    
    #     *   (ii) Child Development Account (CDA) benefits, including the First Step Grant and Government co-matching of parents’ savings.    

    #     The scheme was enhanced in 2023 for eligible children born on or after 14 Feb 2023.
    # """)
    # intro.subheader("Calculate the baby bonus that you can receive!")
    return

def setup_form(input, result):
    input.subheader("Current CPF Special Account (SA)")
    col1, col2 = input.columns(2)
    current_amount = col1.number_input(label="Amount ($)", min_value=0, step=100)
    current_date = col2.date_input(label="Date")
    
    input.subheader("Saving Plan")
    col1, col2, col3 = input.columns(3)
    saving_amount = col1.number_input(label="Amount ($)", value=0, min_value=0, step=100)
    saving_start_date = col2.date_input(label="Start Date")
    saving_occurrence = col3.selectbox("Occurrence", ("One time", "Yearly", "Monthly", "Weekly", "Daily"),)

    input.subheader("Calculate")
    # as_of = input.date_input(label="Baby Bonus received as of")
    submitted = input.form_submit_button("Calculate")
    if submitted:
        result = calculate_preschool_subsidies(
            current_amount, current_date,
            saving_amount, saving_start_date, saving_occurrence
        )  
        update_result(result)                  
            

def update_result(result):
    st.write(result)
 

# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="KK Streamlit App"
)
# endregion <--------- Streamlit App Configuration --------->

st.title("CPF FRS Calculator")

# Check if the password is correct.  
# if not check_password():  
#     st.stop()

intro = st.container()
input = st.form('form')
result = st.container(border=True)

setup_intro(intro)
setup_form(input, result)