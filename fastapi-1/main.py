from fastapi import FastAPI, status, Response

from router import blog_get, blog_post

app = FastAPI()
app.include_router(blog_get.router, prefix='/blog', tags=['blog'])
app.include_router(blog_post.router, prefix='/blog', tags=['blog'])


@app.get('/')
def index():
    return {'message': 'Hello world'}



