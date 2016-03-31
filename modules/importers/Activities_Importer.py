#coding: utf8
import MySQLdb
from FormailizeString import formalizeStr

'''
        Fonction qui importe le fichier csv activites dans notre base de donnée
'''

def Activity(connection, csv_data):
    cursor = connection.cursor()
    not_first = False
    for row in csv_data:
        if(not_first) :
            if(len(row) > 5):
                if(row[4] and row[5]) :
                    if(isinstance(row[4], int)) :
                        args1 = [int(row[4])]
                        cursor.execute('SELECT ID FROM activitee WHERE ID=%s', args1)
                        rep = cursor.fetchall()
                        if(not rep):
                            args = [int(row[4]), formalizeStr(row[5])]
                            cursor.execute('INSERT INTO activitee VALUES(%s, %s)', args)
                    else :
                        raise ValueError('Erreur les valeur ne sont pas bien formatées - Collones 4 ne sont pas des int !!!')
                else :
                    raise ValueError('Erreur les valeur ne sont pas bien formatées - Collones 4 et 5 sont vide !!!')
        else :
            not_first = True
    connection.commit()
    cursor.close()
    print "Done Activities"