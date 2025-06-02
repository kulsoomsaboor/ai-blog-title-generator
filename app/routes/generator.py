from fastapi import APIRouter, Request


from app.models.blog import BlogContent      
from app.services.openai_client import generate_titles
from openai import OpenAIError  

from fastapi import HTTPException
from fastapi.responses import JSONResponse

from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

import logging

router = APIRouter()
logger = logging.getLogger(__name__)


templates = Jinja2Templates(directory="app/templates")

@router.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@router.post("/generate-titles")
async def generate_reponse(blog: BlogContent):
    try:
        logger.info(f"Received blog prompt: {blog.prompt}")
        titles = await generate_titles(blog.prompt)
      

        logger.info(f"Generated titles: {titles}")
        return titles

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))