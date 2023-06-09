from project.dao.user import UserDAO
from project.tools.security import generate_password_hash


class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_one(self, uid):
        return self.dao.get_one(uid)

    def get_by_email(self, email):
        return self.dao.get_by_email(email)

    def get_all(self):
        return self.dao.get_all()

    def create(self, user_data):
        user_data["password"] = generate_password_hash(user_data["password"])
        return self.dao.create(user_data)

    def update(self, user_data):
        self.dao.update(user_data)
        return self.dao

    def update_password(self, id, new_password):
        self.dao.update_password(id, new_password)

    def delete(self, uid):
        self.dao.delete(uid)