'''
Created on Mar 19, 2019

@author: Navin Raman
'''

from coapthon.messages      import request
from labs.common.SensorData import SensorData
from labs.common.DataUtil   import DataUtil

from labs.common.ConfigUtil import ConfigUtil
from labs.common            import ConfigConst

from labs.module07.CoapClientConnector import CoapClientConnector

config = ConfigUtil('../../../config/ConnectedDevicesConfig.props')
config.loadConfig()

data = DataUtil()

host = config.getProperty(ConfigConst.ConfigConst.COAP_DEVICE_SECTION, ConfigConst.ConfigConst.HOST_KEY)
port = int(config.getProperty(ConfigConst.ConfigConst.COAP_DEVICE_SECTION, ConfigConst.ConfigConst.PORT_KEY))
path = 'temperature'

sensor = SensorData("Temperature",0.0,30.0)
sensor.addValue(4.0)
print(str(sensor))

coapClient = CoapClientConnector(host, port, path)

coapClient.ping()
json_data = data.SensorDataToJson(sensor)
print("json"+json_data)

#coapClient.get() #Get will respond with NOT_FOUND since data object on server is not initialized
coapClient.post((json_data)) #Post JSON to server
coapClient.get()

sensor.addValue(5.00)
coapClient.put(data.SensorDataToJson(sensor)) #Update resource on the server
coapClient.get()

coapClient.delete() #Delete resource
coapClient.get()

coapClient.stop()