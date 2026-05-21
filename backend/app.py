from fastapi import FastAPI
from pydantic import BaseModel
from tutor import ask_tutor
from typing import List
from quiz_generator import generate_quiz


app = FastAPI()


class QuestionRequest(BaseModel):
    question: str
    mode: str
    chat_history: List[dict]


class QuizRequest(BaseModel):
    topic: str
    difficulty: str


@app.get("/")
def home():
    return {"message": "Personal AI Tutor Backend Running"}


@app.post("/ask")
def ask_question(request: QuestionRequest):

    response = ask_tutor(request.question,
                          request.mode,
                          request.chat_history
                          )

    return {
        "question": request.question,
        "answer": response
    }


@app.post("/quiz")
def create_quiz(request: QuizRequest):

    quiz = generate_quiz(
        request.topic,
        request.difficulty
    )

    return {
        "topic": request.topic,
        "quiz": quiz
    }