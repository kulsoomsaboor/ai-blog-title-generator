from dotenv import load_dotenv
import os

import openai 

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


async def generate_titles(prompt: str) -> list:
    response = openai.responses.create(
        model="gpt-4.1",
        input="Write a one-sentence bedtime story about a unicorn."
    )
 
    return print(response.output_text)




