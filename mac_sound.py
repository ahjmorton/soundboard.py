#!/opt/local/bin/python

import subprocess

def play(file_name) :
    print("Playing file %s" % file_name)
    subprocess.Popen(["afplay", file_name]).wait()

def can_play(root, filename) :
    return True
