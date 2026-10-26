# imports

import os
#from dotenv import load_dotenv
#from scraper import fetch_website_contents
#from IPython.display import Markdown, display
from openai import OpenAI

#load_dotenv()
# Load environment variables in a file called .env


openai = OpenAI(
    api_key="ollama",
    base_url="http://127.0.0.1:11434/v1"
)



message = "Hello, GPT! This is my first ever message to you! Hi!"

messages=[{"role":"user", "content":message}]
response = openai.chat.completions.create(model="llama3.2:1b", messages=messages)
print(response.choices[0].message.content)

messages=[{"role": "user", "content": "what is 2+2?"}]
response = openai.chat.completions.create(model="llama3.2:1b", messages=messages)
print(response.choices[0].message.content)