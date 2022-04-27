import models
from config import db
from models import User, University, Faculty
import json


def create_user():
    user = User(name="Aleksey", email='Aleksey@gmaol.com', age='12', key='qew')
    university1 = University(name="PGNIU", address='Zakamskaya 39')
    university2 = University(name="PHTT2", address='Zakamskaya 41')
    user.universities.append(university1)
    user.universities.append(university2)
    faculty1 = Faculty(name="MM", points='123', description='super', price='1233567890')
    faculty2 = Faculty(name="Mn", points='123', description='super', price='1233567890')
    faculty3 = Faculty(name="Mv", points='123', description='super', price='1233567890')
    faculty4 = Faculty(name="Mf", points='123', description='super', price='1233567890')
    university1.faculties.append(faculty1)
    university1.faculties.append(faculty2)
    university2.faculties.append(faculty3)
    university2.faculties.append(faculty4)
    db.session.add(user)
    db.session.commit()


def parse_json():
    with open('../../static/json/perm_university.json') as json_file:
        data = json.load(json_file)['PERM']

    for key, value in data.items():
        university = University(name=value['title'], address='-')
        for key1, value1 in value['specialties'].items():
            for key2, value2 in value1['programs'].items():
                faculty = Faculty(name=value2['title'], points=value2['score'], description='-', price=value2['price'])
                university.faculties.append(faculty)
        #print(f'{key}: {value}')
        db.session.add(university)
        db.session.commit()


if __name__ == '__main__':
    parse_json()