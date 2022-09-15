from pydantic import BaseModel
from datetime import datetime


class PostBase(BaseModel):
    image_url: str
    title: str
    content: str
    creator: str


class PostDisplay(PostBase):
    id: int
    timestamp: datetime

    class Config:
        orm_mode = True
