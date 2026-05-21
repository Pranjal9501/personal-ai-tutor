from google import genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Create Gemini client
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def generate_quiz(topic, difficulty):

    prompt = f"""
    You are an expert teacher and quiz generator.

    Generate a quiz on the following topic.

    Topic:
    {topic}

    Difficulty Level:
    {difficulty}

    Instructions:
    - Generate 3 Multiple Choice Questions
    - Generate 2 Short Answer Questions
    - Generate 1 Coding Question if the topic is programming related
    - For each question provide:
        1. Question
        2. Correct Answer
        3. Explanation
    - Keep explanations beginner friendly
    - Format the response clearly using headings and bullet points
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text