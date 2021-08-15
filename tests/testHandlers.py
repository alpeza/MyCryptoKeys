import unittest
from time import sleep

import sys
import os

dname = os.path.dirname(__file__)
relpath = os.path.join(dname, '../MyCryptoKeys')
abspath = os.path.abspath(relpath)
sys.path.insert(0, abspath)
from handlers import FileDBHandler as fh
from handlers import SessionHandler as sh

class MainTestSuite(unittest.TestCase):
    """Basic test cases."""
    def testFH(self):
        for a in range(10):
            print('---------------------------------------')
            print('Insertando')
            fh.addEntry(env='test', name='clave1', description='pepep', passphaser='asdf asdf asdf asdf asdf  asdf ')
            print('Select')
            print(fh.getByName(name='clave1'))
            print('Update')
            fh.updateByName(name='clave1', description='Otra descripción', passphaser='otra frase frase')
            print('Select')
            print(fh.getByName(name='clave1'))
            print('Delete')
            print(fh.deleteByName(name='clave1'))

    def testSession(self):
        timeout=0.5
        sh.startSession('asdff',timeout=timeout)
        if sh.isLoged():
            print('Esta logado: ' + sh.getPassword())
        else:
            print('No Esta logado')
        print('Esperando varios minutos a que finalice la sessionn ...')
        sleep(60 * (timeout + 3))
        if sh.isLoged():
            print('Esta logado: ' + sh.getPassword())
        else:
            print('No Esta logado')


if __name__ == '__main__':
    unittest.main()
