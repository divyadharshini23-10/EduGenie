from google import genai
import os

client = genai.Client(
    api_key=os.environ.get("GEMINI_API_KEY")
)


def answer_question(question):
    prompt = f"""
    Answer the following question clearly and accurately.
    Give a detailed explanation and an example if useful.

    Question: {question}
    """

    response = client.models.generate_content(
        model="gemini-3.7-flash",
        contents=prompt
    )

    return response.text