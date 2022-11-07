from sqlalchemy import func

from db.models.user import UserModel


def get_user(name, db):
    user = db.query(UserModel).filter(name.lower() == func.lower(UserModel.username)).first()
    return user
