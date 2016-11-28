#!/usr/bin/python
import subprocess
subprocess.call(["rsync", "-a", "/node/code/assets/images/", "/srv/images/", "--delete"])