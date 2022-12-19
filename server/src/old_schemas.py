import typing as t
from dataclasses import dataclass

@dataclass
class UserOut:
    user_id: int
    username: str


@dataclass
class UserIn:
    username: str
    password: str
    email: t.Optional[str] = None
