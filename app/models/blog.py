from pydantic import BaseModel, Field
from typing import Optional


class BlogContent(BaseModel):
    prompt: Optional [str] = Field(default=
                "Healthy eating can transform your energy levels, "
                "mood, and focus. Here’s how to start")