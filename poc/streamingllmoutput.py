import openai
client = openai.Client(
    base_url="http://localhost:11434/v1/",
    api_key="***",
)

prompt = {
    "role": "user",
    "content": "Write a poem about AI in the style of Shakespeare.",
}

response = client.chat.completions.create(
    model="gemma3:1b",
    messages=[prompt],
    stream=True,
)

for chunk in response:
    delta = chunk.choices[0].delta
    if delta and delta.content:
        print(delta.content, end="", flush=True)
        

print("------")

response = client.chat.completions.create(
    model="gemma3:1b",
    messages=[prompt],
    stream=False,
)

print(response.choices[0].message.content)