'''
Created on Apr 19, 2019

@author: Navin Raman
'''

import time
import requests
from project import ConfigUtil

'''
This class is used to publish the data to the broker using HTTPS
'''
class HTTPClientPublisher(object):
    
    url     = ''
    TOKEN   = ''
    
    '''
    Constructor
    '''
    def __init__(self):
        
        self.config     = ConfigUtil.ConfigUtil()
        self.baseURL    = self.config.getProperty(self.config.configConst.UBIDOTS_CLOUD_SECTION, self.config.configConst.CLOUD_BASE_URL)
        self.TOKEN      = self.config.getProperty(self.config.configConst.MQTT_CLOUD_SECTION, self.config.configConst.USER_NAME_TOKEN_KEY)

    '''
    This function is used to publish the payload to broker
    @param label: variable label
    @param payload: value of the datain JSON format
    '''
    def publish(self, label, payload):
        
        self.url    = self.baseURL + label # Creates the headers for the HTTP requests
        headers     = {"X-Auth-Token": self.TOKEN, "Content-Type": "application/json"}
    
        status      = 400 # Makes the HTTP requests
        attempts    = 0
        
        while status >= 400 and attempts <= 5:
            print("sending request")
            req = requests.post(url=self.url, headers=headers,data= payload )
            status = req.status_code
            print(req.status_code)
            attempts += 1
            time.sleep(1)
    
        # Processes the results
        if status >= 400:
            print("[ERROR] Could not send data after 5 attempts, please check \
                your token credentials and internet connection")
            return False
    
        print("[INFO] request made properly, your device is updated")
        return True