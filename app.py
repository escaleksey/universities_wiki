from flask import Flask, render_template

app = Flask(__name__)


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


def main():
    app.run()


if __name__ == '__main__':
    main()