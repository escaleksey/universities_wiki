import datetime
import sqlalchemy
from flask_login import UserMixin
from sqlalchemy import orm
from werkzeug.security import generate_password_hash, check_password_hash

from utils.db_api.data.db_session import SqlAlchemyBase


class User(SqlAlchemyBase, UserMixin):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    email = sqlalchemy.Column(sqlalchemy.String, index=True, unique=True, nullable=True)
    salt = sqlalchemy.Column(sqlalchemy.LargeBinary, nullable=False)
    key = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    created_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)

    #universities = orm.relationship("University", backhref=).backhref

    def __repr__(self):
        return f'<User> {self.id} {self.name} {self.email}'

    """ пока не знаю как это сделать (?)
    def set_password(self, password):
        self.salt, self.key = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)"""
