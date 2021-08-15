import pyAesCrypt
from os import stat, remove
bufferSize = 64 * 1024
import yaml
import os.path,base64

def encryptFile(file,password):
    # encryption/decryption buffer size - 64K
    # with stream-oriented functions, setting buffer size is mandatory
    # encrypt
    with open(file, "rb") as fIn:
        with open(file+".aes", "wb") as fOut:
            pyAesCrypt.encryptStream(fIn, fOut, password, bufferSize)


def decrypt2Mem(file,password):
    with open(file, "rb") as fIn:
        encFileSize = stat(file).st_size
        try:
            with open('tmpdata.txt', "wb") as fOut:
                # decrypt file stream
                pyAesCrypt.decryptStream(fIn, fOut, password, bufferSize, encFileSize)

            with open('tmpdata.txt') as json_file:
                data = yaml.load(json_file, Loader=yaml.FullLoader)
                remove('tmpdata.txt')
                return data
        except ValueError as e:
            # remove output file on error
            remove('tmpdata.txt')
            raise e

def decryptFile(file,password):
    with open(file+".aes", "rb") as fIn:
        encFileSize = stat(file + ".aes").st_size
        try:
            with open(file+".json", "wb") as fOut:
                # decrypt file stream
                pyAesCrypt.decryptStream(fIn, fOut, password, bufferSize, encFileSize)
        except ValueError as e:
            # remove output file on error
            remove(file+'.json')
            raise e


def existsFile(file):
    return os.path.isfile(file)

def deleteFile(file):
    remove(file)

def encodeFileBase64(file):
    data = open(file, "r").read().encode("utf-8")
    return base64.b64encode(data)
