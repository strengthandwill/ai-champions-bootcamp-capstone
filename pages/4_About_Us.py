import streamlit as st

# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="My Streamlit App"
)
# endregion <--------- Streamlit App Configuration --------->

st.title("😀 About Baby Benefits Calculator")

st.markdown("""
    Welcome to the **Baby Benefits Calculator**! 🎉 
            
    This user-friendly tool is designed to empower parents and caregivers by providing an easy way to estimate the financial support available through various baby benefit schemes in Singapore.

    By harnessing the power of the OpenAI API, this app quickly calculates the benefits you could receive based on the information you provide. Whether you're a new parent or planning for the future, we've got you covered with the insights you need to make informed decisions.
""")

st.markdown("""
### How to Use the Baby Benefits Calculator            

1. **Fill in the required information** in the form. Make sure to provide accurate details to get the best results.
2. **Click the 'Calculate' button** to process your input. Sit back and relax while we do the math!
3. **Instant Results!** The calculator will promptly generate the baby benefits you may be eligible for, helping you understand your financial support options.
""")

st.markdown("""
🔗 **Explore the Source Code**: [GitHub Repository](https://github.com/strengthandwill/ai-champions-bootcamp-capstone)  
Discover how we built this tool and learn more about our project!
""")
