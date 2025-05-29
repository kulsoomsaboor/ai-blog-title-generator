from fastapi import APIRouter

from app.models.blog import BlogContent      
from app.services.openai_client import generate_titles
from openai import OpenAIError  

from fastapi import HTTPException
from fastapi.responses import JSONResponse

import logging

router = APIRouter()
logger = logging.getLogger(__name__)


@router.get("/")
def read_root():
    return {"message": "Blog Title Generator API"}

@router.post("/generate-titles")
async def generate_reponse(blog: BlogContent):
    try:
        logger.info(f"Received blog prompt: {blog.prompt}")
        titles = await generate_titles(blog.prompt)
      

        logger.info(f"Generated titles: {titles}")
        return {"titles": titles["titles"]}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))