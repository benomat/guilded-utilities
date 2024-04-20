from gutil import *
triednames=(open("available.txt").read()+open("unavailable.txt").read()).split("\n")


usernames=open("1").read().split("\n")#"".split(",")
availablefile=open("available.txt","a")
unavailablefile=open("unavailable.txt","a")
for user in usernames:
    if user not in triednames:
        if available(user): print(user); availablefile.write(user+"\n")
        else: unavailablefile.write(user+"\n")
availablefile.close()
unavailablefile.close()