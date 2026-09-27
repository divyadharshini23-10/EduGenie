import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from google import genai

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

@app.get("/")
def home():
    return {"message": "EduGenie Backend is Working!"}

@app.get("/ask")
def ask(question: str, task: str = "explain"):

    if task == "explain":
        prompt = f"""
        Explain this topic in detail using simple English.
        Use headings, examples, and important points.
        Topic: {question}
        """

    elif task == "qna":
        prompt = f"""
        Answer this question clearly and accurately.
        Give a detailed explanation with an example if useful.
        Question: {question}
        """

    elif task == "quiz":
        prompt = f"""
        Create 5 multiple-choice quiz questions about this topic.
        Give 4 options for each question and show the correct answer
        with a short explanation.
        Topic: {question}
        """

    elif task == "summary":
        prompt = f"""
        Give a clear and easy-to-understand summary of this topic.
        Include the most important points.
        Topic: {question}
        """

    elif task == "recommend":
        prompt = f"""
        Create a step-by-step learning path for this topic.
        Include what to learn first, next topics, useful practice,
        and a simple final project idea.
        Topic: {question}
        """

    else:
        prompt = question

    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents=prompt
    )

    return {"answer": response.text}