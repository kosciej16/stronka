import typing as t

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db import get_db
from db.models.comment import CommentModel
from queries.user import get_user
from schemas.comment import CommentIn, CommentOut

comment_router = APIRouter()


@comment_router.get("", response_model=t.List[CommentOut])
def get_comments(db: Session = Depends(get_db)):
    res = []
    comments = db.query(CommentModel).filter_by(deleted=False).order_by(CommentModel.created_at.desc()).all()
    for c in comments:
        res.append(CommentOut.from_orm(c))
    return res


@comment_router.post("/comment", response_model=t.List[CommentOut])
def add_comment(c: CommentIn, db: Session = Depends(get_db)):
    user = get_user(c.author_name, db)
    db.add(CommentModel(author_id=user.user_id, comment=c.comment, event_id=c.event_id, anonym=c.anonym))
    db.commit()


@comment_router.delete("/comment/{comment_id}")
def delete_comment(comment_id: int, db: Session = Depends(get_db)):
    res = db.query(CommentModel).filter_by(comment_id=comment_id).first()
    res.deleted = True
    db.commit()
