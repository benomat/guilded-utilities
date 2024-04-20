from gutil import createuser
available=open("available.txt").read().split("\n")
from time import sleep
for i in available:
    if createuser(i): print("Created: "+i)
    else: print("Failed: "+i)