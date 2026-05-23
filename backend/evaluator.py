from google import genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Create Gemini client
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def evaluate_answer(question, student_answer):

    prompt = f"""
    You are an expert teacher and evaluator.

    Evaluate the student's answer carefully.

    Question:
    {question}

    Student Answer:
    {student_answer}

    Provide the following:

    1. Score out of 10
    2. Correctness Analysis
    3. Mistakes in the Answer
    4. Suggestions for Improvement
    5. Reference/Ideal Answer

    Instructions:
    - Be educational and encouraging
    - Explain mistakes clearly
    - Use beginner-friendly language
    - Give constructive feedback
    - Format the response using headings and bullet points
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text