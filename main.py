from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Read meeting notes from text file
with open("meeting_notes.txt", "r", encoding="utf-8") as file:
    meeting_notes = file.read()



prompt = f"""
Convert these meeting notes into:
1. Summary
2. Action items
3. Risks
4. Follow-up

Notes:
{meeting_notes}
"""

response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {"role": "system", "content": "You are a helpful meeting assistant."},
        {"role": "user", "content": prompt}
    ]
)

# Create fresh output file every run
result = response.choices[0].message.content
with open("meeting_summary.txt", "w", encoding="utf-8") as output_file:
    output_file.write(result)

print("Fresh meeting summary file created successfully.")

