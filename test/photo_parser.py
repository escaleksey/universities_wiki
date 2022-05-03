import json
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
            '57d25683454640ad37b54ec582d6efb38aa74ea74e38c56e111fa721b59b48b5',
            '896da93ecb3403d3793e2e2dfd4ea019879a4294b88f08bd482774f5cea194fc']


def get_image_link(text, api_key):
    from serpapi import GoogleSearch

    params = {
        "q": text,
        "tbm": "isch",
        "ijn": "0",
        "api_key": api_key
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    images_results = results['images_results']
    return images_results[0]['original']


def full_data_base():
    db_file = "../db/database.db"
    db_session.global_init(db_file)
    session = db_session.create_session()
    universities = session.query(University).all()
    connection = sqlite3.connect(db_file)
    cursor = connection.cursor()

    counter = 0
    result_json = dict()
    image = 'any'
    for elem in universities:
        try:
            if counter < 66:
                image = get_image_link(elem.name, API_KEYS[0])
            elif counter < 166:
                image = get_image_link(elem.name, API_KEYS[1])
            elif counter < 266:
                image = get_image_link(elem.name, API_KEYS[2])
            else:
                break

        except Exception:
            with open('../static/json/images.json', 'w') as file:
                json.dump(result_json, file)

        counter += 1
        print(f'{counter}: {elem.name}, {image}')

        result_json[elem.id] = {
            'id': elem.id,
            'name': elem.name,
            'city': elem.city,
            'image': image
        }

        cursor.execute(f"""UPDATE university
                        SET image = '{image}'
                        WHERE id = '{elem.id}'""")
        connection.commit()

    with open('../static/json/images.json', 'w') as file:
        json.dump(result_json, file)

    connection.close()
    session.close()


if __name__ == '__main__':
    # full_data_base()
    pass
