import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")
API_URL = "https://openrouter.ai/api/v1/chat/completions"

def ask_ai(prompt: str) -> str:
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": "openrouter/auto",
        "messages": [
            {"role": "user", "content": prompt}
        ],
    }

    response = requests.post(API_URL, headers=headers, json=payload, timeout=60)
    response.raise_for_status()
    data = response.json()
    return data["choices"][0]["message"]["content"]

def main():
    prompt = input("Enter your prompt: ")
    reply = ask_ai(prompt)
    print("\nAI Response:\n")
    print(reply)

if __name__ == "__main__":
    main()