from openai import OpenAI
from scraper import fetch_website_contents

# Connect to Ollama running locally
client = OpenAI(
    api_key="ollama",
    base_url="http://127.0.0.1:11434/v1"
)

# Fetch the website content
url = "https://edwarddonner.com"
website_text = fetch_website_contents(url)

# Ask the model to summarize the website
messages = [
    {
        "role": "system",
        "content": (
            "You are a helpful assistant that summarizes websites. "
            "Write a clear summary of the main points."
        )
    },
    {
        "role": "user",
        "content": (
            f"Please summarize this website:\n\n{website_text[:12000]}"
        )
    }
]

response = client.chat.completions.create(
    model="llama3.2:1b",
    messages=messages
)

summary = response.choices[0].message.content
print("\n--- Website Summary ---\n")
print(summary)