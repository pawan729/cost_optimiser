import os
from google import genai
from dotenv import load_dotenv

load_dotenv()  # loads GEMINI_API_KEY from .env

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

response = client.models.generate_content(
    model="gemini-2.5-flash",   # use this to avoid quota=0 issues
    contents="Explain how AI works in a few words"
)

print(response.text)
