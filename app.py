from bottle import route, run, template, static_file, get, request
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

run(host='93.124.34.49',port=8080)