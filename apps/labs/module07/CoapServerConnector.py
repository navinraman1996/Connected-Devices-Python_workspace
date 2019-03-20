'''
Created on Mar 19, 2019

@author: Navin Raman
'''

from coapthon.server.coap   import CoAP

from coapthon.resources.resource        import Resource
from labs.module07.TempResourceHandler  import TempResourceHandler

client = None

'''
classdocs
'''
class CoapServerConnector(CoAP):
    
    '''
    Constructor
    '''
    def __init__(self,host,port,config):
        
        CoAP.__init__(self, (host, port))
        self.add_resource("temperature/", TempResourceHandler(config = config)) #Add Temperature resource while initializing server
        
    '''
    This function is used to start the server
    '''
    def start(self):
        try:
            print("Starting Server...")
            self.listen(10)
        except KeyboardInterrupt:
            print("Server Shutdown")
            self.close()
            print("Exiting...")
        finally:
            self.close()