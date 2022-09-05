from fastapi import APIRouter, Depends, Header, Cookie
from fastapi.responses import Response, HTMLResponse, PlainTextResponse
from sqlalchemy.orm.session import Session
from typing import List, Optional

from db import db_article
from db.database import get_db
from schemas import ArticleBase, ArticleDisplay

router = APIRouter()

products = ['watch', 'camera', 'phone']


@router.get('/withheader')
def get_products(
        response: Response,
        custom_header: Optional[List[str]] = Header(),
        test_cookie: Optional[str] = Cookie(None)
):
    response.headers['custom_response_header'] = \
        ' and '.join(custom_header)
    return {
        'data': products,
        'custom_header': custom_header,
        'test_cookie': test_cookie
    }


@router.get('/all')
def get_all_products():
    # return products
    data = ' '.join(products)
    response = Response(content=data, media_type='text/plain')
    response.set_cookie(key='test_cookie', value='test_cookie_value')
    return response


@router.get('/{id}', responses={
    200: {
        'content': {
            'text/html': {
                'example': '<div>Product</div>'
            }
        },
        'description': 'Returns the HTML for an object'
    },
    404: {
        'content': {
            'text/plain': {
                'example': 'Product not available'
            }
        },
        'description': 'A clear text error message'
    }
})
def get_product(id: int):
    if id > len(products):
        out = 'Product not available'
        return PlainTextResponse(status_code=404, content=out,
                                 media_type='text/plain')
    else:
        product = products[id]
        out = f'''
        <head>
          <style>
          .product{{
            width: 500px;
            height: 30px;
            border: 2px inset green;
            background-color: lightblue;
            test-align: center;
          }}
          </style>
        <head>
        <div class="product">{product}</div>
        '''
        return HTMLResponse(content=out, media_type='text/html')
