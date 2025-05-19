from dotenv import load_dotenv
import os

from openai import OpenAI

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI()



async def generate_titles( 
        prompt_content:
        str = "Healthy eating can transform your energy levels, mood, and focus. Here’s how to start " ) -> list:
    response = client.chat.completions.create(
        model="gpt-4.1",
        temperature=0.7,
        messages=[
            {"role": "user", 
             "content": f"Generate 3 catchy titles for a blog post based on this content: \n {prompt_content}"}
        ]
    )
    
    return response.choices[0].message.content.split('\n')






