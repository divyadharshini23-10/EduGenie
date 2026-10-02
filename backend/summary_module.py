from google import genai
import os

client = genai.Client(
    api_key=os.environ.get("GEMINI_API_KEY")
)


def summarize_text(text):
    prompt = f"""
    Summarize the following text clearly and concisely.

    Keep the important information.
    Remove unnecessary repetition.
    Use simple and easy-to-understand English.

    Text:
    {text}
    """

    response = client.models.generate_content(
        model="gemini-3.7-flash",
        contents=prompt
    )

    return response.text