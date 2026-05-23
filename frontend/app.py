import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:8001"

st.set_page_config(
    page_title="Personal AI Tutor",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 Personal AI Tutor")

st.write("Learn anything step-by-step with AI.")

# Learning Mode
mode = st.sidebar.selectbox(
    "Select Learning Mode",
    ["Beginner", "Intermediate", "Advanced"]
)

# QUIZ GENERATOR
st.sidebar.header("Quiz Generator")

quiz_topic = st.sidebar.text_input(
    "Quiz Topic"
)

quiz_difficulty = st.sidebar.selectbox(
    "Quiz Difficulty",
    ["Beginner", "Intermediate", "Advanced"]
)

if st.sidebar.button("Generate Quiz"):

    quiz_payload = {
        "topic": quiz_topic,
        "difficulty": quiz_difficulty
    }

    try:

        quiz_response = requests.post(
            f"{BASE_URL}/quiz",
            json=quiz_payload
        )

        if quiz_response.status_code == 200:

            quiz_data = quiz_response.json()["quiz"]

            # Save quiz in session state
            st.session_state.generated_quiz = quiz_data

            st.subheader("📝 Generated Quiz")

            st.write(quiz_data)

        else:
            st.error(quiz_response.text)

    except Exception as e:
        st.error(f"Quiz Error: {str(e)}")


# ANSWER EVALUATION

st.sidebar.header("Answer Evaluation")

student_answer = st.sidebar.text_area(
    "Your Answer"
)

if st.sidebar.button("Evaluate Answer"):

    if "generated_quiz" not in st.session_state:

        st.error("Please generate a quiz first.")

    else:

        evaluation_payload = {
            "question": st.session_state.generated_quiz,
            "student_answer": student_answer
        }

        try:

            evaluation_response = requests.post(
                f"{BASE_URL}/evaluate",
                json=evaluation_payload
            )

            if evaluation_response.status_code == 200:

                evaluation_result = evaluation_response.json()["evaluation"]

                st.subheader("📊 Evaluation Result")

                st.write(evaluation_result)

            else:
                st.error(evaluation_response.text)

        except Exception as e:
            st.error(f"Evaluation Error: {str(e)}")


# CHAT MEMORY

if "messages" not in st.session_state:
    st.session_state.messages = []


for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])


user_input = st.chat_input(
    "Ask your question..."
)

if user_input:

    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.markdown(user_input)

    payload = {
        "question": user_input,
        "mode": mode,
        "chat_history": st.session_state.messages
    }

    try:

        response = requests.post(
            f"{BASE_URL}/ask",
            json=payload
        )

        if response.status_code == 200:

            ai_response = response.json()["answer"]

        else:
            ai_response = response.text

    except Exception as e:

        ai_response = f"Connection Error: {str(e)}"

    st.session_state.messages.append({
        "role": "assistant",
        "content": ai_response
    })


    with st.chat_message("assistant"):
        st.markdown(ai_response)