from libs.bottle import route, template, run

@route('/recherche/<name>')
def index(name):
    return "Hello {{name}}"

run(host='0.0.0.0', port=8081)