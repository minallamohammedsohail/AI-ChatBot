from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#loading gemini pro model and getting response
model=genai.GenerativeModel("gemini-pro")
chat=model.start_chat(history=[])

def get_gemini_response(question):
    response=chat.send_message(question,stream=True)
    return response

#Initializing Streamlit app
st.set_page_config(page_title="E-ATS")
st.header("Enhanced Applicant Tracking System")

#Chat History configuration
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

#input and submit button
input=st.text_input("Input:",key="input")
submit=st.button("Submit")

if submit and input:
    response=get_gemini_response(input)
    # saving user query to chat history
    st.session_state['chat_history'].append(("You",input))
    st.subheader("ChatBot:")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("ChatBot",chunk.text))
st.subheader("Chat History")      

for role,text in st.session_state['chat_history']:
    st.write(f"{role}:{text}")
