from flask import Flask, url_for
from markupsafe import escape

app = Flask(__name__)


@app.route('/')
def hello():
    return '<h1>Hello Totoro!</h1><img src="static/img/totoro.gif">'


@app.route('/home')
@app.route('/index')
def index():
    return 'WelCome to My Flask'


@app.route('/user/<name>')
def user_page(name):
    return f'User: {escape(name)}'


@app.route('/test')
def test_url_for():
    print(url_for('hello'))
    print(url_for('user_page', name='zishuQ'))
    print(url_for('user_page', name='purple'))
    print(url_for('test_url_for'))
    print(url_for('test_url_for', num=2))
    """
    /
    /user/zishuQ
    /user/purple
    /test
    /test?num=2
    """
    return 'Test page'


if __name__ == '__main__':
    app.run()
