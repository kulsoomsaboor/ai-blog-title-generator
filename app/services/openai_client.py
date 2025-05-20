from dotenv import load_dotenv
import os

from openai import OpenAI
from app.utils import build_prompt



load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI()



async def generate_titles( prompt_content: str ) -> list:
    refined_prompt=build_prompt(prompt_content)
    response = client.chat.completions.create(

        
        model="gpt-4.1",
        temperature=0.7,
        messages=[
            {"role": "user", 
             "content": f"Generate 3 catchy titles for a blog post based on this content: \n {refined_prompt}"}
        ]
    )
    
    return response.choices[0].message.content.split('\n')






