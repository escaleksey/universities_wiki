from flask import jsonify
from flask_restful import abort, Resource
from utils.db_api import db_session
from utils.db_api.models import University


def abort_if_job_not_found(university_id):
    session = db_session.create_session()
    job = session.query(University).get(university_id)
    if not job:
        abort(404, message=f"university {university_id} not found")


class UniversityResource(Resource):
    def get(self, university_id):
        abort_if_job_not_found(university_id)
        session = db_session.create_session()
        university = session.query(University).get(university_id)
        university = university.__dict__
        u1 = {
            'title': university['name'],
            'city': university['city'],
            # TODO: Спарсить адреса универов
            'address': 'address',
        }
        json = jsonify(u1)
        session.close()
        return json


class UniversityListResource(Resource):
    def get(self, city):
        # abort_if_job_not_found(city)
        session = db_session.create_session()
        university = session.query(University).where(University.city == city).all()
        u1 = {}
        for i in range(len(university)):
            university_dict = university[i].__dict__
            u1[i] = {
                'id': university_dict['id'],
                'title': university_dict['name'],
                # TODO: картинки!
                'image': "https://m.rosvuz.ru/uploads/partition120/unit/1/3035d394be7c049c67ff3a7036db851c.800_415.jpg?code=MjYwNTguODAwXzQxNQ=="
            }
        json = jsonify(u1)
        session.close()
        return json
