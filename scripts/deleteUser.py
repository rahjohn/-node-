#!/usr/bin/python
import subprocess
import sys
import os
import MySQLdb

db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="user",         # your username
                     passwd="cinnamon",  # your password
                     db="it210b")        # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()
cur.execute("SELECT userId FROM users where userName=\'" + sys.argv[1] + "\'")

for row in cur.fetchall():
    #print row[0]
    cur2 = db.cursor()
    # row[0] is userId
    cur2.execute("SELECT imagePath from images where userId=\'" + str(row[0]) + "\'")
    for row2 in cur2.fetchall():
        # row2[0] is imagePath
        os.remove("/home/webadmin/node/code/assets" + str(row2[0]))
    cur3 = db.cursor()
    cur3.execute("DELETE from images where userId=\'" + str(row[0]) + "\'")

cur.execute("DELETE from users where userName=\'" + sys.argv[1] + "\'")

db.commit()
db.close()