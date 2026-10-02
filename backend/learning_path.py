from google import genai
import os

client = genai.Client(
    api_key=os.environ.get("GEMINI_API_KEY")
)


def get_learning_recommendations(topic, learner_level="beginner"):
    prompt = f"""
    Create a personalized learning path for the following topic.

    Learner level: {learner_level}
    Topic: {topic}

    Include:
    1. Beginner concepts
    2. Intermediate concepts
    3. Advanced concepts
    4. Useful learning resources such as videos, articles, or books
    5. Practice activities
    6. A simple final project idea

    Organize the learning path clearly according to difficulty.
    """

    try:
        response = client.models.generate_content(
            model="gemini-3.7-flash",
            contents=prompt
        )

        return response.text

    except Exception as error:
        return {
            "error": f"Learning path generation failed: {str(error)}"
        }