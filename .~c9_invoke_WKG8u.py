from libs.bottle import route, template, run

@route('/')
def index(name):
    
    return template("<b>Hello {{name}}!", name=name)
run(host='localho', port=8081)
run(host='0.0.0.0', port=8080)