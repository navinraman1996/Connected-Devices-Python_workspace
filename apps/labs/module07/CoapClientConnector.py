'''
Created on Mar 19, 2019

@author: Navin Raman
'''

from coapthon.messages              import request
from coapthon.client.helperclient   import HelperClient

'''
This is the helper class that connects to the CoAP server
    
@param host: IP address of the server
@param port: Port number to connect
@param path: Resource URI
'''
class CoapClientConnector():
    
    def __init__(self, host, port, path):
        self.host = host
        self.port = port
        self.path = path
        self.client = HelperClient(server=(host, port))
        
    '''
    Wrapper method is used to ping the server
    '''    
    def ping(self):
                
        self.client.send_empty("")
    
    '''
    Wrapper method is used for the GET action
    '''    
    def get(self):
        
        response = self.client.get(self.path)
        print(response.pretty_print())
    
    '''
    Wrapper method is used for the POST action
        
    @param jsonData: Request payload in JSON format
    '''
    def post(self,jsonData):
        
        response  = self.client.post(self.path, jsonData)
        print(response.pretty_print())
    
    '''
    Wrapper method is used for the PUT action
        
    @param jsonData: Request payload in JSON format
    '''
    def put(self, jsonData):
        
        response = self.client.put(self.path, jsonData)
        print(response.pretty_print())
        
    '''
    Wrapper method is used for the DELETE action
    '''    
    def delete(self):
        
        response = self.client.delete(self.path)
        print(response.pretty_print())
        
    '''
    This method is used to stop the client thread
    '''    
    def stop(self):
        
        self.client.stop()     