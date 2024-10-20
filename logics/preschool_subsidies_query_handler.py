import os
import json
import openai
from helper_functions import llm

# Load the MD file
filepath = './data/preschool-subsidies.md'
with open(filepath, 'r') as file:
    frs_info = file.read()    

def calculate_preschool_subsidies(
        current_amount, current_date,
        saving_amount, saving_start_date, saving_occurrence):    
    delimiter = "####"

    system_message = f"""
        The customer query will be enclosed within a pair of {delimiter}. Please follow the steps below to address it:

        Step 1:
        Review the information below on Singapore's CPF Full Retirement Sum (FRS) and how it impacts retirement savings and payouts.
        {frs_info}

        Step 2:
        - Create a timeline showing the projected growth of the customer’s Special Account (SA) savings.
        - Identify the date when the Full Retirement Sum (FRS) will be reached, based on the customer’s SA balance and savings contributions.
        - Calculate the CPF LIFE payout once the FRS is reached and CPF LIFE is activated.

        Response Format:
        Step 1: <Summary of the CPF Full Retirement Sum and its implications on savings and payouts>
        Step 2: <Detailed timeline of SA growth, FRS achievement date, and CPF LIFE payout estimate>     
    """

    print(system_message)

    user_message = f"""
        - The current Special Account balance is {current_amount} as of {current_date}.
        - {saving_amount} is contributed to the Special Account {saving_occurrence}, starting on {saving_start_date}.
    """

    print(user_message)

    messages =  [
        {'role':'system',
         'content': system_message},        
        {'role':'user',
         'content': f"{delimiter}{user_message}{delimiter}"},
    ]

    response_str = llm.get_completion_by_messages(messages)

    print(response_str)
    
    # response_str = response_str.split(delimiter)[-1]    
    # dict = json.loads(response_str)    
    return response_str