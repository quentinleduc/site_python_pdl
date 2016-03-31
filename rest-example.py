#coding: utf8
from libs.bottle import *
import json
from SqlRequestPy.searchRequest import searchRequest
from SqlRequestPy.completionRequest import completionRequest


'''
        Toute les recherche se ferons à l'adresse mon.domaine.com/search/<param>
        Retourne une matrice formater en JSON
'''
@route('/search/<param>')
def search(param):
    
    result = searchRequest(param)
    
    return json.dumps(result)
    

'''
        Simple auto completion return un array formater en JSON pour tout ce qui commence par <param>
        Accessible à l'adresse mon.domaine.com/completion/<param>
'''
@route('/completion/<param>')
def completion(param):
    
    result = completionRequest(param)
    
    return json.dumps(result)


#####################################################
#               Default     Pages                   #
#####################################################

'''
        Route par defaut !
'''
@route('/')
def index():
    return static_file("index.html", root='vues/')
    

'''
        Route par defaut !
'''
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