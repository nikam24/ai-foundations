import os
from dotenv import load_dotenv 
from google import genai

load_dotenv() 

client = genai.Client()

def main():
    text = input("Enter the text to summarize: ")
    response = client.models.generate_content(
        model="gemini-3.1-flash-lite-preview", 
        contents=f"Summarize the following text in 3 concise bullet points.:\n\n{text}"
    )
    summary = response.text
    print(f"\nSummary:\n{summary}")

if __name__ == "__main__":
    main()