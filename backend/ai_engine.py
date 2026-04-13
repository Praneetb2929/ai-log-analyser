import google.generativeai as genai
import os

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Use fast model
model = genai.GenerativeModel("gemini-1.5-flash")


def extract_errors(log_text, max_lines=20):
    """
    Extract only relevant error/warning lines from logs
    """
    lines = log_text.split("\n")

    keywords = ["error", "fail", "exception", "critical", "warning"]

    filtered = [
        line for line in lines
        if any(keyword in line.lower() for keyword in keywords)
    ]

    # Limit size to avoid timeout
    return "\n".join(filtered[:max_lines])


def analyze_errors(log_text):
    """
    Send filtered logs to Gemini and get analysis
    """

    # Step 1: Filter important lines
    filtered_logs = extract_errors(log_text)

    # Step 2: Fallback if no errors found
    if not filtered_logs.strip():
        filtered_logs = log_text[:1500]  # fallback small chunk

    # Step 3: Create optimized prompt
    prompt = f"""
You are an expert DevOps engineer.

Analyze the following log errors and provide:
1. Root cause
2. Simple explanation
3. Suggested fix

Logs:
{filtered_logs}
"""

    try:
        # Step 4: Call Gemini
        response = model.generate_content(prompt)

        # Step 5: Return response safely
        if hasattr(response, "text"):
            return response.text
        else:
            return str(response)

    except Exception as e:
        return f"❌ Error analyzing logs: {str(e)}"
