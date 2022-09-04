from fastapi import FastAPI, status, Response

from router import blog_get, blog_post, user, article
from db import models
from db.database import engine

app = FastAPI()
app.include_router(blog_get.router, prefix='/blog', tags=['blog'])
app.include_router(blog_post.router, prefix='/blog', tags=['blog'])
app.include_router(user.router, prefix='/user', tags=['user'])
app.include_router(article.router, prefix='/article', tags=['article'])


@app.get('/')
def index():
    return {'message': 'Hello world'}


models.Base.metadata.create_all(engine)
