'''
Created on Jan 26, 2019

@author: Navin Raman
'''

import os
from datetime import datetime

'''
This class is used to define the ActuatorData object.
'''
class ActuatorData(object):

    gasactuator         = 0
    humidityactuator    = 0
    temperatureactuator = 0
    
    '''
    Constructor
    '''
    def __init__(self):
        self.updateTimeStamp()

    '''
    This function is used to update the ActuatorData
    @param data: data from ActuatorData 
    '''
    def updateData(self, data):
        
        self.gasactuator            = data.gasactuator
        self.humidityactuator       = data.humidityactuator
        self.temperatureactuator    = data.temperatureactuator

    '''
    This function is used to update the date and time 
    '''
    def updateTimeStamp(self):
        self.timeStamp = str(datetime.now())

    '''
    This function will return the string representation of the ActuatorData object.
    @return: 'customStr' - data from ActuatorData object in string format.
    '''
    def __str__(self):
        
        customStr = \
        os.linesep + '\ttimeStamp: '            + self.timeStamp + \
        os.linesep + '\tgasactuator: '          + str(self.gasactuator) + \
        os.linesep + '\thumidityactuator: '     + str(self.humidityactuator) + \
        os.linesep + '\ttemperatureactuator '   + str(self.temperatureactuator)
        
        return customStr