'''
Created on Jan 24, 2019

@author: Navin Raman
'''

from datetime import datetime
import os

class SensorData(object):
    '''
    this class contains sensor data's and attributes
    '''
    timestamp           = None
    name                = 'not set'
    curVal              = 0;
    avgVal              = 0;
    minVal              = 0;
    maxVal              = 25;
    totVal              = 0;
    diffVal             = 0;
    sampleCount         = 0;
    #to store the updated data in the local SensorData
    surpassed_values    = list();
    
    '''
    Constructor to create object of SensorData Class
   
    @param name: Sensor name
    @param minVal: Minimum allowed value of the sensor
    @param maxVal: Maximum allowed value of the sensor  
    '''
    def __init__(self, name, minVal, maxVal):
        '''
        Constructor
        '''
        self.timestamp  = str(datetime.now());
        self.name       = name;
        self.maxVal     = maxVal;
        self.minVal     = minVal;
        
    '''
    AddValue function is used to add value to previous total and calculate avg
   
    @param newVal: new Sensor value 
    '''
    def addValue(self, newVal):
        self.sampleCount += 1
        
        self.timeStamp  = str(datetime.now())
        self.curVal     = newVal
        self.totVal    += newVal
        
        if (self.curVal < self.minVal):
            self.minVal = self.curVal
        
        if (self.curVal > self.maxVal):
            self.maxVal = self.curVal
        
        if (self.totVal != 0 and self.sampleCount > 0):
            self.avgVal = self.totVal / self.sampleCount

    def getAvgValue(self): # returns the average value
        return self.avgVal
    
    def getMaxValue(self):# returns the maximum value
        return self.maxVal
    
    def getMinValue(self):# returns the minimum value
        return self.minVal
    
    def getValue(self):# returns the current value
        return self.curVal
    
    '''
    ToString function returns object in human readable format
   
    @return: Object in human readable customized format
    ''' 
    def __str__(self):
        self.customStr = \
            str(self.name + ':' + \
            os.linesep + '\tTime: '                         + self.timeStamp + \
            os.linesep + '\tSample number: '                + str(self.sampleCount) + \
            os.linesep + '\tCurrent Temperature value is: ' + str(self.curVal) + chr(176) +'C' + \
            os.linesep + '\tAverage Temperature: '          + str(self.avgVal) + chr(176) +'C' + \
            os.linesep + '\tMinimum Temperature: '          + str(self.minVal) + chr(176) +'C' + \
            os.linesep + '\tMaximum Temperature: '          + str(self.maxVal) + chr(176) +'C' + '\n')
            
        return self.customStr