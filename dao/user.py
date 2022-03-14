from HW19.dao.model.user import User


class UserDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, uid):
        return self.session.query(User).get(uid)

    def get_all(self):
        return self.session.query(User).all()

    def get_filter(self, filter_dict):
        return self.session.query(User).filter_by(**filter_dict).all()

    def create(self, user_d):
        obj = User(**user_d)
        self.session.add(obj)
        self.session.commit()
        return obj

    def delete(self, uid):
        user = self.get_one(uid)
        self.session.delete(user)
        self.session.commit()

    def update(self, user_d):
        user = self.get_one(user_d.get("id"))
        if user:
            if user_d.get("usernamename"):
                user.username = user_d.get("usernamename")
            if user_d.get("password"):
                user.username = user_d.get("password")
            if user_d.get("role"):
                user.username = user_d.get("role")

        self.session.add(user)
        self.session.commit()
