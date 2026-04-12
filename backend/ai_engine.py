import ollama

def analyze_errors(errors: list):
    if not errors:
        return "No critical errors found."

    prompt = f"""
You are a senior DevOps engineer.

Analyze the following system errors and explain:

1. What the error means
2. Possible cause
3. How to fix it (step-by-step)

Errors:
{errors}

Give clear and simple explanation.
"""

    response = ollama.chat(
        model="qwen2.5:1.5b",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response["message"]["content"]