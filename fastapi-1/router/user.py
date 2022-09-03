from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session

from db import db_user
from db.database import get_db
from schemas import UserBase, UserDisplay

router = APIRouter()


# Create user
@router.post('/', response_model=UserDisplay)
def create_user(request: UserBase, db: Session = Depends(get_db)):
    return db_user.create_user(db, request)

# Read user

# Update user

# Delete user
