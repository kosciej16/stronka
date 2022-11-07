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
            i = random.randint(0, len(name) - 1)
            name = f"{name[0:i]}*{name[i+1:]}"
        return cls(
            c.comment_id,
            c.author.username,
            name,
            str(c.created_at),
            c.comment.replace("głupi", ""),
        )


@dataclass
class CommentIn:
    author_name: str
    comment: str
    anonym: bool
    event_id: t.Optional[int] = None
