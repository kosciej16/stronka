import typing as t
from dataclasses import dataclass

from schemas.comment import CommentOut


@dataclass
class EventOut:
    name: str
    event_id: int
    start: str
    type: t.Optional[str]
    tags: t.List[str]
    limit: t.Optional[int]
    private: bool
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
            tags=e.tags.split(",") if e.tags else [],
            limit=e.limit,
            private=e.private,
            description=e.description,
            comments=[CommentOut.from_orm(c) for c in e.comments],
            users=[u.username for u in e.users],
        )
