import streamlit as st
#import os
#from langchain_openai.chat_models import ChatOpenAI
from groq import Groq

st.title("My LLM App")

#openai_api_key=st.sidebar.text_input("Open API key",type="password")

groq_llama_api_key=st.secrets.api_key
client = Groq(
    api_key=groq_llama_api_key,
)

def generate_response(input_text):
   # model=ChatOpenAI(temperature=0.7,api_key=openai_api_key)
   chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": input_text ,
        }
    ],
    model="llama3-8b-8192" )

   st.info(chat_completion.choices[0].message.content)

with st.form("my_form"):
    text=st.text_area(
        "Enter text:",
        "What are the three key pieces of advice for learning how to code"
    )
    submitted =st.form_submit_button("Submit")
    if submitted:
        generate_response(text)