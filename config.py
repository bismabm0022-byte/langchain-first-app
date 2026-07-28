import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

def get_chat_model(temperature: float = 0.7):
    """Initializes and returns the LangChain Chat Model."""
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("GOOGLE_API_KEY not found in environment variables.")

    return ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=temperature
    )
