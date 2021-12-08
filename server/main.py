from db import Base, SessionLocal, engine
from db.models.user import UserModel
from db.models.event import EventModel, association_table
from db.models.comment import CommentModel
from db.models.point import PointModel
from datetime import datetime, timedelta

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

s = SessionLocal()
u = UserModel(username="abc", password="12")
u2 = UserModel(username="a", password="a", extra={"a": 1, "b": "a"})
e = EventModel(
    name="Terra Mystica",
    start=datetime.now(),
    type="plansze",
    tags=["a", "b"],
    limit=4,
    description="Terra mystica to super gra jfkd fjs fsl jfsdlj fsdl fjsld jfsldj flsd fjsldj fsld jf",
    private=True,
)
e2 = EventModel(
    name="Terra Mystica",
    start=datetime.now() + timedelta(days=1),
    type="plansze",
    tags=["a", "b"],
    limit=4,
    description="Terra mystica to super gra jfkd fjs fsl jfsdlj fsdl fjsld jfsldj flsd fjsldj fsld jf",
)
e3 = EventModel(
    name="Terra Mystica",
    start=datetime.now() - timedelta(days=1),
    type="plansze",
    tags=["a", "b"],
    limit=4,
    description="Terra mystica to super gra jfkd fjs fsl jfsdlj fsdl fjsld jfsldj flsd fjsldj fsld jf",
)
e4 = EventModel(
    name="Terra Mystica",
    start=datetime.now() + timedelta(days=2),
    type="plansze",
    tags=["a", "b"],
    limit=4,
    description="Terra mystica to super gra jfkd fjs fsl jfsdlj fsdl fjsld jfsldj flsd fjsldj fsld jf",
)
s.add(e)
s.add(e2)
s.add(e3)
s.add(e4)
s.add(u)
s.add(u2)
s.commit()
c = CommentModel(author_id=u.user_id, event_id=e.event_id, comment="co")
s.add(c)
s.commit()
# stmt = association_table.insert().values(event_id=e.event_id, user_id=u.user_id)
# s.execute(stmt)
# s.commit()
