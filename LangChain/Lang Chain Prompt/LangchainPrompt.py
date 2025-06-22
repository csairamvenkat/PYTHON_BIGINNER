import streamlit as st
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import LLMChain

# Set page config
st.set_page_config(page_title="Independence Struggle Info", layout="centered")

st.title("Independence Struggle Explainer")
st.write("Enter a country name to learn about its independence movement.")

# Take user input
country = st.text_input("Enter Country Name", "")

# If country is entered
if country:
    # Define the prompt
    prompt_template = "Explain me about Independence struggle of {country}"
    prompt = PromptTemplate(input_variables=["country"], template=prompt_template)

    # Set your Gemini API Key
    key = "AIzaSyAnZEfDI7xQGvJCchJXaN95lP0XXtxAqY0"  # You can also use st.secrets or environment variables

    # Define the LLM
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.1, max_tokens=10000, google_api_key=key)

    # Create the chain
    chain = LLMChain(llm=llm, prompt=prompt)

    # Run the chain
    with st.spinner("Fetching details from Gemini..."):
        try:
            result = chain.run({"country": country})
            st.subheader(f"Independence Struggle of {country}")
            st.write(result)
        except Exception as e:
            st.error(f"Error: {str(e)}")

