import os 
from dotenv import load_dotenv 
from google import genai 

load_dotenv() 

client = genai.Client() 

def main(): 
    try: 
        while True: 
            user_input = input("You: ")
            if(user_input.lower() in ["exit", "quit"]):
                print("Exiting the chatbot. Goodbye!")
                break

            response = client.models.generate_content(
                model="gemini-3.1-flash-lite-preview", 
                contents=f"You are a helpful AI assistant. Answer clearly and concisely.\n\nUser: {user_input}"
            )
            print(f"Bot: {response.text}")
    except Exception as e: 
        print(f"An error occurred: {e}")

if __name__ == "__main__": 
    main() 