from flask import jsonify, render_template
from flask_restful import abort, reqparse, Resource
from utils.db_api import db_session, University


def abort_if_job_not_found(university_id):
    session = db_session.create_session()
    job = session.query(University).get(university_id)
    if not job:
        abort(404, message=f"university {university_id} not found")


class UniversityResource(Resource):
    def get(self, university_id):
        #abort_if_job_not_found(university_id)
        session = db_session.create_session()
        university = session.query(University).get(university_id)
        university = university.__dict__
        u1 = {'title': university['name'],
              'city': university['city']}
        json = jsonify(u1)
        return json


class UniversityListResource(Resource):
    def get(self, city):
        #abort_if_job_not_found(city)
        session = db_session.create_session()
        university = session.query(University).where(University.city == city).all()
        u1 = {}
        for i in range(len(university)):
            university_dict = university[i].__dict__
            u1[i] = {
                'id': university_dict['id'],
                'title': university_dict['name']
            }
        print(city)
        print(u1)
        json = jsonify(u1)
        return json