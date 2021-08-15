import handlers as hnd
import traceback


def checkIfLogged(password):
    om = hnd.om.OMessage()
    om.isOK = True
    # 1.- Validamos si el usuario está logado
    if not hnd.sh.isLoged() and not password:
        om.isOK = False 
        om.message = 'El usuario no está logado, ha de introducirse el password'
        return om
    elif hnd.sh.isLoged() and not password:
        password = hnd.sh.getPassword()
        if not password:
            om.isOK = False
            om.message = 'Error al recuperar el password'
            return om
    om.data = {"password": password}
    return om

def list(password='',mode='all',name=''):
    om = hnd.om.OMessage()
    retom = checkIfLogged(password)
    if not retom.isOK:
        return retom
    password = retom.data['password']
    if not hnd.cyh.existsFile(hnd.ch.storagefile):
        om.message = 'No existe ningún fichero de key, inicie un nuevo billetero'
        om.isOK = False
        return om
    else:
        try:
            jsonfile = hnd.ch.storagefile + '_tmp.json'
            hnd.cyh.decryptFile(hnd.ch.storagefile,jsonfile,password)
            hnd.fh.setJSONPath(jsonfile)
            if mode == 'all':
                om.message = hnd.fh.getAll()
            elif mode == 'name':
                om.message = hnd.fh.getByName(name=name)
        except Exception as e:
            om.isOK = False
            om.message = str(e)
            om.exception = str(traceback.format_exc())
        finally:
            try:
                hnd.cyh.remove(jsonfile)
                return om
            except Exception as e:
                pass


def addElement(password='',env='pro',name='',description='',passphaser='',note=''):
    # Añade una nueva entrada. 
    om = hnd.om.OMessage()

    retom = checkIfLogged(password)
    if not retom.isOK:
        return retom

    password = retom.data['password']
    jsonfile = hnd.ch.storagefile + '_tmp.json'
    # 2.- Si no existe fichero de storage
    if not hnd.cyh.existsFile(hnd.ch.storagefile):
        # El fichero de datos no existe. Crearemos uno nuevo
        try:
            # Insertamos la nueva clave
            hnd.fh.setJSONPath(jsonfile)
            hnd.fh.addEntry(env=env, name=name, description=description, passphaser=passphaser, note=note)
            # Encriptamos el fichero
            hnd.cyh.encryptFile(jsonfile,password,newname=hnd.ch.storagefile)
            # Iniciamos session
            hnd.sh.startSession(password)
        except Exception as e:
            om.isOK = False
            om.message = str(e)
            om.exception = str(traceback.format_exc())
        finally:
            hnd.cyh.remove(hnd.ch.storagefile + '_tmp.json')
            return om

    # 3.- En caso de que ya exista un fichero de storage
    # Desencriptamos
    try:
        hnd.cyh.decryptFile(hnd.ch.storagefile,jsonfile,password)
        hnd.fh.setJSONPath(jsonfile)
        hnd.fh.addEntry(env=env, name=name, description=description, passphaser=passphaser, note=note)
        # Encriptamos el fichero
        hnd.cyh.encryptFile(jsonfile,password,newname=hnd.ch.storagefile)
        hnd.sh.startSession(password)
    except Exception as e:
        om.isOK = False
        om.message = str(e)
        om.exception = str(traceback.format_exc())
    finally:
        try:
            hnd.cyh.remove(jsonfile)
        except Exception as e:
            pass
       

    return om