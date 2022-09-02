from typing import Optional
from enum import Enum

from fastapi import FastAPI, status, Response

app = FastAPI()


class BlogType(str, Enum):
    short = 'short'
    story = 'story'
    howto = 'howto'


@app.get('/')
def index():
    return {'message': 'Hello world'}


# @app.get('/blog/all')
# def get_all_blogs():
#     return {'message': 'blog all'}


@app.get(
    '/blog/all',
    tags=['blog'],
    summary='Retrieve all blogs',
    description='???',
    response_description='adsfasdfasd'
)
def get_all_blogs(page: int = 1, page_size: Optional[int] = None):
    return {'message': f'All {page_size} blogs on page {page}'}


@app.get('/blog/{id}/comments/{comment_id}', tags=['blog', 'comment'])
def get_comment(id: int, comment_id: int, valid: bool = True,
                username: Optional[str] = None):
    """
    Simulates retrieving a comment of a blog

    - **id** mandatory path parameter
    """
    return {'message': f'blog {id}, {comment_id}, {valid}, {username}'}


@app.get('/blog/{id}', status_code=status.HTTP_200_OK, tags=['blog'])
def get_blog(id: int, response: Response):
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'error': f'Blog {id} not found'}
    response.status_code = status.HTTP_200_OK
    return {'message': f'blog with {id}'}


@app.get('/blog/type/{type}', tags=['blog'])
def get_blog_type(type: BlogType):
    return {'message': f'Blog type {type}'}
