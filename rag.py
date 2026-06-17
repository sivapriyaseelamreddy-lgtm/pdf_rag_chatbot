import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")
def get_answer(pdf_text, question):

    prompt = f"""
You are a helpful AI assistant.

PDF CONTENT:
{pdf_text}

QUESTION:
{question}

Answer only from PDF.
"""

    response = model.generate_content(prompt)

    return response.text