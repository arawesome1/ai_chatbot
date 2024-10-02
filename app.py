import os 
from dotenv import load_dotenv
load_dotenv()
os.environ['langchain_api_key']= os.getenv("langchain_api_key")
os.environ['langchain_tracing_V2']='True'
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st

prompt = ChatPromptTemplate([
    ("system","you are a helpful ai assistant"),
    ("user","question:{question}")
])

def generate_response(question,engine,temperature,max_token):
    llm = Ollama(model = engine)
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser
    answer = chain.invoke({'question': question})
    return answer

st.title("QnA Chatbot")
engine=st.sidebar.selectbox("Select Model",['mistral','llama3.2','gemma2','phi3'])
temperature = st.sidebar.slider("Temperature",min_value=0.0, max_value=1.0,value=0.7)
max_token = st.sidebar.slider("Max Token",min_value=50, max_value=300, value = 150)

st.sidebar.write("Made by Ankit")
st.write("Go ahead and ask your question")
user_input = st.text_input("You: ")
if user_input:
    response = generate_response(user_input,engine,temperature,max_token)
    st.write(response)
else:
    st.write("Please provide user input")
