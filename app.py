from flask import Flask, render_template, url_for, request
from markupsafe import escape

app = Flask(__name__)


@app.route('/')
def index():
    return 'index' # render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()


@app.route('/user/<username>')
def profile(username):
    return "{}\'s profile".format(escape(username))


with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username="Min Jae"))


if __name__ == '__main__':
    app.run(host='127.0.0.1')
