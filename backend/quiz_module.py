from google import genai
import os
import json
import re

client = genai.Client(
    api_key=os.environ.get("GEMINI_API_KEY")
)


def clean_json_block(text):
    text = text.strip()

    text = re.sub(r"^```json\s*", "", text)
    text = re.sub(r"^```\s*", "", text)
    text = re.sub(r"\s*```$", "", text)

    return text.strip()


def generate_quiz(topic):
    prompt = f"""
    Create 3 multiple-choice questions about the following topic.

    Requirements:
    - Each question must have 4 options.
    - Include the correct answer.
    - Return ONLY valid JSON.
    - Do not include Markdown or ```.

    Use this JSON format:

    [
        {{
            "question": "Question text",
            "options": [
                "Option A",
                "Option B",
                "Option C",
                "Option D"
            ],
            "answer": "Correct option"
        }}
    ]

    Topic: {topic}
    """

    try:
        response = client.models.generate_content(
            model="gemini-3.7-flash",
            contents=prompt
        )

        cleaned_response = clean_json_block(response.text)
        quiz = json.loads(cleaned_response)

        return quiz

    except Exception as error:
        return {
            "error": f"Quiz generation failed: {str(error)}"
        }