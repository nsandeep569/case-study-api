from db import db


class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    password = db.Column(db.String(80))
    level=db.Column(db.Integer)

    def __init__(self, name, password,level):
        self.name = name
        self.password = password
        self.level=level

    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'level':self.level
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
