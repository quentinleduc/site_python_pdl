#coding: utf8
import MySQLdb
'''
        Simple fichier python pour configurer la connection à la base mysql
'''
def connection():
    return MySQLdb.connect(user='quentinleduc', passwd='quentinleduc', db='c9',  charset='utf8')