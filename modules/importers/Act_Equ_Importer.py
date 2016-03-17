#coding: utf8
import MySQLdb
from FormailizeString import formalizeStr

def Act_Equ(connection, csv_data):
    cursor = connection.cursor()
    not_first = False
    for row in csv_data:
        if(not_first) :
            if(len(row) > 4):
                if(row[2] and row[4]) :
                    args = [int(row[2]), int(row[4])]
                    cursor.execute('SELECT * FROM equipement_activitee WHERE id_equ=%s and id_act=%s', args)
                    rep = cursor.fetchall()
                    if(not rep):
                        cursor.execute('INSERT INTO equipement_activitee VALUES(%s, %s)', args)
        else :
            not_first = True
    #close the connection to the database.
    connection.commit()
    cursor.close()
    print "Done Equipements / Activities"