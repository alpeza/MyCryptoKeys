import json
class OMessage(object):
    """Mensaje que se envia"""
    def __init__(self, isOK=True,errc=0, message='', exception='', data={}):
        super(OMessage, self).__init__()
        self.isOK= isOK
        self.errc = errc
        self.message = message
        self.exception = exception
        self.data = data
    
    def getDictMessage(self):
        return {
            "errc" : self.errc,
            "message": self.message,
            "exception": self.exception,
            "data": self.data,
            "isOK": self.isOK
        }
    
    def getJSONMessage(self):
        return json.dumps(self.getDictMessage())

    def printm(self):
        print(self.getJSONMessage())