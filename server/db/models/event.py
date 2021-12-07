from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey, Table

from db import Base


association_table = Table(
    "user_event",
    Base.metadata,
    Column("user_id", ForeignKey("user.user_id"), primary_key=True),
    Column("event_id", ForeignKey("event.event_id"), primary_key=True),
)


class EventModel(Base):
    __tablename__ = "event"

    event_id = Column(Integer, primary_key=True)
    name = Column(String)
    start = Column(DateTime)
    type = Column(String)
    tags = Column(String)
    limit = Column(Integer)
    description = Column(String)

    comments = relationship("CommentModel")
    users = relationship("UserModel", secondary=association_table)
