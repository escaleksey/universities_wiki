from flask import jsonify, render_template
from flask_restful import abort, reqparse, Resource
from utils.db_api import db_session, Faculty


def abort_if_job_not_found(university_id):
    session = db_session.create_session()
    job = session.query(Faculty).get(university_id)
    if not job:
        abort(404, message=f"university {university_id} not found")


class FacultyListResource(Resource):
    def get(self, university_id):
        abort_if_job_not_found(university_id)
        session = db_session.create_session()
        university = session.query(Faculty).where(Faculty.university_id == university_id).all()
        u1 = {}
        for i in range(len(university)):
            university_dict = university[i].__dict__
            u1[i] = {
                'name': university_dict['name'],
                'points': university_dict['points'],
                'price': university_dict['price'],
                'description': university_dict['description'],
                'subject1': university_dict['subject1'],
                'subject2': university_dict['subject2'],
                'subject3': university_dict['subject3']
            }

        json = jsonify(u1)
        session.close()
        return json
