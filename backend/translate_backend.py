import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
MODEL = os.getenv("GEMINI_MODEL", "models/gemini-2.5-flash")

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel(MODEL)

def translate_text(text, target_language):
    prompt = f"""
    Translate the following text into {target_language}.
    Only return the translated text. No explanation.

    TEXT:
    {text}
    """

    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Translation Error: {str(e)}"
