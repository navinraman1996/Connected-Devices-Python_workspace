'''
Created on Jan 19, 2019

@author: Navin Raman
'''

import os
from datetime import datetime

'''
This class is used to calculate and categorize required value from sensor data.
@var timeStamp: present date and time.
'''
class SensorData(object):
    
    gas         = 0
    humidity    = 0
    temperature = 0
    
    '''
    SensorData constructor
    '''
    def __init__(self):
        
        self.timeStamp = str(datetime.now())
        self.totValue = [0, 0, 0]
        self.avgValue = [0, 0, 0]
        self.sampleCount = 0
        
    '''
    This function is used to calculate and categorize the
    required values from sensor readings.
    @param newVal: new sensor datas.
    '''
    def addValue(self, newVal):
        
        print('\n--------------------')
        print('Sensor data : ' + 'T:' + str(newVal[0]) +'  '+ 'G:' +str(newVal[1]) +'  '+ 'H:' +str(newVal[2]))
        
        self.sampleCount += 1
        self.timeStamp      = str(datetime.now())
        self.temperature    = newVal[0]
        self.gas            = newVal[1]
        self.humidity       = newVal[2]
        self.totValue[0]   += newVal[0]
        self.totValue[1]   += newVal[1]
        self.totValue[2]   += newVal[2]

        i = 0
        for x in self.totValue :
            if (x != 0 and self.sampleCount > 0):
                self.avgValue[i] = (x / self.sampleCount)
            i += 1

    '''
    This function returns the string representation of the SensorData object.
    @return: 'customStr' - SensorData object in string format.
    '''
    def __str__(self):
        
        customStr = \
        os.linesep + '\ttimeStamp: ' + self.timeStamp + \
        os.linesep + '\ttemperature: ' + str(self.temperature) + \
        os.linesep + '\tgas: ' + str(self.gas) + \
        os.linesep + '\thumidity: ' + str(self.humidity)
        
        return customStr