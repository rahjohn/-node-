#!/usr/bin/python
import subprocess
subprocess.call(['/usr/bin/mysqldump', '--all-databases', '-u', 'guest', '-pguest', '--result-file=/srv/database/backup.sql'])