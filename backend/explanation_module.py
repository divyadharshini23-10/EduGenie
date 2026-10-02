from google import genai
import os

client = genai.Client(
    api_key=os.environ.get("GEMINI_API_KEY")
)


def explain_topic(topic):
    prompt = f"""
    Explain the following topic in simple and easy English.

    The explanation should be suitable for beginners and self-learners.
    Make the explanation concise, clear, and easy to understand.

    Topic: {topic}
    """

    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents=prompt
    )

    return response.text