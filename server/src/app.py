from dataclasses import asdict
from datetime import datetime
import re
import typing as t
from fastapi.exceptions import HTTPException
from starlette.responses import HTMLResponse
import uvicorn
from fastapi import FastAPI, Depends, Body
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from db import get_db
from db.models.event import EventModel, association_table
from db.models.user import UserModel
from queries.user import get_user
from routers.comment import comment_router
from old_schemas import EventOut, UserIn, UserOut

app = FastAPI()
app.include_router(comment_router, prefix="/api/v1/comment")
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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
    errors.append(("Hasło jest za długie. Upewnij się, że Twoje hasło ma maksymalnie 2 znaki", b))
    b = not re.match("[0-9a]*$", data.password)
    errors.append(("Hasło ma zbyt skomplikowane znaki. Dozwolone znaki to cyfry i litera 'a'", b))

    user = db.query(UserModel).filter(data.password == UserModel.password).first()
    b = user is not None
    errors.append(("Z hasła nie może korzystać żaden inny użytkownik", b))
    #     return UserOut(user_id=user.user_id, username=user.username)
    if any(el[1] for el in errors):
        errors.insert(0, "Hasło nie spełnia wymogów zapamiętywalności!")
        raise HTTPException(401, detail=errors)
    db.add(UserModel(**asdict(data)))
    db.commit()


if __name__ == "__main__":
    kwargs = {"host": "0.0.0.0", "port": 8002}
    kwargs.update({"debug": True, "reload": True})
    uvicorn.run("app:app", **kwargs)
