from utils.db_api.config import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

association_table = db.Table('users_universities', db.Model.metadata,
                             db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
                             db.Column('university_id', db.Integer, db.ForeignKey('university.id')),
                             extend_existing=True
                             )


class User(db.Model, UserMixin):
    __tablename__ = 'user'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    age = db.Column(db.Integer)
    email = db.Column(db.String)
    hashed_password = db.Column(db.String, nullable=False)
    # avatar = db.Column(db.LargeBinary, nullable=False)
    universities = db.relationship("University",
                                   secondary=association_table)

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)


class University(db.Model):
    __tablename__ = 'university'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    # address = db.Column(db.String)
    city = db.Column(db.String)
    faculties = db.relationship('Faculty', backref='university')



class Faculty(db.Model):
    __tablename__ = "faculty"
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    points = db.Column(db.String)
    # description = db.Column(db.String)
    price = db.Column(db.String)
    university_id = db.Column(db.Integer, db.ForeignKey('university.id'))


if __name__ == "__main__":
    # Run this file directly to create the database tables.
    print("Creating database tables...")
    db.create_all()
    print("Done!")
