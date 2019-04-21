'''
Created on Feb 13, 2019
TempSensorAdaptor.py : Temperature sensor adaptor python class
@author: Navin Raman
'''

import threading
import random  # import to generate random values within a range 
from project    import SensorData
from project    import ActuatorData
from project    import Actuator_Adaptor
from sense_hat  import SenseHat
from time       import sleep
from project    import DataUtil
from project    import MqttPubClient
from project    import MqttSubClient
from project    import HTTPClientPublisher

UBIDOTS_DEVICE_LABEL                = "final_project"
UBIDOTS_VARIABLE_TEMPERATURE_LABEL  = "temperatureactuator"
UBIDOTS_VARIABLE_PRESSURE_LABEL     = "gasactuator"
UBIDOTS_VARIABLE_HUMIDITY_LABEL     = "humidityactuator"
UBIDOTS_VARIABLES = [UBIDOTS_VARIABLE_TEMPERATURE_LABEL, UBIDOTS_VARIABLE_PRESSURE_LABEL, UBIDOTS_VARIABLE_HUMIDITY_LABEL]

'''
TempSensorAdaptor - Class to get system's temperature sensor readings, send mail and take action.
'''
class Sensor_Adaptor(threading.Thread):
    
    __instance      = None
    sensorData      = None 
    ActuatorData    = None
    ActuatorEmulator = None
    SenseHat        = None
    sensorReading   = None
    curTemp         = 0 
    prevTemp        = 0
    curGas          = 0
    prevPressure    = 0
    curHumidity     = 0
    prevHumidity    = 0
    isPrevSensorReadingsSet = False
    timeInterval    = 0
    DataUtil        = None
     
    '''
    Static access function for singleton implementation.
    @return: '__instance' - singleton TempSensorEmulator class instance.
    '''
    @staticmethod
    def getInstance():
        if Sensor_Adaptor.__instance == None:
            Sensor_Adaptor()
            
        return Sensor_Adaptor.__instance

    '''
    TempSensorEmulator Constructor
    '''
    def __init__(self):
        
        if Sensor_Adaptor.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            self.beginEmulator  = False
            self.threadName     = "Sensor_Adaptor"
            self.sensorData     = SensorData.SensorData()
            self.sensorReading  = [0, 0, 0]
            self.curTemp        = 0
            self.prevTemp       = 0
            self.curGas         = 0
            self.prevPressure   = 0
            self.curHumidity    = 0
            self.prevHumidity   = 0
            self.tempDiff       = 0
            self.isPrevSensorReadingsSet = False
            self.timeInterval   = 30
            self.ActuatorData   = ActuatorData.ActuatorData()
            self.Actuator_Adaptor = Actuator_Adaptor.Actuator_Adaptor()
            self.SenseHat = SenseHat()
            self.DataUtil = DataUtil.DataUtil()
            self.MQTTsubscriber = MqttSubClient.MqttSubClient()
            self.HTTPpublisher  = HTTPClientPublisher.HTTPClientPublisher()
            threading.Thread.__init__(self)
            Sensor_Adaptor.__instance = self

    '''
    This function is used to set the sensor sensor adaptor for emulating.
    @param value: sensor value
    '''
    def setSensorAdaptor(self, value):
        self.beginEmulator = value 
    
    '''
    Thread function
    connecting to the MQTT broker
    '''    
    def run(self):
        self.MQTTsubscriber.connect()
        
        while True:
            if self.beginEmulator:
                #get temperature from SenseHat
                self.curTemp            = self.SenseHat.get_temperature()  
                self.sensorReading[0]   = self.curTemp
                #generating random value for virtual gas sensor
                self.curGas             = random.uniform(0, 100)  
                self.sensorReading[1]   = self.curGas
                #get humidity from SenseHats
                self.curHumidity        = self.SenseHat.get_humidity()  
                self.sensorReading[2]   = self.curHumidity
                self.sensorData.addValue(self.sensorReading)
                
                if self.isPrevSensorReadingsSet == False:
                    self.prevTemp       = self.curTemp
                    self.prevPressure   = self.curGas
                    self.prevHumidity   = self.curHumidity
                    self.isPrevSensorReadingsSet = True
                    
                else:
                    print("Sensor JSON DATA : " + self.DataUtil.toJsonFromSensorData(self.sensorData))
                    self.MQTTsubscriber.subscribe(UBIDOTS_VARIABLES)
                
                    if self.HTTPpublisher.publish(UBIDOTS_DEVICE_LABEL, self.DataUtil.toJsonFromSensorData(self.sensorData)) == False:
                        return
                    
                    self.Actuator_Adaptor.processMessage(self.MQTTsubscriber.connector.dataUtil.key, self.MQTTsubscriber.connector.dataUtil.ActuatorData)     
            sleep(self.timeInterval) #for delay
        self.MQTTsubscriber.disconnect()