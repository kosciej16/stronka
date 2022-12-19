from dataclasses import asdict
from datetime import datetime
import re
import typing as t
from fastapi.exceptions import HTTPException
from starlette.responses import HTMLResponse
import uvicorn
from fastapi import APIRouter, FastAPI, Depends, Body
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from db import get_db
from db.models.event import EventModel, association_table
from db.models.user import UserModel
from queries.user import get_user
from schemas.event import EventOut


event_router = APIRouter()

@event_router.get("")
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


@event_router.get("/{event_id}", response_model=EventOut)
def get_event(event_id: int, db: Session = Depends(get_db)):
    e = db.query(EventModel).filter_by(event_id=event_id).first()
    if e:
        return EventOut.from_orm(e)
    raise HTTPException(404)