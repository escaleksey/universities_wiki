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
        abort_if_job_not_found(university_id)
        session = db_session.create_session()
        university = session.query(University).get(university_id)
        university = university.__dict__
        u1 = {'title': university['name'],
              'city': university['city']}
        print(u1)
        json = jsonify(u1)
        return json