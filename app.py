import os 
from dotenv import load_dotenv
load_dotenv()
groq_api_key = os.getenv("groq_api_key")
os.environ['langchain_api_key']= os.getenv("langchain_api_key")
os.environ['langchain_tracing_V2']='True'
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st

prompt = ChatPromptTemplate([
    ("system","you are a helpful ai assistant"),
    ("user","question:{question}")
])

def generate_response(question,engine,temperature,max_token):
    llm = ChatGroq(groq_api_key=groq_api_key, model = engine)
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser
    answer = chain.invoke({'question': question})
    return answer


st.title("QnA Chatbot")
engine=st.sidebar.selectbox("Select Model",['gemma2-9b-it','lama3-groq-70b-8192-tool-use-preview','mixtral-8x7b-32768','llava-v1.5-7b-4096-preview'])
temperature = st.sidebar.slider("Temperature",min_value=0.0, max_value=1.0,value=0.7)
max_token = st.sidebar.slider("Max Token",min_value=50, max_value=300, value = 150)

st.sidebar.write("Made by Ankit")
st.sidebar.write("This is just an AI interfernce, without VectorStoreDB or RAG Supported")
st.write("Go ahead and ask your question")
user_input = st.text_input("You: ")
if user_input:
    response = generate_response(user_input,engine,temperature,max_token)
    st.write(response)
else:
    st.write("Please provide user input")
