from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship

from db import Base


class PointModel(Base):
    __tablename__ = "point"

    point_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.user_id"))
    event_id = Column(Integer, ForeignKey("event.event_id"))
    quantity = Column(Integer)
    description = Column(String)

    user = relationship("UserModel", backref="points")
