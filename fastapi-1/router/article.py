from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session
from typing import List

from db import db_article
from db.database import get_db
from schemas import ArticleBase, ArticleDisplay

router = APIRouter()


# Create article
@router.post('/', response_model=ArticleDisplay)
def create_article(request: ArticleBase, db: Session = Depends(get_db)):
    return db_article.create_article(db, request)


# Get specific article
@router.get('/{id}', response_model=ArticleDisplay)
def get_article(id: int, db: Session = Depends(get_db)):
    return db_article.get_article(db, id)
