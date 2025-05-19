from fastapi import APIRouter
from pydantic import BaseModel
from app.services.openai_client import generate_titles
from fastapi import HTTPException



router = APIRouter()

class BlogContent(BaseModel):
    prompt: str

@router.get("/")
def read_root():
    return {"message": "Blog Title Generator API"}

@router.post("/generate-titles")
async def generate_reponse(blog: BlogContent):
    try:
        titles = await generate_titles(blog.prompt)
        return {"titles": titles}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    