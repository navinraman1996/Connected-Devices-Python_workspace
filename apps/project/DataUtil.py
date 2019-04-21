'''
Created on Mar 13, 2019

@author: Navin Raman
'''

import json
from project import SensorData
from project import ActuatorData

'''
This class is used to convert Sensor Data to json and vice versa
'''
class DataUtil(object):
    
    sensorData      = None
    ActuatorData    = None
    sJSONobj        = None
    aJSONobj        = None
    dict            = None
    key             = None
    Sdata           = '{"timeStamp":"0", "temperature":"0", "pressure":"0", "humidity":"0"}'
    Adata           = '{"timeStamp":"0", "temperatureactuator":"0", "humidityactuator":"0", "pressureactuator":"0"}'
    
    '''
    Constructor
    '''
    def __init__(self):
        
        self.sensorData     = SensorData.SensorData()
        self.sJSONobj       = json.dumps(self.Sdata)
        self.ActuatorData   = ActuatorData.ActuatorData()
        self.aJSONobj       = json.dumps(self.Adata)
      
    '''
    This Function is used to convert Sensor Data to JSON
    @param sensordata: Sensor Data object
    @return sJSONobj: sJSONobj JSON string on success, null on failure
    '''    
    def toJsonFromSensorData(self, sensorData):
        
        self.dict = {}
        self.dict['temperature']    = sensorData.temperature
        self.dict['gas']            = sensorData.gas
        self.dict['humidity']       = sensorData.humidity
        self.sJSONobj               = json.dumps(self.dict)
        
        if (self.sJSONobj != None):
            sOutfile = open('SensorDatatoJSON.txt', 'w')
            sOutfile.write(self.sJSONobj)
            return self.sJSONobj
    
        return None
    
    '''
    This function is used to convert the JSON data to Sensor data
    @param JSON: JSON string
    @return sensorData: Sensor Data object on success, null on failure
    '''
    def toSensorDataFromJson(self, JSON):
        self.dict = json.loads(JSON)
        
        if (self.dict != None):
            self.sensorData.temperature = self.dict['temperature']
            self.sensorData.gas         = self.dict['gas']
            self.sensorData.humidity    = self.dict['humidity']
            return self.sensorData
        
        return None
        
    '''
    This function is used to convert Actuator Data to JSON
    @param ActuatorData: Actuator Data object
    @return aJSONobj: aJSONobj JSON string on success, null on failure
    '''    
    def toJsonFromActuatorData(self, ActuatorData):
        
        self.aJSONobj = json.dumps(ActuatorData.__dict__)
        
        if (self.aJSONobj != None):
            aOutfile = open('ActuatorDatatoJSON.txt', 'w')
            aOutfile.write(self.aJSONobj)
            return self.aJSONobj
    
        return None
    
    '''
    This function is used to convert JSON to Sensor data
    @param JSON: JSON string
    @return actuatorData: Sensor Data object on success, null on failure
    '''
    def toActuatorDataFromJson(self, JSON):
        
        self.dict = json.loads(JSON)
        
        if (self.dict != None):
            self.ActuatorData.timeStamp         = self.dict["timeStamp"]
            self.ActuatorData.gasactuator       = self.dict["gasactuator"]
            self.ActuatorData.humidityactuator  = self.dict["humidityactuator"]
            self.ActuatorData.temperatureactuator = self.dict["temperatureactuator"]
            return self.ActuatorData
        
        return None
     
    '''
    This function is used to update the ActuatorData
    @param JSON: JSON string
    @param topic: endpoint value
    '''    
    def updateActuatorData(self, topic, JSON):
        print('Inside updateActuatorData ' + topic +'JSON :' + JSON) 
        self.dict   = json.loads(JSON)
        self.key    = self.parseTopic(topic)
        print('key is ' + self.key)
        
        if (self.key != None):
            if (self.key == "temperatureactuator"):
                self.ActuatorData.temperatureactuator = self.dict["value"]
                
            elif(self.key == "gasactuator"):
                self.ActuatorData.gasactuator = self.dict["value"]
                
            elif(self.key == "humidityactuator"):
                self.ActuatorData.humidityactuator = self.dict["value"]
                
        print(self.ActuatorData)
    '''
    This Function is used to parse the topic from the endpoint
    @param topic: endpoint value
    '''
    def parseTopic(self, topic):
        return topic.rsplit('/', 1)[-1]