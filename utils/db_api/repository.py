import models
from config import db
from models import User, University, Faculty


def create_user():
    user = User(name="Vania")
    university1 = University(name="PHTT")
    university2 = University(name="PHTT2")
    user.universities.append(university1)
    user.universities.append(university2)
    faculty1 = models.Faculty(name="MM")
    faculty2 = models.Faculty(name="Mn")
    faculty3 = models.Faculty(name="Mv")
    faculty4 = models.Faculty(name="Mf")
    university1.faculties.append(faculty1)
    university1.faculties.append(faculty2)
    university2.faculties.append(faculty3)
    university2.faculties.append(faculty4)
    db.session.add(user)
    db.session.commit()