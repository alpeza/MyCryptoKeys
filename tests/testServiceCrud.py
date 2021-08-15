import unittest
from time import sleep

import sys
import os,time

dname = os.path.dirname(__file__)
relpath = os.path.join(dname, '../MyCryptoKeys')
abspath = os.path.abspath(relpath)
sys.path.insert(0, abspath)
from services import crudService as cs
import handlers as hnd

class MainTestSuite(unittest.TestCase):
    """Basic test cases."""
    def testInsertConPassword(self):
        try:
            hnd.cyh.remove(hnd.ch.storagefile)
            hnd.cyh.remove(os.path.join(hnd.ch.config['localpath'], '.session'))
        except Exception as e:
            print(e)
            pass


        print('Insertando con password')
        cs.addElement(password='hola', name='hola', description='asdf', passphaser='asdf').printm()

    def testInsertSinPasswordUno(self):
        # Insertamos siin password
        print('Insertando sin password 1')
        cs.addElement(name='segundaEntrada', description='Esta es otra entrad', passphaser='asdf').printm()
        print('Insertando sin password 2 después de que caduque la sesión')
        hnd.sh.closeSession()
        cs.addElement(name='terceraEntrada', description='Esta es deberia de fallar por sesion caducada', passphaser='asdf').printm()

        # Leemos 
        om = cs.list(password='hola',mode='all')
        print(om.message)

if __name__ == '__main__':
    unittest.main()
