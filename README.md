###Groq-Powered QnA Chatbot
This repository hosts a simple yet powerful QnA chatbot built using Groq and LangChain, allowing users to interact with AI models in real-time without relying on external databases or Retrieval-Augmented Generation (RAG). The chatbot is designed to provide quick, accurate responses purely from the built-in AI models. With a user-friendly interface and adjustable settings, this project showcases the capabilities of various language models.

##Key Features:
Multiple AI Models: Choose from several powerful models like gemma2-9b-it, lama3-groq-70b, and more, each offering unique response styles.
Real-Time QnA: Ask questions and get answers immediately, without using external knowledge bases or RAG.
Customizable: Easily adjust the temperature and max tokens to fine-tune the chatbot's response behavior.
User-Friendly Interface: Built with Streamlit for an intuitive and easy-to-use experience.
AI Only: The chatbot operates solely on the AI model's knowledge, making it a unique solution for those who want an AI-powered assistant without external dependencies like VectorStoreDB.
##Tech Stack:
Groq: For AI model execution and high-speed inference.
LangChain: To handle prompt templates and chatbot flows.
Streamlit: Provides a clean, web-based interface for the chatbot.
Python-Dotenv: Manages environment variables for secure API key storage.

Setup Instructions:
Clone this repository:
git clone https://github.com/your-username/qna-groq-chatbot.git
cd qna-groq-chatbot

Install the required dependencies:
pip install -r requirements.txt

Set up your environment variables:

Add your Groq and LangChain API keys to a .env file.
groq_api_key=your_groq_api_key
langchain_api_key=your_langchain_api_key

Run the Streamlit app:
streamlit run app.py

Interact with the chatbot on the locally hosted web interface!

Usage:
Choose your preferred language model from the sidebar.
Adjust the temperature (0.0 - 1.0) to control the creativity of the model's responses.
Set a token limit to manage the response length.
Type your question into the input box, and the chatbot will generate an immediate answer!
Example Models:
gemma2-9b-it: Ideal for general queries and robust question answering.
lama3-groq-70b: Handles more complex or nuanced queries.
mixtral-8x7b: Known for generating structured and detailed responses.
Contributions:
This project is open for contributions! Feel free to submit pull requests, report issues, or suggest improvements.
