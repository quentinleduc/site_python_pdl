#coding: utf8
import MySQLdb
from FormailizeString import formalizeStr

def Equipement(connection, csv_data):
    cursor = connection.cursor()
    not_first = False
    for row in csv_data:
        if(not_first) :
           # print(row[2], row[5])
            args = [int(row[4]), formalizeStr(row[5]), int(row[2])]
            #print args
            cursor.execute('INSERT INTO equipement VALUES(%s, %s, %s)', args)
        else :
            not_first = True
    #close the connection to the database.
    connection.commit()
    cursor.close()
    print "Done Equipements"