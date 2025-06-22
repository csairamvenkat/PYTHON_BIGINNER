import streamlit as st
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

# Or use OpenAI
# from langchain.chat_models import ChatOpenAI

# Create the translation prompt
template = """
Translate the following text from {source_lang} to {target_lang}:

Text: "{text}"

Translation:
"""

prompt = PromptTemplate(
    input_variables=["source_lang", "target_lang", "text"],
    template=template,
)
key = "AIzaSyAnZEfDI7xQGvJCchJXaN95lP0XXtxAqY0" 
# Initialize LLM
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.3, google_api_key=key)
# For OpenAI:
# llm = ChatOpenAI(model_name="gpt-3.5-turbo")

chain = LLMChain(llm=llm, prompt=prompt)

# Streamlit UI
st.title("🌍 Language Translator using LangChain")
text = st.text_area("Enter text to translate:")
source_lang = st.selectbox("Source Language", ["English", "Spanish", "French", "Hindi", "German"])
target_lang = st.selectbox("Target Language", ["English", "Spanish", "French", "Hindi", "German"])

if st.button("Translate"):
    if text and source_lang and target_lang:
        with st.spinner("Translating..."):
            result = chain.run(source_lang=source_lang, target_lang=target_lang, text=text)
        st.success("Translation Completed:")
        st.write(result)
    else:
        st.warning("Please fill all the fields.")
