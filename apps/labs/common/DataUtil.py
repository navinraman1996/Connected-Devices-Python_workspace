'''
Created on Feb 17, 2019

@author: Navin Raman
'''

import json
from labs.common.SensorData import SensorData
from labs.common.ActuatorData import ActuatorData


class DataUtil(object):
    '''
    This Class contains Functions which simply converts the data from one
    format to another which is, 
    jsonToSensorData,  SensorDataToJson,
    jsonToActuatorData, ActuatorDataToJson
    '''

    def __init__(self):
        '''
        Constructor
        '''
        
    '''
    This function will accept a JSON string as a parameter, then parse it and
    store the values in a new SensorData instance, returning the instance
    
    @param jsondata: data from the JSON string
    @return: returning the sensor data instance 
    '''
    def jsonToSensorData(self, jsonData):
        sdDict = json.loads(jsonData)

        #print(" decode [pre] --> " + str(sdDict))
        
        sd              = SensorData()
        sd.name         = sdDict['name']
        sd.timeStamp    = sdDict['timeStamp']
        sd.avgValue     = sdDict['avgValue']
        sd.minValue     = sdDict['minValue']
        sd.maxValue     = sdDict['maxValue']
        sd.curValue     = sdDict['curValue']
        sd.totValue     = sdDict['totValue']
        sd.sampleCount  = sdDict['sampleCount']
        
        #print(" decode [post] --> " + str(sd))
        
        return sd
    
    '''
    This function will accept a SensorData object as a parameter, convert and
    then return its contents as a JSON string
    
    @param SensorData: data from the sensor
    @return: returning the JSON instance 
    '''
    def SensorDataToJson(self, SensorData):
        data = {};
        
        data['name']        = SensorData.name
        data['avgValue']    = SensorData.avgVal
        data['maxValue']    = SensorData.getMaxValue()
        data['minValue']    = SensorData.getMinValue()
        data['curValue']    = SensorData.getValue()
        data['time']        = str(SensorData.timestamp)
        self.jsonSd         = json.dumps(data)
        outputSd            = open('sensordata.txt','w')
        
        outputSd.write(self.jsonSd)
    
        return self.jsonSd
        #return (print('JSON data:' + self.jsonSd))
    
    '''
    This function will accept a JSON string as a parameter, then parse it and
    store the values in a new ActuatorData instance, returning the instance
    
    @param jsondata: data from the JSON string
    @return: returning the Actuator data instance 
    '''
    def jsonToActuatorData(self, jsonData):
        adDict = json.loads(jsonData)
        
        #print(" decode [pre] --> " + str(adDict))
        
        ad              = ActuatorData()
        ad.name         = adDict['name']
        ad.timeStamp    = adDict['timeStamp']
        ad.hasError     = adDict['hasError']
        ad.command      = adDict['command']
        ad.errCode      = adDict['errCode']
        ad.statusCode   = adDict['statusCode']
        ad.stateData    = adDict['stateData']
        ad.curValue     = adDict['curValue']
        
        #print(" decode [post] --> " + str(ad))
        
        return ad
        
    '''
    This function will accept a ActuatorData object as a parameter, convert and
    then return its contents as a JSON string
    
    @param SensorData: data from the Actuator
    @return: returning the JSON instance 
    '''    
    def ActuatorDataToJson(self,actuatordata):
        
        self.jsonAd = json.dumps(actuatordata.__dict__)
        outputAd    = open('actuatordata.txt','w')
        
        outputAd.write(self.jsonAd)
        return self.jsonAd