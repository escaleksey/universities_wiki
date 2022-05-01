import logging

from flask import Flask, render_template, redirect, make_response, jsonify
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from utils.forms import RegisterForm, LoginForm
from utils.db_api import User, University, association_table
from utils.db_api import db_session
from flask_restful import reqparse, abort, Api, Resource
from resources import UniversityResource
import requests
import sqlite3


app = Flask(__name__)
api = Api(app)
login_manager = LoginManager()
login_manager.init_app(app)
app.config['SECRET_KEY'] = 'universities_wiki_key'


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).filter(User.id == user_id).first()


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/universities/<city>')
def universities(city):
    params = {
        'city': city
    }
    return render_template('list_universities.html', **params)


@app.route('/university/<int:university_id>')
def university(university_id):
    params = requests.get(f"http://127.0.0.1:8080/api/university/{university_id}").json()
    return render_template('university_page.html', **params)


@app.route('/profile')
def profile():
    universities_data = []
    user_id = current_user.id
    db_sess = db_session.create_session()
    user = db_sess.query(User).filter(User.id == user_id).first()

    result = db_sess.query(User).filter(User.id == user_id).first()
    for elem in result.universities:
        universities_data.append(elem.name)


    params = {
        'user_id': user_id,
        'name': user.name,
        'email': user.email,
        'age': user.age,
        'universities': universities_data
    }
    return render_template('profile.html', **params)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html', message="Неправильный логин или пароль", form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация', form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация', form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            name=form.name.data,
            email=form.email.data,
            age=form.age.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


def main():
    db_file = "db/database.db"
    db_session.global_init(db_file)
    api.add_resource(UniversityResource, "/api/university/<int:university_id>")
    app.run(host="127.0.0.1", port=8000)


if __name__ == '__main__':
    main()
