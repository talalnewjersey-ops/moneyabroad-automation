import os
from openai import OpenAI

# Initialisation API
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

prompt = """
Write a 3500-word SEO article in HTML format for newcomers in the USA.

Topic: Credit Score USA 2026

Include:
- Key Takeaways
- 2 realistic stories
- 2 tables
- FAQ section
- Beginner-friendly tone
- Author box (Talal Eddaouahiri)
- Educational disclaimer

Return clean HTML only.
"""

response = client.chat.completions.create(
    model="gpt-5.3",
    messages=[{"role": "user", "content": prompt}]
)

content = response.choices[0].message.content

with open("article.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Article generated successfully")
