from libs.bottle import *
import MySQLdb
import json
from modules.importers.FormailizeString import formalizeStr


def connection():
    return MySQLdb.connect(user='quentinleduc', passwd='quentinleduc', db='c9',  charset='utf8')
    
@route('/search/<param>')
def search(param):
    
    result = []
    
    return json.dumps(result)
    
@route('/completion/<param>')
def completion(param):
    conn = connection()
    cursor = conn.cursor()
    ask = formalizeStr(param)
    cursor.execute("SELECT DISTINCT ville FROM installations WHERE ville LIKE '"+ask+"%' LIMIT 10;")
    ville = cursor.fetchall()
    
    cursor.execute("SELECT DISTINCT nom FROM activitee WHERE nom LIKE '"+ask+"%' LIMIT 10;")
    act = cursor.fetchall()
    
    cities = []
    for row in ville:
        cities.append(row[0])
    
    activities = []
    for row in act:
        activities.append(row[0])
        
    cities.sort()
    activities.sort()
    
    result = []
    result.append(cities)
    result.append(activities)
    
    return json.dumps(result)



#####################################################
#               Default     Pages                   #
#####################################################
@route('/')
def index():
    return static_file("index.html", root='vues/')
    
@route('/<filename:path>')
def index_path(filename):
    return static_file(filename, root='vues/')

  
####################################################
#           Phpmyadmin     Pages                   #
####################################################
#@route('/phpmyadmin/<filename:path>')
#def phpmyadmin(filename):
#    return static_file(filename, root='/usr/share/phpmyadmin/')
    
    


run(host='0.0.0.0', port=8080)