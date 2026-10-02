import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from explanation_module import explain_topic
from qna import answer_question
from quiz_module import generate_quiz
from summary_module import summarize_text
from learning_path import get_learning_recommendations


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {"message": "EduGenie Backend is Working!"}


@app.get("/explain")
def explain(topic: str):
    return {
        "answer": explain_topic(topic)
    }


@app.get("/qa")
def qa(question: str):
    return {
        "answer": answer_question(question)
    }


@app.get("/quiz")
def quiz(topic: str):
    return {
        "quiz": generate_quiz(topic)
    }


@app.get("/summarize")
def summarize(text: str):
    return {
        "summary": summarize_text(text)
    }


@app.get("/learn/recommendations")
def learning_recommendations(
    topic: str,
    learner_level: str = "beginner"
):
    return {
        "learning_path": get_learning_recommendations(
            topic,
            learner_level
        )
    }