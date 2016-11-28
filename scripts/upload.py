#!/usr/bin/python
import MySQLdb

db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="guest",         # your username
                     passwd="guest",  # your password
                     db="it210b")        # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()

# Use all the SQL you like
cur.execute("SELECT uploaded FROM images WHERE uploaded = 1")

db.close()