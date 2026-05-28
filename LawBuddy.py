from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from dotenv import load_dotenv
import streamlit as st
import os
import json
from prompt_template import prompt

load_dotenv()

llm= HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="conversational",
    temperature=0.7
)
model= ChatHuggingFace(llm=llm)

history= "chat_history.json"
if os.path.exists(history):
    with open(history, "r") as f:
        chat_history= json.load(f)
else:
    chat_history= []

st.title("Legal Document Chatbot")
uinput= st.text_area("Paste your legal document query:")
if st.button("send") and uinput.strip():
    format_prompt= prompt.format(uinput= uinput, chat_history= chat_history)

    messages=[
        HumanMessage(content= format_prompt)
    ]
    result= model.invoke(messages)

    chat_history.append({"role": "human", "content": uinput})
    chat_history.append({"role": "assistant", "content": result.content})
    with open(history, "w") as f:
        json.dump(chat_history, f, indent=4)

    st.write("Chatbot Response:", result.content)