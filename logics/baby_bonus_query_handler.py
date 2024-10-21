import os
import json
import openai
from helper_functions import llm

# Load the MD file
filepath = './data/baby_bonus.md'
with open(filepath, 'r') as file:
    baby_bonus_info = file.read()    

def calculate_baby_bonus(
        birth_order, birth_date, 
        cda_saving_amount, cda_saving_date, cda_saving_occurrence,
        as_of):    
    delimiter = "####"

    system_message = f"""
        Follow the steps below to address customer queries. The customer query will be enclosed within a pair of {delimiter}.

        Step 1:
        Review and understand the information on Singapore's Baby Bonus Scheme provided below:
        {baby_bonus_info}

        Step 2:
        Generate two timelines up until {as_of}:
        1) A timeline for the Baby Bonus Cash Gift (BBCG).
        Calculate the total amount of cash gifts disbursed by {as_of}.
        2) A timeline for personal savings and the government’s contribution (First Step Grant + Government Co-matching) to the Child Development Account (CDA).
        Calculate both the personal savings and government contributions up until {as_of}.

        Step 3:
        Provide a summary of the calculations and results from Step 2.

        Step 4: {delimiter}        
        Generate a dictionary object containing the data from Step 2 and Step 3. Ensure the response includes only the dictionary object, without any enclosing tags or delimiters. The structure should be as follows:
        - BBCG:
            - Overview: A paragraph-long overview of the calculations.
            - Timeline:
                - Date
                - Amount
            - Total Amount
            - Summary: A paragraph summarizing the timeline and total amount.
        - CDA:
            - Overview: A paragraph-long overview of the calculations.
            - Timeline:
                - Date
                - Event Type: First Step Grant / Personal Saving / Government Co-matching
                - Amount
            - Total Personal Saving
            - Total Government Contribution
            - Total CDA Amount
            - Summary: A paragraph summarizing the timeline and total amounts.

        Response Format:
        Step 1: <Step 1 explanation and reasoning>
        Step 2: <Step 2 response with BBCG timeline and calculations>
        Step 3: <Step 3 response with CDA timeline and calculations>
        Step 4: {delimiter} <Step 4 dictionary object>
    """

    print(system_message)

    user_message = f"""
        - The child's birth order is {birth_order}
        - The birth date is {birth_date}
        - An amount of {cda_saving_amount} is saved into the Child Development Account (CDA) {cda_saving_occurrence} starting on {cda_saving_date}.
    """

    print(user_message)

    messages =  [
        {'role':'system',
         'content': system_message},        
        {'role':'user',
         'content': f"{delimiter}{user_message}{delimiter}"},
    ]

    response_str = llm.get_completion_by_messages(messages)
    response_str = response_str.split(delimiter)[-1]    
    dict = json.loads(response_str)    
    return dict["BBCG"], dict["CDA"]