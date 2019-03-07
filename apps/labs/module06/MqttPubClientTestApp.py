'''
Created on Mar 5, 2019

@author: Navin Raman
'''

import logging

from random     import uniform
from datetime   import datetime

from labs.common            import ConfigConst
from labs.common.ConfigUtil import ConfigUtil
from labs.common.DataUtil   import DataUtil
from labs.common.SensorData import SensorData
from labs.module06.MqttClientConnector  import MqttClientConnector

topic   = "Temperature Sensor"

config  = ConfigUtil('../../../config/ConnectedDevicesConfig.props');
host    = config.getProperty(ConfigConst.ConfigConst.MQTT_CLOUD_SECTION, ConfigConst.ConfigConst.HOST_KEY)

'''
Creating the Sensor Data
'''
sensor              = SensorData(topic,0,30)
sensor.curValue     = uniform(float(sensor.getMinValue()), float(sensor.getMaxValue())); 
sensor.addValue(sensor.curValue);
sensor.diffValue    = sensor.curValue - sensor.avgVal;
sensor.timestamp    = datetime.now();
logging.info('SensorData to be sent:')
print("Sensor data before converting to Json: " + str(sensor));

'''
Converting the Sensor Data to the JSON format
'''
data        = DataUtil()
jsonData    = data.SensorDataToJson(sensor)
logging.info('SensorData converted into Json:')
print("SensorData in Json Format before publishing" + "\n" + str(jsonData) + "\n")
pub_client  = MqttClientConnector();

'''
This Function is used to publish the JSON data to the MQTT broker through
the MQTT ClientConnector class

@param topic:    Topic of the message
@param jsonData: It is the JSON Payload
@param host:     It is the address of the MQTT broker 
'''
pub_client.publish(topic,jsonData,host)
        