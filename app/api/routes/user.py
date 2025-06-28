from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.schemas.user import User, UserCreate
from app.crud import user as crud_user
from app.core.db import get_db

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=User)
def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    return crud_user.create_user(db, user)

@router.get("/", response_model=List[User])
def read_users(db: Session = Depends(get_db)):
    return crud_user.get_users(db)
