import streamlit as st
import pandas as pd
from logics.baby_bonus_query_handler import calculate_baby_bonus
from helper_functions.utility import check_password

def setup_intro(intro):
    intro.markdown(f"""
        The Baby Bonus Scheme helps you manage the costs of raising a child. It consists of:            
        *   (i) Baby Bonus Cash Gift (BBCG) and    
        *   (ii) Child Development Account (CDA) benefits, including the First Step Grant and Government co-matching of parents’ savings.    

        The scheme was enhanced in 2023 for eligible children born on or after 14 Feb 2023.
    """)
    intro.subheader("Calculate the baby bonus that you can receive!")

def setup_form(input, result):
    input.subheader("Birth Information")
    col1, col2 = input.columns(2)
    birth_order = col1.number_input(label="Birth Order", min_value=1, step=1)
    birth_date = col2.date_input(label="Birth Date")
    
    input.subheader("Saving for CDA Government Co-matching")
    col1, col2, col3 = input.columns(3)
    cda_saving_amount = col1.number_input(label="Amount ($)", value=0, min_value=0, step=100)
    cda_saving_date = col2.date_input(label="Date")
    cda_saving_occurrence = col3.selectbox("Occurrence", ("One time", "Yearly", "Monthly", "Weekly", "Daily"),)

    input.subheader("Calculate")
    as_of = input.date_input(label="Baby Bonus received as of")
    submitted = input.form_submit_button("Calculate")
    if submitted:
        bbcg, cda = calculate_baby_bonus(
            birth_order=birth_order, birth_date=birth_date, 
            cda_saving_amount=cda_saving_amount, cda_saving_date=cda_saving_date, cda_saving_occurrence=cda_saving_occurrence,
            as_of=as_of)  
        update_result(result, bbcg, cda)                  
            

def update_result(result, bbcg, cda):
    result.subheader("Baby Bonus Cash Gift (BBCG)")
    result.html(bbcg["Overview"])    
    bbcg_timeline = pd.DataFrame(bbcg["Timeline"])
    bbcg_timeline.set_index("Date", inplace=True)
    bbcg_timeline['Amount'] = bbcg_timeline['Amount'].apply(lambda x: f"${x:,.0f}")
    result.dataframe(bbcg_timeline)
    result.write(f"Total amount: ${bbcg["Total Amount"]:,.0f}")
    result.html(bbcg["Summary"])        
    
    result.subheader("Child Development Account (CDA)")
    result.html(cda["Overview"])
    cda_timeline = pd.DataFrame(cda["Timeline"]).reset_index(drop=True)
    cda_timeline.set_index("Date", inplace=True)
    cda_timeline['Amount'] = cda_timeline['Amount'].apply(lambda x: f"${x:,.0f}")
    result.dataframe(cda_timeline)
    result.write(f"Total Personal Saving: ${cda["Total Personal Saving"]:,.0f}")
    result.write(f"Total Government Contribution: ${cda["Total Government Contribution"]:,.0f}")
    result.write(f"Total CDA Amount: ${cda["Total CDA Amount"]:,.0f}")
    result.html(cda["Summary"])    

# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="KK Streamlit App"
)
# endregion <--------- Streamlit App Configuration --------->

st.title("Baby Bonus Calculator")

# Check if the password is correct.  
if not check_password():  
    st.stop()

intro = st.container()
input = st.form('form')
result = st.container(border=True)

setup_intro(intro)
setup_form(input, result)