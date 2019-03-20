'''
Created on Mar 19, 2019

@author: Navin Raman
'''

from coapthon.server.coap   import CoAP

from coapthon.resources.resource        import Resource
from labs.module07.TempResourceHandler  import TempResourceHandler

client = None

'''
This class is used to connect to the server
'''
class CoapServerConnector(CoAP):
    
    '''
    Constructor
    '''
    def __init__(self,host,port,config):
        
        CoAP.__init__(self, (host, port))
        
        #Adding Temperature resource while initializing server
        self.add_resource("temperature/", TempResourceHandler(config = config)) 
        
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