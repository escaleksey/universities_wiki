from config import db

association_table = db.Table('users_universities', db.Model.metadata,
                             db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
                             db.Column('university_id', db.Integer, db.ForeignKey('university.id'))
                             )


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    universities = db.relationship("University",
                                   secondary=association_table)


class University(db.Model):
    __tablename__ = 'university'
    name = db.Column(db.String)
    id = db.Column(db.Integer, primary_key=True)
    faculties = db.relationship('Faculty', backref='university')


class Faculty(db.Model):
    __tablename__ = "faculty"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    university_id = db.Column(db.Integer, db.ForeignKey('university.id'))


if __name__ == "__main__":
    # Run this file directly to create the database tables.
    print("Creating database tables...")
    db.create_all()
    print("Done!")