from typing import List, Optional

from fastapi import Depends, FastAPI, HTTPException, Request, status
from pydantic import BaseModel, EmailStr
from sqlalchemy.orm import Session

from db import Base, SessionLocal, engine
from models import User

app = FastAPI()

Base.metadata.create_all(bind=engine)


class new_user(BaseModel):
    username: str
    email: EmailStr


class user_update(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None


def init_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/all-users")
def get_all_users(username: str = "", email: str = "", db: Session = Depends(init_db)):
    users = db.query(User).all()
    filtered_users = list(
        filter(
            lambda x: username.casefold() in x.username.casefold()
            and email.casefold() in x.email.casefold(),
            users,
        )
    )
    return filtered_users


@app.get("/users/{id}")
def get_users(id: int, db: Session = Depends(init_db)):
    user = db.query(User).filter(User.id == id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@app.put("/update-user/{id}")
def update_user(id: int, req: user_update, db: Session = Depends(init_db)):
    user = db.query(User).filter(User.id == id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    update_data = req.model_dump(exclude_unset=True)
    for key, val in update_data.items():
        setattr(user, key, val)
    db.commit()
    db.refresh(user)
    return user


@app.delete("/delete-user/{id}")
def del_user(id: int, db: Session = Depends(init_db)):
    user = db.query(User).filter(User.id == id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()

    return {"message": f"the user with id : {id} has been deleted"}, 401


@app.post("/add-user")
def add_new_user(user: new_user, db: Session = Depends(init_db)):
    user_instance = User(**user.dict())
    db.add(user_instance)
    db.commit()
    db.refresh(user_instance)
    return {"message": "User added successfully", "user": user_instance}
