# coding: utf8

import csv
import MySQLdb
import codecs

connection = MySQLdb.connect(user='quentinleduc', passwd='', db='c9')
cursor = connection.cursor()

csv_data = csv.reader(file('./csv/installations.csv'))
not_first = False
for row in csv_data:
    if(not_first) :
       # print(row[2], row[5])
        args = [int(row[1]), row[0], row[6]+" "+row[7]+" "+row[5], row[4], row[2], float(row[10]), float(row[9])]
        cursor.execute('INSERT INTO installations VALUES("%s", "%s", "%s", "%s", "%s", "%s", "%s")', args)
    else :
        not_first = True
#close the connection to the database.
connection.commit()
cursor.close()
print "Done"

cursor = connection.cursor()

csv_data = csv.reader(file('./csv/equipements.csv'))
not_first = False
for row in csv_data:
    if(not_first) :
       # print(row[2], row[5])
        args = [int(row[4]), row[5], int(row[2])]
        cursor.execute('INSERT INTO equipement VALUES("%s", "%s", "%s")', args)
    else :
        not_first = True
#close the connection to the database.
connection.commit()
cursor.close()
print "Done"

cursor = connection.cursor()

csv_data = csv.reader(file('./csv/activites.csv'))
not_first = False
for row in csv_data:
    if(not_first) :
       # print(row[2], row[5])
        args = [int(row[4]), row[5]]
        cursor.execute('INSERT INTO activitee VALUES("%s", "%s")', args)
    else :
        not_first = True
not_first = False
for row in csv_data:
    if(not_first) :
       # print(row[2], row[5])
        args2 = [int(row[2]), int(row[4])]
        cursor.execute('INSERT INTO equipement_activitee VALUES("%s", "%s")', args2)
    else :
        not_first = True
#close the connection to the database.
connection.commit()
cursor.close()
print "Done"

    
    
    