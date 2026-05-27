import os
from dotenv import load_dotenv
import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")

os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY", "")
os.environ["LANGCHAIN_TRACING_V2"] = "true"

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI assistant, created by Ankit and used in a QnA chatbot."),
    ("user", "question: {question}")
])

def generate_response(question, engine, temperature, max_token):
    llm = ChatGroq(
        api_key=groq_api_key,
        model=engine,
        temperature=temperature,
        max_tokens=max_token
    )
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser
    answer = chain.invoke({"question": question})
    return answer

st.title("QnA Chatbot")

engine = st.sidebar.selectbox("Select Model", [
    "gemma2-9b-it",
    "llama-3.1-8b-instant",
    "llama-3.3-70b-versatile"
])

temperature = st.sidebar.slider("Temperature", 0.0, 1.0, 0.7)
max_token = st.sidebar.slider("Max Token", 50, 500, 150)

st.sidebar.write("Made by Ankit")
st.sidebar.markdown("[Watch the tutorial](https://www.youtube.com/watch?v=Iv4eRB5qLtg)")

st.write("Go ahead and ask your question")
user_input = st.text_input("You: ")

if user_input:
    try:
        if not groq_api_key:
            st.error("GROQ_API_KEY not found in .env file")
        else:
            response = generate_response(user_input, engine, temperature, max_token)
            st.write(response)
    except Exception as e:
        st.error(f"An error occurred: {e}")
else:
    st.info("Please provide user input to get started.")

