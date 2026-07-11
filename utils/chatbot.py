import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

def ask_gemini(context, question):
    prompt = f"""
You are an intelligent AI Document Assistant.

Instructions:
- Answer only using the document context provided.
- Do not make up information.
- If the answer is not available in the document, say:
  "I couldn't find that information in the uploaded document."
- Keep the answer clear, concise, and well formatted.
- Use bullet points where appropriate.

Document Context:
{context}

User Question:
{question}

Answer:
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text