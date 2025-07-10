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
    ("system","you are a helpful ai assistant, created by Ankit and is being used in QnA Chatbot"),
    ("user","question:{question}")
])

def generate_response(question,engine,temperature,max_token):
    llm = ChatGroq(groq_api_key=groq_api_key, model = engine)
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser
    answer = chain.invoke({'question': question})
    return answer


st.title("QnA Chatbot")
engine=st.sidebar.selectbox("Select Model",['gemma2-9b-it','llama-3.1-8b-instant','playai-tts','qwen/qwen3-32b'])
temperature = st.sidebar.slider("Temperature",min_value=0.0, max_value=1.0,value=0.7)
max_token = st.sidebar.slider("Max Token",min_value=50, max_value=300, value = 150)

st.sidebar.write("Made by Ankit")
st.sidebar.write("This is just an AI interfernce, without VectorStoreDB or RAG Supported. **Updated till 2023 dataset.**")
st.sidebar.markdown("""
**Want to know how this chatbot was built?**  
[Click here to watch the video](https://www.youtube.com/watch?v=Iv4eRB5qLtg)
""")

st.write("Go ahead and ask your question")
user_input = st.text_input("You: ")

if user_input:
    response = generate_response(user_input,engine,temperature,max_token)
    st.write(response)
else:
    st.write("Please provide user input")
    st.markdown("""
This AI-powered chatbot answers your questions in real-time using advanced language models. Unlike other chatbots, it **does not use Retrieval-Augmented Generation (RAG)** or external databases like vector stores. Everything is generated purely from the AI's built-in knowledge.

### Key Features:
- **Direct answers** without external data sources.
- Choose from multiple AI models like **gemma2-9b-it**, **llama-3.1-8b-instant**, and more.
- Adjustable **temperature** and **token limits** for fine-tuning responses.
- User-friendly interface with quick response times.
""")
