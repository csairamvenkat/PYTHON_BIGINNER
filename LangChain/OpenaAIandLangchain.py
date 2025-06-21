#from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.chat_models import ChatOpenAI

import streamlit as st
import os
#from dotenv import load_dotenv

os.environ["OPENAI_API_KEY"] = "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"
#os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")

## Langmith tracking
os.environ["LANGCHAIN_TRACING_V2"]="true"

os.environ["LANGCHAIN_API_KEY"]= "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"
#os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")


## Prompt Template

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","I am chatbot. I am hear to assist you. Please type your queries"),
        ("user","Question:{question}")
    ]
)

## streamlit framework

st.title('LLM-OPENAI PROJECT')
input_text=st.text_input("How may I help you")

# openAI LLm
llm=ChatOpenAI(model="gpt-4")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))