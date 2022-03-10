import hashlib

from HW19.constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS
from HW19.dao.user import UserDAO



class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_one(self, uid):
        return self.dao.get_one(uid)

    def get_all(self):
        return self.dao.get_all()

    def create(self, user_d):
        return self.dao.create(user_d)

    def update(self, uid):
        self.dao.update(uid)
        return self.dao

    def delete(self, uid):
        self.dao.delete(uid)

    def get_hash(password):
            return hashlib.pbkdf2_hmac(
                'sha256',
                password.encode('utf-8'),  # Convert the password to bytes
                PWD_HASH_SALT,
                PWD_HASH_ITERATIONS
            ).decode("utf-8", "ignore")