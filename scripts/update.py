#!/usr/bin/python
import MySQLdb
import subprocess

db = MySQLdb.connect(host="localhost",
                     user="guest",
                     passwd="guest",
                     db="it210b")
cur = db.cursor()
cur.execute("SELECT imagePath FROM images where uploaded=0")
cur2 = db.cursor()
for row in cur.fetchall():
    subprocess.call(["wget", "-P", "/node/code/assets/images/", "-r", "-nH", "--cut-dirs=2", "--no-parent", "http://192.168.217.130/images/edit/" + row[0]])
    #subprocess.call(["rm", "/node/code/assets/images/index.html"])
    cur2.execute("UPDATE images set uploaded=1 WHERE imagePath=" + "\'" + row[0] + "\'")
db.commit()
db.close()
