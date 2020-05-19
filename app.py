from bottle import route, run, template, static_file, get, request
from sys import argv
from ml import solve
import os

d = {
    1: ('Диплодок', 'https://img3.goodfon.com/original/2560x1440/5/4c/kinder-syurpriz-igrushka-trava.jpg'),
    2: ('Тиранозавр','https://im0-tub-ru.yandex.net/i?id=48782499d25bb29dbd75adc029f31d78&n=13'),
    3: ('Антоха Карцев','https://sun9-18.userapi.com/c849020/v849020892/39b41/BIc2v6uq9eo.jpg')}

@route('/')
def index():
    return template('static/html/index.html')

@route('/other')
def other():
    return template('static/html/other.html')

@route('/test')
def test():
    return template('static/html/test.html')

@get("/static/css/<filepath:re:.*\.css>")
def css(filepath):
    return static_file(filepath, root="static/css")

@route('/result', method='POST')
def do_login():
    first = int(request.forms.get('radio-button'))
    second = int(request.forms.get('radio-button1'))
    third = int(request.forms.get('radio-button2'))
    answer = d[int(solve(first,second,third)[0])]
    return template('static/html/result.html',answer=answer[0],adress=answer[1])

if os.environ.get('APP_LOCATION') == 'heroku':
    run(host="0.0.0.0", port=argv[1])
else:
    run(host='localhost', port=8080, debug=True)