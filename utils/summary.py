import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

def summarize_document(text):
    prompt = f"""
You are an AI Document Summarizer.

Read the following document and generate:

1. A short summary (5-7 lines)
2. Key points (bullet points)
3. Important information
4. Conclusion

Document:
{text}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text