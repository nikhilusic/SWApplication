from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os 
from  dotenv import load_dotenv
os.environ["LANGCHAIN_TRACKING_V2"]="true"
os.environ["LANGCHAIN_API_Key"]=os.getenv("LANGCHAIN_API_Key")

##prmot template

prompt=ChatPromptTemplate.from_message (
    [ 
     ("system"," you are a helpful assistant. Pleasse respond to the user query")
     
     ("user", "Question: {Question}")
     
     ]
)

##streamlit framework
st.title ('My name is Nikhil')
input_text=st.tect_input("Search the topic")

#openAI LLM
llm=ChatOpenAI(model="gpt-3.5-turbo")
output_parser=StrOutPutParser
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))
