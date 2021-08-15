from tinydb import TinyDB, Query
from datetime import datetime

db = TinyDB('db.json')

def setJSONPath(path):
    global db
    db = TinyDB(path)

def getCurrentDate():
    dateTimeObj = datetime.now()
    timestampStr = dateTimeObj.strftime("%d-%b-%Y %H:%M:%S.%f")
    return timestampStr

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
        raise CustomError("El campo name,description,passphaser han de estar informados")

# --- SELECT
def getAll():
    return db.all()

def getByEnv(env='pro'):
    q = Query()
    return db.search(q.env == env)

def getByName(name=''):
    q = Query()
    if name:
        return db.search(q.name == name)
    else:
        raise CustomError("El campo name ha de estar informado")

# --- UPDATE
def updateByName(env='',name='',description='',passphaser='',note=''):
    q = Query()
    objd = db.search(q.name == name)
    tmpo = objd[0]
    tmpo['env'] = env if env != '' else tmpo['env'] 
    tmpo['description'] = description if description != '' else tmpo['description']
    tmpo['passphaser'] = passphaser if passphaser != '' else tmpo['passphaser']
    tmpo['note'] = note if note != '' else tmpo['note']
    tmpo['update'] = getCurrentDate()
    db.update(tmpo, q.name == name)

# --- DELETE
def deleteByName(name=''):
    q = Query()
    db.remove(q.name == name)