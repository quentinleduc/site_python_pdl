#coding: utf8
from mysqlConnection import connection
from modules.importers.FormailizeString import formalizeStr

'''
        La fonction completionRequest est notre fonction de completion pour une activité ou une ville
        Retourne les activités et les villes qui dont le nom commence par ce qui est entré en paramètre
        On récupère 10 villes et 10 activités
        On les ajoute dans un tableau puis on renvoie ce tableau
'''

def completionRequest(param):
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
    
    return result