import requests
from time import sleep
from os import system,remove
def available(user):
    url = f"https://www.guilded.gg/api/subdomains/u/{user}"

    response = requests.request("GET", url)

    if response.text=="{}": return True
    elif response.text.startswith('{"code'): print("toofast"); sleep(6); available(user)
    else: print(response.text);return False

def createuser(user):
    url = "https://www.guilded.gg/api/users"

    querystring = {"type":"email"}

    payload = {
        "extraInfo": {"platform": "desktop"},
        "name": user,
        "email": f"{user}@whimper.xyz",
        "password": f"{user}@woahyoufoundme!!",
        "fullName": user
    }


    response = requests.request("POST", url, json=payload, params=querystring)

    if response.text.startswith('{"user'): print(response.text)
    elif response.text=='{"code":"BadRequest","message":"Name is too long."}':print(f"Name ({user}) is too long");return False
    elif response.text=='{"code":"Conflict","message":"User with this email already exists."}': print(f"{user}@whimper.xyz");print(payload);return False
    elif response.text.startswith('{"code'): print("expecting toofast: "+response.text); sleep(15); createuser(user)
    else: print("idk"+response.text); return False
    remove("temp.txt")
    system(f"curl -s https://www.guilded.gg/u/{user} >> temp.txt")
    temp=open("temp.txt").read()
    if temp.split(">")[4].split("&")[0] == user: return True
    else: print("creation failed, trying again in 30 seconds");return False#sleep(30);createuser(user)


def checkuser(user):#this does the same thing as available, just without using the api
    remove("temp.txt")
    system(f"curl -s https://www.guilded.gg/u/{user} >> temp.txt")
    temp=open("temp.txt").read()
    if temp.split(">")[4].split("&")[0] == user: return True
    else: return False