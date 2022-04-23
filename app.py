from flask import Flask, render_template, redirect
from flask_login import LoginManager, login_user

from utils.forms.user import RegisterForm, LoginForm
from utils.db_api.data.users import User
from utils.db_api.data import db_session

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
app.config['SECRET_KEY'] = 'universities_wiki_key'


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


@app.route('/profile/<int:user_id>')
def profile(user_id):
    params = {}
    params['user_id'] = user_id
    return render_template('profile.html', **params)


@app.route('/login')
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
def reqister():
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
            about=form.about.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


def main():
    # TODO: create database
    db_file = ""
    db_session.global_init(db_file)
    app.run(host="127.0.0.1", port=8080)


if __name__ == '__main__':
    main()
