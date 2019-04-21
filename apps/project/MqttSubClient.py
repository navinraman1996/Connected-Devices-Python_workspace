'''
Created on Feb 22, 2019

@author: Navin Raman
'''
from project import MQTTClientConnector

UBIDOTS_DEVICE_LABEL    = "ubidots/"
UBIDOTS_TOPIC_DEFAULT   = "/v1.6/devices/"

QOS = 2

'''
This class is used to receive message using MQTT protocol
'''
class MqttSubClient(object):
    connector = None
    
    '''
    MQTT publisher constructor, initializes the MQTT client connector.
    '''
    def __init__(self):
        # MQTT connector instance
        self.connector = MQTTClientConnector.MQTTClientConnector()  

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
    @param topic: data
    '''     
    def subscribe(self,topic):
        self.connector.subscibetoTopic(UBIDOTS_TOPIC_DEFAULT + UBIDOTS_DEVICE_LABEL + topic[0], None , QOS)
        self.connector.subscibetoTopic(UBIDOTS_TOPIC_DEFAULT + UBIDOTS_DEVICE_LABEL + topic[1], None , QOS)
        self.connector.subscibetoTopic(UBIDOTS_TOPIC_DEFAULT + UBIDOTS_DEVICE_LABEL + topic[2], None , QOS)