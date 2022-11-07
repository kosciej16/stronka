from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.sqltypes import JSON

from db import Base


class UserModel(Base):
    __tablename__ = "user"

    user_id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    password = Column(String(100), nullable=False)
    phone = Column(String(15))
    email = Column(String(100), unique=True)
    extra = Column(JSON)
