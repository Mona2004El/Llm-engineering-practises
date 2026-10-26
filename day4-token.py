import tiktoken

encoding = tiktoken.encoding_for_model("gpt-4.1-mini")
tokens = encoding.encode("Hi my name is Ed and I like banoffee pie")
print(tokens)

for token_id in tokens:
    token_text = encoding.decode([token_id])
    print(f"{token_id} = {token_text}")

print(encoding.decode([326]))
###### let's start with a new example ###
from openai import OpenAI

openai = OpenAI(api_key="ollama",
    base_url="http://127.0.0.1:11434/v1")

messages1 = [
    {"role": "system", "content": "You are a helpful assistant"},
    {"role": "user", "content": "Hi! I'm Ed!"}
    ]
response1= openai.chat.completions.create(model="llama3.2:1b", messages=messages1)
res1=response1.choices[0].message.content
print("res1=",res1)

messages2= [
    {"role": "system", "content": "You are a helpful assistant"},
    {"role": "user", "content": "What's my name?"}
    ]
response2 = openai.chat.completions.create(model="llama3.2:1b", messages=messages2)
res2=response2.choices[0].message.content
print("res2= ",res2)

messages3 = [
    {"role": "system", "content": "You are a helpful assistant"},
    {"role": "user", "content": "Hi! I'm Ed!"},
    {"role": "assistant", "content": "Hi Ed! How can I assist you today?"},
    {"role": "user", "content": "What's my name?"}
    ]
response3 = openai.chat.completions.create(model="llama3.2:1b", messages=messages3)
res3=response3.choices[0].message.content
print("res3= ",res3)