'''
Created on Mar 22, 2019

@author: Navin Raman
'''
import logging 
import paho.mqtt.client as mqttClient  # MQTT client
import ssl 
from project    import ConfigUtil
from project    import SensorData
from time       import sleep
from datetime   import datetime
from project    import DataUtil

'''
MQTTClientConnector: python class for implementing MQTT protocol connector
'''
class MQTTClientConnector(object):

    port                = None
    brockerKeepAlive    = None #to stay active in integer
    mqttClient          = None
    config              = None
    dataUtil            = None
    brokerAddr          = ""   #complete address of the host server in String
    
    '''
    Constructor
    '''
    def __init__(self):
        
        self.createLogger()  # log the console output 
        self.mqttClient     = mqttClient.Client()
        self.config         = ConfigUtil.ConfigUtil()
        self.config.loadConfig()
        self.brokerAddr     = self.config.getProperty(self.config.configConst.MQTT_CLOUD_SECTION, self.config.configConst.CLOUD_MQTT_BROKER)
        self.port           = int(self.config.getProperty(self.config.configConst.MQTT_CLOUD_SECTION, self.config.configConst.SECURE_PORT_KEY))
        self.brockerKeepAlive = int(self.config.getProperty(self.config.configConst.MQTT_CLOUD_SECTION, self.config.configConst.KEEP_ALIVE_KEY))
        self.dataUtil       = DataUtil.DataUtil()
        self.sensoData      = SensorData.SensorData()
        self.username       = self.config.getProperty(self.config.configConst.MQTT_CLOUD_SECTION, self.config.configConst.USER_NAME_TOKEN_KEY)
        self.password       = ""
        self.TLS_CERT_PATH  = r"ubidots_cert.pem"
         
    '''
    This function is used to create the logger and console handler
    '''            
    def createLogger(self):
        
        # creating logger
        self.logger = logging.getLogger('MQTTClientConnector')
        self.logger.setLevel(logging.DEBUG)
        
        # creating console handler and setting the level to debug
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        
        # creating the formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        
        # add formatter to ch
        ch.setFormatter(formatter)
        
        # add ch to logger
        self.logger.addHandler(ch)
    
    '''
    This function is used to connect to the MQTT host server
    @param connectionCallback: call back function for connection
    @param msgCallback: message call back function
    '''
    def connect(self, connectionCallback=None , msgCallback=None):
        
        if(connectionCallback != None):
            self.mqttClient.on_connect = connectionCallback
        else:
            self.mqttClient.on_connect = self.onConnect
            
        if(msgCallback != None) :
            self.mqclient.on_disconnect = msgCallback
        else :
            self.mqttClient.on_disconnect = self.onMessage
            
        self.mqttClient.on_message = self.onMessage    
        
        self.mqttClient.loop_start()
        self.mqttClient.username_pw_set(self.username, password=self.password)
        self.logger.info("Connecting to broker " + self.brokerAddr)
        self.mqttClient.tls_set(ca_certs=self.TLS_CERT_PATH, certfile=None,
                            keyfile=None, cert_reqs=ssl.CERT_REQUIRED,
                            tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)
        self.mqttClient.tls_insecure_set(False)
        self.mqttClient.connect(self.brokerAddr, self.port, self.brockerKeepAlive)
        
    '''
    This function is used to disconnect from the MQTT host server
    '''    
    def disconnect(self):
        self.mqttClient.loop_stop()
        self.logger.info("Disconneting the MQTT  broker connection ")
        self.mqttClient.disconnect()
        
    '''
    This Function is called when the broker responds to our connection request.
    @param flags: flags is a dict that contains response flags from the broker
    @param rc: The value of rc determines success or not
    @param client: Mqtt client
    @param userData: Mqtt data
    '''    
    def onConnect(self , client , userData , flags , rc):
        print("On connect RC : " + rc)
        
        if rc == 0:
            self.logger.info("Connected OK returned Code: " + rc)
        else:
            self.logger.debug("Bad connection Returned Code: " + rc)
        
    '''
    This function is called when a message has been received on a topic that the client subscribes to.
    @param msg: MqttMessage that describes all of the message parameters.
    @param client: Mqtt client
    @param userData: Mqtt data
    @param msg: The actual msg to send
    '''        
    def onMessage(self , client , userdata , msg):
        
        rcvdJSON = msg.payload.decode("utf-8")
        self.logger.info("\nReceived Topic is " + msg.topic + " --> \n" + str(rcvdJSON))
        self.dataUtil.updateActuatorData(msg.topic,rcvdJSON)
        
    '''
    This function is used to publish a message on a topic causing
    a message to be sent to the broker and subsequently from
    the broker to any clients subscribing to matching topics.
    @param topic: The topic that the message should be published on.
    @param msg: The actual message to send.
    @param msg: The actual message to send.
    '''    
    def publishMessage(self , topic , msg , qos=2):
   
        if qos < 0 or qos > 2 :
            qos = 2
            
        self.logger.info("\nTopic : "+ str(topic) + "\nMessage :\n" + str(msg))
        self.mqttClient.publish(topic, msg, qos)
        
    '''
    This function is used to establishthe MQTT connection, publish and disconnect
    @param topic: topic of the MQTT message in string
    @param msg: message payload
    @param qos: The quality of service level to use
    '''    
    def publishAndDisconnect(self , topic , msg, qos=2):
        
        self.logger.info("\nTopic :\n" + str(topic))
        self.connect()
        self.publishMessage(topic, msg, qos)
        self.disconnect()
       
    '''
    This function is used to subscribe the client to one or more topics
    @param topic: topic of the MQTT message in string
    @param connnectionCallback: call back function on subscribe/on message
    @param qos: The quality of service level to use
    '''    
    def subscibetoTopic(self , topic , connnectionCallback=None , qos=2):
        
        self.logger.info('subscibetoTopic : ' + topic)
        if (connnectionCallback != None):
            self.mqttClient.on_subscribe(connnectionCallback)
            self.mqttClient.on_message(connnectionCallback)
        
        self.mqttClient.subscribe(topic , qos)

    '''
    This function is used to unsubscribe the client from one or more topics.
    @param topic: A single string, or list of strings that are the
    subscription topics to unsubscribe from.
    @param connnectionCallback: call back function on unsubscribe event
    '''
    def unsubscibefromTopic(self , topic , connnectionCallback=None):
        
        if (connnectionCallback != None):
            self.mqttClient.on_unsubscribe(connnectionCallback)
               
        self.mqttClient.unsubscribe(topic)
     
    '''
    This function is used to establish MQTT connection,
    subscribe the client to one or more topics and disconnect
    @param topic: topic of the MQTT message in string
    @param connnectionCallback: call back function on unsubscribe event
    @param qos: The quality of service level to use
    '''    
    def subscribeAndDisconnect(self , topic , connnectionCallback=None , qos=2):
        
        self.logger.info("\nTopic :\n" + str(topic))
        self.connect()
        self.subscibetoTopic(topic, connnectionCallback , qos)
        self.disconnect()