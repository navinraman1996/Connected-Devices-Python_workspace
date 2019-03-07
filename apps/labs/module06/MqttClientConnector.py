'''
Created on Mar 5, 2019

@author: Navin Raman
'''
import time
import paho.mqtt.client as mqtt

'''
MqttClientConnector class is used to connect to a MQTT broker for publishing 
and subscription service
'''
class MqttClientConnector():
    host = "test.mosquitto.org"
    jsonData = "Hello"

    '''
    on_connect is a callback function which is called once the client connects
    with the MQTT broker.
    
    @param client: It is the reference to the client connection instance
    @param userData: User specified data associated with the connection
    @param flags: It is used to establish the connection with the broker
    @param rc: result code, which is an integer
    '''
    def on_connect(self, client, userdata, flags, rc):
        print("Connected with the Client: " + str(rc) + "\n")
        client.subscribe(self.topic)
        
    '''
    on_message is a callback function which is called when the client receives
    a message for a topic that ut has subscribed to.
    
    @param client: It is the reference to the client connection instance
    @param userData: User specified data associated with the connection
    @param msg: Message container for the published data, payload is used to
    store the actual message content.    
    '''
    def on_message(self, client, userdata, msg):
        global jsonData
        jsonData = str(msg.payload.decode("utf-8"))
        client.loop_stop()
        
    '''
    Constructor
    
    @param topic: It is the topic of the message publised or subscribed 
    '''
    def __init__(self, topic=None):
        self.topic = topic
        
    '''
    This function is used to publish the message
    
    @param topic: It is the topic of the message
    @param message: It is the message to be sent
    @param host: It is the Address of the MQTT broker 
    '''
    def publish(self,topic,message,host):
        client = mqtt.Client()
        client.connect(host,1883)
        client.publish(topic, message)
        
    '''
    This function is used to subscribe to a topic
    
    @param host: It is the Address of the MQTT broker
    '''
    def subscribe(self, host):
        client = mqtt.Client()
        client.on_connect = self.on_connect
        client.on_message = self.on_message
        client.connect(host,1883,60)
        client.loop_start()
        time.sleep(10)
        
    '''
    This function is used to store the data received from the MQTT broker
    
    @return: Returns the data which is received from the MQTT broker
    '''
    def message(self):
        global jsonData
        return jsonData 