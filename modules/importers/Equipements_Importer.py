#coding: utf8
import MySQLdb
from FormailizeString import formalizeStr

'''
        Fonction qui importe le fichier csv equipements dans notre base de donnée
'''

def Equipement(connection, csv_data):
    cursor = connection.cursor()
    not_first = False
    for row in csv_data:
        if(not_first) :
            if(row[2] and row[4] and row[5]) :
                if(isinstance(row[2], int) and isinstance(row[4], int)):
                    args = [int(row[4]), formalizeStr(row[5]), int(row[2])]
                    cursor.execute('INSERT INTO equipement VALUES(%s, %s, %s)', args)
                else :
                    raise ValueError('Erreur les valeur ne sont pas bien formatées - Collones 2 et 4 ne sont pas des int !!!')
            else :
                raise ValueError('Erreur les valeur ne sont pas bien formatées - Collones 2, 4 et 5 sont vide !!!')
        else :
            not_first = True
    #close the connection to the database.
    connection.commit()
    cursor.close()
    print "Done Equipements"