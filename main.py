import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.ChatCompletion.create(
    model="gpt-5.3",
    messages=[
        {"role": "user", "content": "Write a short test article about credit score USA"}
    ]
)

content = response['choices'][0]['message']['content']

with open("article.html", "w") as f:
    f.write(content)

print("✅ OK - Article generated")
