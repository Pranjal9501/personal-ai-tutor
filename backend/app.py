from fastapi import FastAPI
from pydantic import BaseModel
from tutor import ask_tutor

app = FastAPI()


class QuestionRequest(BaseModel):
    question: str
    mode: str


@app.get("/")
def home():
    return {"message": "Personal AI Tutor Backend Running"}


@app.post("/ask")
def ask_question(request: QuestionRequest):

    response = ask_tutor(request.question, request.mode)

    return {
        "question": request.question,
        "answer": response
    }