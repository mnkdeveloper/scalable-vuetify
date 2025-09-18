
# api/services/user_service.py
from models.user import User
from extensions import db

class UserService:


    def create_user(username, email):
        user = User(username, email)
        db.session.add(user)
        db.session.commit()
        return user
