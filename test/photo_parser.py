import logging

from flask import Flask, render_template, redirect, make_response, jsonify
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from sqlalchemy import delete, insert
from utils.db_api.models import association_table
from utils.forms import RegisterForm, LoginForm
from utils.db_api import User, University
from utils.db_api import db_session
from flask_restful import reqparse, abort, Api, Resource
from resources import UniversityResource, FacultyListResource, UniversityListResource
import requests
import sqlite3

API_KEYS = ['f010ca449d644b287ac10cfe71a3ddaac00ebb81bc266fd179b03dc492ab24f2',
            '57d25683454640ad37b54ec582d6efb38aa74ea74e38c56e111fa721b59b48b5']


def get_image_link(text):
    from serpapi import GoogleSearch

    params = {
        "q": text,
        "tbm": "isch",
        "ijn": "0",
        "api_key": API_KEYS[0]
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    images_results = results['images_results']
    return images_results[0]['original']


db_file = "../db/database.db"
db_session.global_init(db_file)
session = db_session.create_session()
universities = session.query(University).all()
connection = sqlite3.connect(db_file)
cursor = connection.cursor()

for elem in universities:
    # image = get_image_link(elem.name)
    image = 'link'
    cursor.execute(f"""UPDATE university
                    SET image = '{image}'
                    WHERE id = '{elem.id}'""")
    connection.commit()

connection.close()
session.close()
