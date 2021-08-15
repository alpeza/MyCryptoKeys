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
        print('Insertando con password')
        cs.addElement(password='hola', name='hola', description='asdf', passphaser='asdf').printm()

    def testInsertSinPasswordUno(self):
        print('Insertando sin password 1')
        cs.addElement(name='segundaEntrada', description='Esta es otra entrad', passphaser='asdf').printm()
        print('Insertando sin password 2 después de que caduque la sesión')
        hnd.sh.closeSession()
        cs.addElement(name='terceraEntrada', description='Esta es deberia de fallar por sesion caducada', passphaser='asdf').printm()



if __name__ == '__main__':
    unittest.main()
