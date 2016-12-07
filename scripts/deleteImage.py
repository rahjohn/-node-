#!/usr/bin/python
import subprocess
import sys
import os
import MySQLdb

db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="guest",         # your username
                     passwd="guest",  # your password
                     db="it210b")        # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()
cur.execute("SELECT imagePath from images where altText=\'" + str(sys.argv[1]) + "\'")
for row in cur.fetchall():
    os.remove("/node/code/assets" + str(row[0]))

cur.execute("DELETE from images where altText=\'" + sys.argv[1] + "\'")

db.commit()
db.close()