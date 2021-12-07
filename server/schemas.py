import random
import typing as t
from dataclasses import dataclass


@dataclass
class CommentOut:
    comment_id: int
    author_name: str
    anomised: str
    created_at: str
    comment: str

    @classmethod
    def from_orm(cls, c):
        name = c.author.username
        if c.anonym:
            i = random.randint(0, len(name)-1)
            name = f"{name[0:i]}*{name[i+1:]}"
        return cls(
            c.comment_id, c.author.username, name, str(c.created_at), c.comment.replace("głupi", "")
        )


@dataclass
class CommentIn:
    author_name: str
    comment: str
    anonym: bool
    event_id: t.Optional[int] = None


@dataclass
class EventOut:
    name: str
    event_id: int
    start: str
    type: t.Optional[str]
    tags: t.List[str]
    limit: t.Optional[int]
    description: t.Optional[str]
    comments: t.List[CommentOut]
    users: t.List[str]

    @classmethod
    def from_orm(cls, e):
        return cls(
            name=e.name,
            event_id=e.event_id,
            start=str(e.start),
            type=e.type,
            tags=e.tags.split(","),
            limit=e.limit,
            description=e.description,
            comments=[CommentOut.from_orm(c) for c in e.comments],
            users=[u.username for u in e.users],
        )


@dataclass
class UserOut:
    user_id: int
    username: str


@dataclass
class UserIn:
    username: str
    password: str
    email: t.Optional[str] = None
