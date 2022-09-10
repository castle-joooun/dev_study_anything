import time

from fastapi import FastAPI, status, Response, Request, HTTPException
from fastapi.responses import JSONResponse, PlainTextResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import uvicorn

from router import blog_get, blog_post, user, article, product, file
from db import models
from db.database import engine
from exception import StoryException
from auth import authentication
from templates import templates

app = FastAPI()
app.include_router(blog_get.router, tags=['blog'])
app.include_router(blog_post.router, prefix='/blog', tags=['blog'])
app.include_router(user.router, prefix='/user', tags=['user'])
app.include_router(article.router, prefix='/article', tags=['article'])
app.include_router(product.router, prefix='/product', tags=['product'])
app.include_router(authentication.router, tags=['authentication'])
app.include_router(file.router, prefix='/file', tags=['file'])
app.include_router(templates.router, prefix='/templates',
                   tags=['templates'])


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


@app.middleware('http')
async def add_middleware(request: Request, class_next):
    start_time = time.time()
    response = await class_next(request)
    duration = time.time() - start_time
    response.headers['duration'] = str(duration)
    return response


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

app.mount('/files', StaticFiles(directory='files'), name='files')
app.mount('/templates/static',
          StaticFiles(directory='templates/static'),
          name='static'
          )

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
