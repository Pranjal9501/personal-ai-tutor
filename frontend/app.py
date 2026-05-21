import streamlit as st
import requests

API_URL = "http://127.0.0.1:8001/ask"

st.set_page_config(
    page_title="Personal AI Tutor",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 Personal AI Tutor")

mode = st.sidebar.selectbox(
    "Select Learning Mode",
    ["Beginner", "Intermediate", "Advanced"]
)

st.write("Learn anything step-by-step with AI.")

# Session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
user_input = st.chat_input("Ask your question...")

if user_input:

    # Store user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    # Display user message
    with st.chat_message("user"):
        st.markdown(user_input)

    # Send request to backend
    payload = {
        "question": user_input,
        "mode" : mode,
        "chat_history": st.session_state.messages
    }

    response = requests.post(API_URL, json=payload)

    ai_response = response.json()["answer"]

    # Store AI response
    st.session_state.messages.append({
        "role": "assistant",
        "content": ai_response
    })

    # Display AI response
    with st.chat_message("assistant"):
        st.markdown(ai_response)