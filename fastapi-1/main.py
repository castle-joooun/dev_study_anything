from fastapi import FastAPI, status, Response, Request, HTTPException
from fastapi.responses import JSONResponse, PlainTextResponse
from fastapi.middleware.cors import CORSMiddleware

from router import blog_get, blog_post, user, article, product
from db import models
from db.database import engine
from exception import StoryException

app = FastAPI()
app.include_router(blog_get.router, prefix='/blog', tags=['blog'])
app.include_router(blog_post.router, prefix='/blog', tags=['blog'])
app.include_router(user.router, prefix='/user', tags=['user'])
app.include_router(article.router, prefix='/article', tags=['article'])
app.include_router(product.router, prefix='/product', tags=['product'])


@app.get('/')
def index():
    return {'message': 'Hello world'}


@app.exception_handler(StoryException)
def story_exception_handler(request: Request, exc: StoryException):
    return JSONResponse(
        status_code=418,
        content={'detail': exc.name}
    )


# @app.exception_handler(HTTPException)
# def custom_handler(request: Request, exc: StoryException):
#     return PlainTextResponse(str(exc), status_code=400)


models.Base.metadata.create_all(engine)

origins = {
    'https://localhost:3000'
}

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)
