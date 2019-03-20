'''
Created on Mar 19, 2019

@author: Navin Raman
'''

from labs.module07.CoapServerConnector import CoapServerConnector

from labs.common import ConfigConst
from labs.common.ConfigUtil import ConfigUtil

config = ConfigUtil('../data/ConnectedDevicesConfig.props')
config.loadConfig()

host = config.getProperty(ConfigConst.ConfigConst.COAP_DEVICE_SECTION, ConfigConst.ConfigConst.HOST_KEY)
port = int(config.getProperty(ConfigConst.ConfigConst.COAP_DEVICE_SECTION, ConfigConst.ConfigConst.PORT_KEY))

server = CoapServerConnector(host,port,config)

server.start()