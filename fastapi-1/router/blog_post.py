from pydantic import BaseModel
from typing import Optional, List, Dict
from fastapi import APIRouter, Query, Path, Body

router = APIRouter()


class Image(BaseModel):
    url: str
    alias: str


class BlogModel(BaseModel):
    title: str
    content: str
    nb_comment: int
    published: Optional[bool]
    tags: List[str] = []
    metadata: Dict[str, str] = {'key1': 'value1'}
    image: Optional[Image] = None


@router.post('/new/{id}')
def create_blog(blog: BaseModel, id: int, version: int = 1):
    return {
        'id': id,
        'data': blog,
        'version': version
    }


@router.post('/new/{id}/comment')
def create_comment(blog: BlogModel, id: int,
                   comment_title: str = Query(
                       None,
                       title='Title of the comment',
                       description='Some description for comment_title',
                       alias='commentTitle',
                       deprecated=True
                   ),
                   content: str = Body(..., min_length=10),
                   v: Optional[List[str]] = Query(None),
                   comment_id: int = Path(None, gt=5, le=10)):
    return {
        'blog': blog,
        'id': id,
        'comment_title': comment_title,
        'content': content,
        'v': v,
        'comment_id': comment_id
    }
