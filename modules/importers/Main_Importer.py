#coding: utf8
import csv
import MySQLdb
from Installations_Importer import Installation
from Equipements_Importer import Equipement
from Activities_Importer import Activity
from Act_Equ_Importer import Act_Equ
from mysqlConnection import connection

import os
 
dir_path = os.path.dirname(os.path.abspath(__file__))

def purge():
    conn = MySQLdb.connect(user='quentinleduc', passwd='quentinleduc', db='c9',  charset='utf8')
    cursor = conn.cursor()
    ############################################################
    #   Vidange des tables ^^
    cursor.execute('DROP TABLE equipement_activitee')
    cursor.execute('DROP TABLE activitee')
    cursor.execute('DROP TABLE equipement')
    cursor.execute('DROP TABLE installations')
    cursor.execute("CREATE TABLE IF NOT EXISTS `activitee` (`ID` int(11) NOT NULL,`nom` varchar(256) NOT NULL,PRIMARY KEY (`ID`)) ENGINE=InnoDB DEFAULT CHARSET=utf8;")
    cursor.execute("CREATE TABLE IF NOT EXISTS `equipement` (`ID` int(11) NOT NULL,`nom` varchar(256) NOT NULL,`num_install` int(11) NOT NULL,PRIMARY KEY (`ID`),KEY `num_install` (`num_install`)) ENGINE=InnoDB DEFAULT CHARSET=utf8;")
    cursor.execute("CREATE TABLE IF NOT EXISTS `equipement_activitee` (`id_equ` int(11) NOT NULL,`id_act` int(11) NOT NULL,PRIMARY KEY (`id_equ`,`id_act`),KEY `id_act` (`id_act`)) ENGINE=InnoDB DEFAULT CHARSET=utf8;")
    cursor.execute("CREATE TABLE IF NOT EXISTS `installations` (`ID` int(11) NOT NULL,`nom` varchar(256) NOT NULL,`adresse` varchar(256) NOT NULL,`code_postal` varchar(10) NOT NULL,`ville` varchar(40) NOT NULL,`latitude` float NOT NULL,`longitude` float NOT NULL,PRIMARY KEY (`ID`)) ENGINE=InnoDB DEFAULT CHARSET=utf8;")
    conn.commit()
    cursor.close()
    print 'Done Vidange'
    ############################################################
    
def importall():
    conn = connection()
    
    Installation(conn, csv.reader(file(dir_path+'/../csv/installations.csv')) )
    Equipement(conn, csv.reader(file(dir_path+'/../csv/equipements.csv')) )
    Activity(conn, csv.reader(file(dir_path+'/../csv/activites.csv')) )
    Act_Equ(conn, csv.reader(file(dir_path+'/../csv/activites.csv')) )
    