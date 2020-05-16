from bottle import route, run, template, static_file, get
@route('/')
def index():
    return template('static/index.html')

@route('/other')
def other():
    return template('static/html/other.html')

@get("/static/css/<filepath:re:.*\.css>")
def css(filepath):
    return static_file(filepath, root="static/css")

run()