from config import db
from utils.db_api.models import User, University, Faculty
import json
from utils.db_api import db_session


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


def parse_json(city_list):
    with open(city_list[0]) as json_file:
        data = json.load(json_file)[city_list[1]]

    with open('../../static/json/images2.json') as json_file:
        data2 = json.load(json_file)

    for key, value in data.items():
        db_file = "../../db/database.db"
        db_session.global_init(db_file)
        session = db_session.create_session()

        all_universities = session.query(University).where(University.name == value['title']).all()
        print(all_universities)
        if all_universities:
            continue
        university = University(name=value['title'], city=city_list[2], image=data2[value['title']])
        for key1, value1 in value['specialties'].items():
            for key2, value2 in value1['programs'].items():
                faculty = Faculty(name=value2['title'], points=value2['score'], price=value2['price'],
                                  description=value2['description'],
                                  subject1=value2['subjects'][0], subject2=value2['subjects'][1],
                                  subject3='/'.join(value2['subjects'][2:]))
                university.faculties.append(faculty)
        # print(f'{key}: {value}')
        db.session.add(university)
        db.session.commit()
        session.close()


def f():
    with open('../../static/json/images.json') as json_file:
        data = json.load(json_file)

    new = {}
    for key, value in data.items():
        new[value['name']] = value['image']

    with open('../../static/json/images2.json', 'w', encoding='utf-8') as json_file:
        json.dump(new, json_file)



if __name__ == '__main__':
    data = [
        ['../../static/json/perm_university.json', 'PERM', 'perm'],
        ['../../static/json/moscow_university.json', 'MOSCOW', 'moscow'],
        ['../../static/json/vladivostok_university.json', 'VLADIVOSTOK', 'vladivostok'],
        ['../../static/json/yekaterinburg_university.json', 'YEKATERINBURG', 'yekaterinburg'],
        ['../../static/json/st_petersburg_university.json', 'SANT_PETERSBURG', 'sant_petersburg_university']
    ]
    for elem in data:
        parse_json(elem)
    #create_user()
