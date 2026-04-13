import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def analyze_errors(errors):
    prompt = f"""
    Analyze the following system errors and provide:
    - Root cause
    - Impact
    - Solution

    Errors:
    {errors}
    """

    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)

    return response.text
