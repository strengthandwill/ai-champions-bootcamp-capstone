import os
import json
import openai
from helper_functions import llm

# Load the JSON file
filepath = './data/baby_bonus.md'
with open(filepath, 'r') as file:
    baby_bonus_info = file.read()    

def calculate_baby_bonus(birth_order, birth_date, as_of):    
    system_message = f"""
    You will be provided with customer service queries about Singapore's Baby Bonus Scheme.
    {baby_bonus_info}    
    """

    print(system_message)

    user_message = f"""
        Birth Order = {birth_date}
        Birth Date = {birth_date}

        Calculate Baby Bonus received as of {as_of}
    """

    print(user_message)

    messages =  [
        {'role':'system',
         'content': system_message},        
        {'role':'user',
         'content': user_message},
    ]

    response_str = llm.get_completion_by_messages(messages)
    print(response_str)    
    return response_str