from libs.bottle import route, template, run

@route('/in')
def index(name):
    
    return template("<b>Hello {{name}}!", name=name)

run(host='0.0.0.0', port=8080)