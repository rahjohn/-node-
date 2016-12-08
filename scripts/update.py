#!/usr/bin/python
import MySQLdb
import subprocess
import os
import PIL
from PIL import Image

db = MySQLdb.connect(host="localhost",
                     user="guest",
                     passwd="guest",
                     db="it210b")
cur = db.cursor()
cur.execute("SELECT imagePath FROM images where uploaded=0")
cur2 = db.cursor()
print "something"
for row in cur.fetchall():
    if subprocess.call(["wget", "-cP", "/tmp/", "http://192.168.230.126/images/edit/" + os.path.basename(row[0])]) == 0:
    #subprocess.call(["rm", "/node/code/assets/images/index.html"])
	img = Image.open("/tmp/" + os.path.basename(row[0]))
        basewidth = 500
        wpercent = basewidth / float(img.size[0])
        hsize = int((float(img.size[1]) * float(wpercent)))
        img2 = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
        img.close()
        try: 
            img2.save("/node/code/assets/images/" + os.path.basename(row[0]))
        except:
            pass
        else:
            cur2.execute("UPDATE images set uploaded=1 where imagePath=\'" + row[0] + "\'")
            os.remove("/tmp/" + os.path.basename(row[0]))
db.commit()
db.close()
