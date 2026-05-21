from google import genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Create Gemini client
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def get_mode_instruction(mode):

    if mode == "Beginner":
        return """
        Explain in very simple language.
        Use analogies and easy examples.
        Avoid difficult terminology.
        Teach slowly step-by-step.
        """

    elif mode == "Intermediate":
        return """
        Explain clearly with examples.
        Include technical concepts where needed.
        Add practical understanding.
        """

    else:
        return """
        Give deep technical explanations.
        Include advanced concepts.
        Include optimization and best practices.
        """

def ask_tutor(question,mode,chat_history):

    mode_instruction = get_mode_instruction(mode)

    conversation = ""

    for msg in chat_history:

        role = msg["role"]
        content = msg["content"]

        conversation += f"{role}: {content}\n"

    prompt = f"""
    You are an expert AI tutor.

    {mode_instruction}

    Previous Conversation:
    {conversation}

    Teaching Rules:
    1. Teach step-by-step
    2. Maintain continuity
    3. Use examples
    4. Ask follow-up questions
    5. Encourage the student
    6. End with a short summary

    Current Student Question:
    {question}
    """
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text