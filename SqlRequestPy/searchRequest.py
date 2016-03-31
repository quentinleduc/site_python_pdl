#coding: utf8
from mysqlConnection import connection
from modules.importers.FormailizeString import formalizeStr

'''
        La fonction searchRequest permet de faire la recherche d'une activité dans une ville
        On récupère ce qui a été entré dans la barre de recherche 
        On récupère d'abord l'ID de l'activité
        Puis on récupère l'ID des équipements possible pour cette activité
        On récupère le numéro de l'installation des différents équipements
        On renvoie toutes les installations de la ville où l'on peut pratiquer l'activité
'''


def searchRequest(param):
    conn = connection()
    cursor = conn.cursor()
    rep = formalizeStr(param)
    recher = rep.split() #on transforme la chaine de caractère en tableau de caractère pour pouvoir traiter chaque élément
    idAct = None
    instal = set()
    
    for r in recher:
        cursor.execute("SELECT DISTINCT ID FROM activitee WHERE nom LIKE '"+r+"%';")
        tmp = cursor.fetchone()
        if(tmp):
            idAct = tmp[0]
            break;
    
    cursor.execute("SELECT DISTINCT id_equ FROM equipement_activitee WHERE id_act="+str(idAct)+";")
    idEqu = cursor.fetchall()
    
    numInstall = []
    for i in idEqu:
        cursor.execute("SELECT DISTINCT num_install FROM equipement WHERE ID="+str(i[0])+";")
        numInstall.append(cursor.fetchone()[0])
    
    for t in recher:
        cursor.execute("SELECT DISTINCT * FROM installations WHERE ville LIKE '"+t+"%';")
        if(cursor.fetchall()):
            for n in numInstall:
                cursor.execute("SELECT DISTINCT nom, adresse, code_postal, ville FROM installations WHERE ID="+str(n)+" and ville LIKE '"+t+"%';")
                result = cursor.fetchall()
                if(result):
                    for row in result:
                        instal.add(row)
                        
    return list(instal)
        