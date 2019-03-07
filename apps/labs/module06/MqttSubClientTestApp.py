'''
Created on Mar 5, 2019

@author: Navin Raman
'''
import logging

from labs.common            import ConfigConst
from labs.common.DataUtil   import DataUtil
from labs.common.ConfigUtil import ConfigUtil
from labs.module06.MqttClientConnector import MqttClientConnector

'''
Setting the values for Topic and address for the MQTT broker
'''
topic = "Temperature Sensor"
config = ConfigUtil('../../../config/ConnectedDevicesConfig.props');
host = config.getProperty(ConfigConst.ConfigConst.MQTT_CLOUD_SECTION, ConfigConst.ConfigConst.HOST_KEY)

'''
Connecting to the MQTT Broker and Subscribing to a specified topic
'''
subscribe = MqttClientConnector(topic)
subscribe.subscribe(host)
msg = subscribe.message()
logging.debug('JSON Data Received: ')
print("Json Data Received: " + "\n" + str(msg) + "\n")

'''
Converting the JSON data into Sensor Data
'''
data = DataUtil();
sensor = data.jsonToSensorData(msg)
logging.debug('Json data converted into SensorData')
print("Received SensorData format message "+str(sensor))       

'''
Converting the Sensor data to JSON data again
'''
json = data.SensorDataToJson(sensor)
logging.debug('SensorData converted into Json Data: ')
print('Again the Sensor Data is converted into Json Data : \n'+str(json))