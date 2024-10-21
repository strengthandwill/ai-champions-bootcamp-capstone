import os
import json
import openai
from helper_functions import llm

# Load the MD file
def read_file(filepath):
    with open(filepath, 'r') as file:
        return file.read()

def calculate_preschool_subsidies(
        father_gross_monthly_income, mother_gross_monthly_income, mother_working_status,
        baby_birth_date, baby_citizenship,
        as_of):    
    delimiter = "####"

    system_message = f"""
        Follow the steps below to address customer queries. The customer query will be enclosed within a pair of {delimiter}.

        Step 1: Review the provided information on Singapore's Preschool Subsidies:
        {preschool_subsidies_info}

        Step 2: Review the enrollment fees of the following preschools:
        - **PCF Sparkletots**: {pcf}
        - **My First Skool**: {myfirstskool}
        - **My World Preschool**: {myworldpreschool}
        - **Skool4Kidz**: {skool4kidz}
        - **E-Bridge Preschool**: {ebridgepreschool}

        Step 3: Based on the customer's query, calculate the following:
        - **Household Income**:
          - Gross Monthly Household Income
          - Gross Monthly Per Capita Income (PCI)
        - **Baby Details**:
          - Baby's Age as of {as_of}
          - Preschool Programme: Full-Day Infant Care / Full-Day Childcare / Kindergarten
        - **Subsidies**:
          - Basic and Additional Subsidies (as applicable)
        - **Enrollment Fees (with and without subsidies)** for:
          - PCF Sparkletots
          - My First Skool
          - My World Preschool
          - Skool4Kidz
          - E-Bridge Preschool

        Step 4: {delimiter}
        Generate a dictionary object containing the data from Step 3. Ensure the response includes only the dictionary object, without any enclosing tags or delimiters. The structure should be as follows:

        - Household Income:
            - Overview: A detailed paragraph summarizing the income calculations.
            - Gross Monthly Household Income
            - Gross Monthly Per Capita Income
            - Summary: A concise summary of household income and calculations.
        - Baby Details:
            - Baby Age: As of {as_of}
            - Preschool Programme
            - Summary: A paragraph summarizing baby details and the chosen preschool programme.
        - Subsidies:
            - Basic Subsidy: If applicable
            - Additional Subsidy: If applicable
            - Max KiFAS: If applicable
            - Summary: A paragraph summarizing the subsidies.
        - Enrollment Fees:
            - Overview: A comprehensive paragraph summarizing the fee calculations.
            - Preschools:
                - PCF Sparkletots
                    - With Subsidies
                    - Without Subsidies
                - My First Skool
                    - With Subsidies
                    - Without Subsidies                
                - My World Preschool
                    - With Subsidies
                    - Without Subsidies                                
                - Skool4Kidz
                    - With Subsidies
                    - Without Subsidies                                
                - E-Bridge Preschool
                    - With Subsidies
                    - Without Subsidies                                
            - Summary: A paragraph summarizing the enrollment fees and calculations. 

        Response Format:
        Step 1: <Detailed explanation based on subsidy information>  
        Step 2: <Explanation of enrollment fees with relevant comparisons>  
        Step 3: <Presentation of calculations and final responses>  
        Step 4: {delimiter} <Structured dictionary object> 
    """

    print(system_message)

    user_message = f"""
        The customer has provided the following details:
        - Father's monthly income: {father_gross_monthly_income}
        - Mother's monthly per capita income: {mother_gross_monthly_income}
        - Mother's employment status: {mother_working_status}
        - Baby's birth date: {baby_birth_date}
        - Baby's citizenship: {baby_citizenship}
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
    
    response_str = response_str.split(delimiter)[-1]    
    dict = json.loads(response_str)

    return dict["Household Income"], dict["Baby Details"], dict["Subsidies"], dict["Enrollment Fees"]

preschool_subsidies_info = read_file('./data/preschool-subsidies.md')
pcf = read_file('./data/pcf.md')
myfirstskool = read_file('./data/myfirstskool.md')
myworldpreschool = read_file('./data/myworldpreschool.md')
skool4kidz = read_file('./data/skool4kidz.md')
ebridgepreschool = read_file('./data/ebridgepreschool.md')