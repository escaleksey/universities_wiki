from config import db
from utils.db_api.models import University, Faculty
import json
from utils.db_api import db_session


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
