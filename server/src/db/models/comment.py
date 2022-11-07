from sqlalchemy import Boolean, Column, Integer, String, DateTime, func
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship


from db import Base


class CommentModel(Base):
    __tablename__ = "comment"

    comment_id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey("user.user_id"))
    event_id = Column(Integer, ForeignKey("event.event_id"))
    created_at = Column(DateTime, server_default=func.now())
    anonym = Column(Boolean, default=False)
    deleted = Column(Boolean, default=False)

    comment = Column(String)

    author = relationship("UserModel")
