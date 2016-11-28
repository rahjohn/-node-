#!/usr/bin/python
import subprocess
subprocess.call(["wget", "-P", "/node/code/assets/images/", "-r", "-nH", "--cut-dirs=2", "--no-parent", "http://192.168.217.130/images/"])
subprocess.call(["rm", "/node/code/assets/images/index.html"])