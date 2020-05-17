from bottle import route, run, template, static_file, get, request
from sys import argv
import os
@route('/')
def index():
    return template('static/html/index.html')

@route('/other')
def other():
    return template('static/html/other.html')

@get("/static/css/<filepath:re:.*\.css>")
def css(filepath):
    return static_file(filepath, root="static/css")

@route('/result', method='POST')
def do_login():
    first = request.forms.get('username')
    second = request.forms.get('password')
    return template('static/html/result.html',first=first,seconde=second)

if os.environ.get('APP_LOCATION') == 'heroku':
    run(host="0.0.0.0", port=argv[1])
else:
    run(host='localhost', port=8080, debug=True)