import jwt
import datetime,json,os
key='sdv3oasjvvi4safjjo'
session_timeout_minutes=10
import os.path
import os
from . import ConfigHandler as ch
session_file=os.path.join(ch.config['localpath'], '.session')

def startSession(password,timeout=session_timeout_minutes):
    encoded_jwt = jwt.encode({"exp": datetime.datetime.utcnow() + datetime.timedelta(minutes = timeout), 
    "password":password}, key, algorithm="HS256")
    with open(session_file, 'w') as outfile:
        json.dump(encoded_jwt, outfile)

def isLoged():
    if getPassword():
        return True 
    else:
        return False

def getPassword():
    if not os.path.isfile(session_file):
        return False
    with open(session_file) as json_file:
        encoded_jwt = json.load(json_file)
    try:
        deco = jwt.decode(encoded_jwt, key, algorithms=["HS256"])
        return deco['password']
    except Exception as e:
        os.remove(session_file)
        return False

def closeSession():
    if not os.path.isfile(session_file):
        os.remove(session_file)

