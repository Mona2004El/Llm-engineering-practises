import os
from dotenv import load_dotenv
from openai import OpenAI

# Constants
MODEL_GPT = "gpt-4o-mini"
MODEL_LLAMA = "llama3.2:1b"

# Set up environment
load_dotenv(override=True)

# Ollama client
ollama = OpenAI(
    base_url="http://localhost:11434/v1/",
    api_key="ollama"
)

# Question
question = """
Please explain what this code does and why:
yield from {book.get("author") for book in books if book.get("author")}
"""

def ask_llama(question):
    response = ollama.chat.completions.create(
        model=MODEL_LLAMA,
        messages=[
            {
                "role": "user",
                "content": question
            }
        ]
    )

    return response.choices[0].message.content


answer = ask_llama(question)
print("\n--- Llama 3.2 Answer ---\n")
print(answer)