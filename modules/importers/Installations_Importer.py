#coding: utf8
import MySQLdb
from FormailizeString import formalizeStr

'''
        Fonction qui importe le fichier csv installations dans notre base de donnée
'''

def Installation(connection, csv_data):
    cursor = connection.cursor()
    not_first = False
    for row in csv_data:
        if(not_first) :
           # print(row[2], row[5])
            args = [int(row[1]), formalizeStr(row[0]), formalizeStr(row[6]+" "+row[7]+" "+row[5]), row[4], formalizeStr(row[2]), float(row[10]), float(row[9])]
            #print args
            cursor.execute('INSERT INTO installations VALUES(%s, %s, %s, %s, %s, %s, %s)', args)
        else :
            not_first = True
    #close the connection to the database.
    connection.commit()
    cursor.close()
    print "Done Installations"