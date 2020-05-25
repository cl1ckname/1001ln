from bottle import route, run, static_file, get, request
from lib import *
from sys import argv
from ml import solve
import os

@get('/favicon.ico')
def favicon():
    return static_file('favicon.ico','static/img/')

@route('/')
def index():
    return template('static/html/index.html', 'DiploDoc')

@route('/other')
def other():
    return template('static/html/other.html')

@route('/test')
def test():
    return template('static/html/test.html', 'Тест')

@route('/doctors')
def doctors():
    return template('static/html/doctors.html', 'Наши врачи')

@get("/static/css/<filepath:re:.*\.css>")
def css(filepath):
    return static_file(filepath, root="static/css")

@route('/result', method='POST')
def do_login():
    first = int(request.forms.get('radio-button'))
    second = int(request.forms.get('radio-button1'))
    third = int(request.forms.get('radio-button2'))
    n = int(solve(first,second,third)[0])
    answer = d[n]
    print(n,answer)

    return template('static/html/result.html','Результат',answer=answer[0],adress=answer[1], describe=answer[2])

@route('/result')
def bad_res():
    return template('static/html/result.html','Уйди',answer='Хакер',adress='https://cs.pikabu.ru/post_img/2013/10/27/11/1382897680_599400827.jpg')

if os.environ.get('APP_LOCATION') == 'heroku':
    run(host="0.0.0.0", port=argv[1])
else:
    run(host='localhost', port=8080, debug=True)