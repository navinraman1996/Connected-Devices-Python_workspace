'''
Created on Feb 22, 2019

@author: Navin Raman
'''
from project import MQTTClientConnector

UBIDOTS_VARIABLE_LABEL  = "/TempSensor"
UBIDOTS_TOPIC_DEFAULT   = "/v1.6/devices/"

QOS = 2

'''
This class is used to publish message using MQTT protocol
'''
class MqttPubClient(object):
    
    connector = None
    '''
    Constructor
    '''
    def __init__(self):
        
        #MQTT publisher constructor, initializes the MQTT client connector.
        self.connector = MQTTClientConnector.MQTTClientConnector()  # MQTT connector instance

    '''
    This function is used to connect to the MQTT broker
    '''
    def connect(self):
        self.connector.connect()
        
    '''
    This function is used to disconnect from the MQTTT broker
    '''    
    def disconnect(self):
        self.connector.disconnect()
        
    '''
    This function is used to publish
    @param label: Device topic
    @param sJSONobj: json object
    ''' 
    def publish(self,label,sJSONobj):
        self.connector.publishMessage(UBIDOTS_TOPIC_DEFAULT + label, sJSONobj, QOS)