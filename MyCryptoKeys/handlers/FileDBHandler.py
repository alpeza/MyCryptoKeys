from tinydb import TinyDB, Query
from datetime import datetime

db = None

def setJSONPath(path):
    global db
    db = TinyDB(path)

def getCurrentDate():
    dateTimeObj = datetime.now()
    timestampStr = dateTimeObj.strftime("%d-%b-%Y %H:%M:%S.%f")
    return timestampStr

class BadData(Exception):
    pass

# --- INSERT
def addEntry(env='pro',name='',description='',passphaser='',note=''):
    if env and name and description and passphaser:
        db.insert({
            'env': env, 
            'name': name,
            'description': description,
            'passphaser': passphaser,
            'note': note,
            'date': getCurrentDate()
        })
    else:
        raise BadData("El campo name,description,passphaser han de estar informados")

# --- SELECT
def getAll():
    global db
    ret = db.all()
    db.close()
    return ret

def getByEnv(env='pro'):
    global db
    q = Query()
    ret = db.search(q.env == env)
    db.close()
    return ret

def getByName(name=''):
    global db
    q = Query()
    if name:
        ret = db.search(q.name == name)
        db.close()
        return ret
    else:
        raise BadData("El campo name ha de estar informado")

# --- UPDATE
def updateByName(env='',name='',description='',passphaser='',note=''):
    global db
    q = Query()
    objd = db.search(q.name == name)
    tmpo = objd[0]
    tmpo['env'] = env if env != '' else tmpo['env'] 
    tmpo['description'] = description if description != '' else tmpo['description']
    tmpo['passphaser'] = passphaser if passphaser != '' else tmpo['passphaser']
    tmpo['note'] = note if note != '' else tmpo['note']
    tmpo['update'] = getCurrentDate()
    db.update(tmpo, q.name == name)
    db.close()

# --- DELETE
def deleteByName(name=''):
    global db
    q = Query()
    db.remove(q.name == name)
    db.close()