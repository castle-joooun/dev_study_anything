from typing import Optional
from enum import Enum

from fastapi import status, Response, APIRouter, Depends

from router.blog_post import required_functionality

router = APIRouter()


class BlogType(str, Enum):
    short = 'short'
    story = 'story'
    howto = 'howto'


@router.get(
    '/blog/all',
    summary='Retrieve all blogs',
    description='???',
    response_description='adsfasdfasd'
)
def get_all_blogs(page: int = 1, page_size: Optional[int] = None,
                  req_parameter: dict = Depends(
                      required_functionality)):
    return {'message': f'All {page_size} blogs on page {page}',
            'req': req_parameter}


@router.get('/blog/{id}/comments/{comment_id}', tags=['comment'])
def get_comment(id: int, comment_id: int, valid: bool = True,
                username: Optional[str] = None):
    """
    Simulates retrieving a comment of a blog

    - **id** mandatory path parameter
    """
    return {'message': f'blog {id}, {comment_id}, {valid}, {username}'}


@router.get('/blog/{id}', status_code=status.HTTP_200_OK)
def get_blog(id: int, response: Response):
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'error': f'Blog {id} not found'}
    response.status_code = status.HTTP_200_OK
    return {'message': f'blog with {id}'}


@router.get('/blog/type/{type}')
def get_blog_type(type: BlogType):
    return {'message': f'Blog type {type}'}
