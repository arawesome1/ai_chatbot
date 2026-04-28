import os 
from dotenv import load_dotenv
import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# 1. Load environment variables
load_dotenv()
groq_api_key = os.getenv("groq_api_key")
os.environ['langchain_api_key'] = os.getenv("langchain_api_key")
os.environ['langchain_tracing_V2'] = 'True'

# 2. Define the prompt template
prompt = ChatPromptTemplate([
    ("system", "you are a helpful ai assistant, created by Ankit and is being used in QnA Chatbot"),
    ("user", "question:{question}")
])

# 3. Enhanced generation function
def generate_response(question, engine, temperature, max_token):
    # Pass temperature and max_tokens directly to the model constructor
    llm = ChatGroq(
        groq_api_key=groq_api_key, 
        model_name=engine, 
        temperature=temperature,
        max_tokens=max_token
    )
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser
    answer = chain.invoke({'question': question})
    return answer

# 4. Streamlit UI
st.title("QnA Chatbot")

# Sidebar Configuration
# Note: Ensure these model strings are supported by your Groq account
engine = st.sidebar.selectbox("Select Model", [
    'gemma2-9b-it', 
    'llama-3.1-8b-instant', 
    'llama-3.3-70b-versatile'
])

temperature = st.sidebar.slider("Temperature", min_value=0.0, max_value=1.0, value=0.7)
max_token = st.sidebar.slider("Max Token", min_value=50, max_value=500, value=150)

st.sidebar.write("Made by Ankit")
st.sidebar.markdown("[Watch the tutorial](https://www.youtube.com/watch?v=Iv4eRB5qLtg)")

# 5. Chat Logic
st.write("Go ahead and ask your question")
user_input = st.text_input("You: ")

if user_input:
    try:
        response = generate_response(user_input, engine, temperature, max_token)
        st.write(response)
    except Exception as e:
        st.error(f"An error occurred: {e}")
else:
    st.info("Please provide user input to get started.")
