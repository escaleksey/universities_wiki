from config import db
from utils.db_api.models import User, University, Faculty
import json


def create_user():
    user = User(name="Aleksey", email='Aleksey@gmaol.com', age='12',
                hashed_password='pbkdf2:sha256:260000$akY41ltT5JCrKDSc$01159880564c9762007205d247a9581c7b5da8aad4e94ffaef1290a8982a7259')
    university1 = University(name="PGNIU", city='Пермь')
    university2 = University(name="PHTT2", city='Пермь')
    user.universities.append(university1)
    user.universities.append(university2)
    faculty1 = Faculty(name="MM", points='123', price='1233567890')
    faculty2 = Faculty(name="Mn", points='123', price='1233567890')
    faculty3 = Faculty(name="Mv", points='123', price='1233567890')
    faculty4 = Faculty(name="Mf", points='123', price='1233567890')
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
        university = University(name=value['title'], city='Пермь')
        for key1, value1 in value['specialties'].items():
            for key2, value2 in value1['programs'].items():
                faculty = Faculty(name=value2['title'], points=value2['score'], price=value2['price'])
                university.faculties.append(faculty)
        # print(f'{key}: {value}')
        db.session.add(university)
        db.session.commit()


if __name__ == '__main__':
    parse_json()
    create_user()
