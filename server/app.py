from dataclasses import asdict
from datetime import datetime
import re
import typing as t
from fastapi.exceptions import HTTPException
from starlette.responses import HTMLResponse
import uvicorn
from fastapi import FastAPI, Depends, Body
from sqlalchemy import func
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from db import get_db
from db.models.comment import CommentModel
from db.models.event import EventModel, association_table
from db.models.user import UserModel
from schemas import CommentIn, CommentOut, EventOut, UserIn, UserOut

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_user(name, db):
    user = db.query(UserModel).filter(name.lower() == func.lower(UserModel.username)).first()
    return user


@app.get("/event")
def get_events(db: Session = Depends(get_db)):
    past, fut = [], []
    events = db.query(EventModel).all()
    for e in events:
        if e.start > datetime.now():
            fut.append(EventOut.from_orm(e))
        else:
            past.append(EventOut.from_orm(e))
    fut.sort(key=lambda e: e.start)
    past.sort(key=lambda e: e.start, reverse=True)
    return {"past": past, "fut": fut}


@app.get("/comment", response_model=t.List[CommentOut])
def get_comments(db: Session = Depends(get_db)):
    res = []
    comments = (
        db.query(CommentModel)
        .filter_by(deleted=False)
        .order_by(CommentModel.created_at.desc())
        .all()
    )
    for c in comments:
        res.append(CommentOut.from_orm(c))
    return res


@app.post("/comment", response_model=t.List[CommentOut])
def add_comment(c: CommentIn, db: Session = Depends(get_db)):
    user = get_user(c.author_name, db)
    db.add(
        CommentModel(
            author_id=user.user_id, comment=c.comment, event_id=c.event_id, anonym=c.anonym
        )
    )
    db.commit()


@app.delete("/comment/{comment_id}")
def delete_comment(comment_id: int, db: Session = Depends(get_db)):
    res = db.query(CommentModel).filter_by(comment_id=comment_id).first()
    print(res)
    res.deleted = True
    db.commit()


@app.get("/event/{event_id}", response_model=EventOut)
def get_event(event_id: int, db: Session = Depends(get_db)):
    e = db.query(EventModel).filter_by(event_id=event_id).first()
    if e:
        return EventOut.from_orm(e)
    raise HTTPException(404)


@app.post("/event/{event_id}", response_model=EventOut)
def sign_on_event(event_id: int, user_id: int = Body(...), db: Session = Depends(get_db)):
    e = db.query(EventModel).filter_by(event_id=event_id).first()
    if e.limit == len(e.users):
        raise HTTPException(400)

    stmt = association_table.insert().values(event_id=event_id, user_id=user_id)
    try:
        db.execute(stmt)
        db.commit()
    except:
        raise HTTPException(400)


@app.delete("/event/{event_id}", response_model=EventOut)
def sign_off_event(event_id: int, user_id: int, db: Session = Depends(get_db)):
    stmt = association_table.delete().where(
        association_table.c.event_id == event_id, association_table.c.user_id == user_id
    )
    try:
        db.execute(stmt)
        db.commit()
    except:
        raise HTTPException(400)


@app.post("/login", response_model=UserOut)
def login(data: UserIn, db: Session = Depends(get_db)):
    user = get_user(data.username, db)
    if user and user.password == data.password:
        print("AAA")
        return UserOut(user_id=user.user_id, username=user.username)
    raise HTTPException(403)


@app.post("/register")
def register(data: UserIn, db: Session = Depends(get_db)):
    errors = []
    b = len(data.password) > 2
    errors.append(("Has??o jest za d??ugie. Upewnij si??, ??e Twoje has??o ma maksymalnie 2 znaki", b))
    b = not re.match("[0-9a]*$", data.password)
    errors.append(("Has??o ma zbyt skomplikowane znaki. Dozwolone znaki to cyfry i litera 'a'", b))

    user = db.query(UserModel).filter(data.password == UserModel.password).first()
    b = user is not None
    errors.append(("Z has??a nie mo??e korzysta?? ??aden inny u??ytkownik", b))
    #     return UserOut(user_id=user.user_id, username=user.username)
    if any(el[1] for el in errors):
        errors.insert(0, "Has??o nie spe??nia wymog??w zapami??tywalno??ci!")
        raise HTTPException(401, detail=errors)
    db.add(UserModel(**asdict(data)))
    db.commit()


if __name__ == "__main__":
    kwargs = {"host": "0.0.0.0", "port": 8002}
    kwargs.update({"debug": True, "reload": True})
    uvicorn.run("app:app", **kwargs)
