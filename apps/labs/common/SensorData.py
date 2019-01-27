'''
Created on Jan 24, 2019

@author: Navin Raman
'''

from datetime import datetime
import os

class SensorData(object):
    '''
    classdocs
    '''
    timestamp = None
    name = 'not set'
    curVal = 0;
    avgVal = 0;
    minVal = 0;
    maxVal = 30;
    totVal = 0;
    sampleCount = 0;
    
    '''
    Constructor used to create an object of SensorData class
    
    @param name: Name of the sensor
    @param minVal: Minimum temperature value of the sensor
    @param maxVal: Maximum temperature value of the sensor     
    '''
    def __init__(self, name,minVal,maxVal):
        self.timestamp = str(datetime.now())
        self.name = name
        self.maxVal = maxVal
        self.minVal = minVal
    
    '''
    This addValue function is used to calculate the average temperature value
    by adding the current value with the previous current value and dividing
    
    @param newVal: This is the new sensor value for the recent reading 
    '''
    def addValue(self,newVal):
        self.sampleCount += 1
        self.timeStamp = str(datetime.now())
        self.curVal = newVal
        self.totVal += newVal
        
        if (self.curVal < self.minVal):
            self.minVal = self.curVal
            
        if (self.curVal > self.maxVal):
            self.maxVal = self.curVal
            
        if (self.totVal != 0 and self.sampleCount > 0):
            self.avgVal = self.totVal / self.sampleCount
    
    #returns the average value of the reading
    def getAvgValue(self):
        return self.avgVal
    
    #returns the maximum value of the reading
    def getMaxValue(self):
        return self.maxVal
    
    #returns the minimum value of the reading
    def getMinValue(self):
        return self.minVal
    
    #returns the current value of the reading
    def getValue(self):
        return self.curVal
    
    def setName(self, name):
        self.name = name
    
    '''
    An object in human readable format which is returned by this toString function
    
    @return: Human readable format object to print in the console 
    '''
    def __str__(self):
        self.customStr = \
        str(self.name + ':' + \
        os.linesep + '\tTime: ' + self.timeStamp + \
        os.linesep + '\tSample number: ' + str(self.sampleCount) + \
        os.linesep + '\tCurrent Temperature value is: ' + str(self.curVal) + \
        os.linesep + '\tAverage Temperature: ' + str(self.avgVal) + \
        os.linesep + '\tMinimum Temperature: ' + str(self.minVal) + \
        os.linesep + '\tMaximum Temperature: ' + str(self.maxVal) + '\n')
        return self.customStr