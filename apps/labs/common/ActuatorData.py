'''
Created on Feb 1, 2019

@author: Navin Raman
'''

import os

from datetime import datetime

COMMAND_OFF     = 0
COMMAND_ON      = 1
COMMAND_SET     = 2
COMMAND_RESET   = 3

STATUS_IDLE     = 0
STATUS_ACTIVE   = 1

ERROR_OK                =  0
ERROR_COMMAND_FAILED    =  1
ERROR_NON_RESPONSIBLE   = -1

'''
This class has the data's and attributes of actuator
'''
class ActuatorData():
    
    timeStamp   = None
    name        = 'Not set'
    hasError    = False
    command     = 0
    errCode     = 0
    statusCode  = 0
    stateData   = None
    val         = 0.0
    
    def __init__(self):
        self.updateTimeStamp()
    
    def getCommand(self): #returns the command value
        return self.command
    
    def getName(self): #returns the name
        return self.name
    
    def getStateData(self): #returns the state data
        return self.stateData
    
    def getStatusCode(self): #returns the state code
        return self.statusCode
    
    def getErrorCode(self): #returns the error code
        return self.errCode

    def getValue(self): #returns the data value
        return self.val;
    
    def hasError(self): #returns the error
        return self.hasError
    
    '''
    @param command: command value of the process 
    '''
    def setCommand(self, command):
        self.command = command
    
    '''
    @param command: name of the process 
    '''
    def setName(self, name):
        self.name = name
    
    '''
    @param stateData: state data of the process  
    '''
    def setStateData(self, stateData):
        self.stateData = stateData
    
    '''
    @param stateData: status code of the process  
    '''
    def setStatusCode(self, statusCode):
        self.statusCode = statusCode
    
    '''
    @param stateData: error code of the process  
    '''
    def setErrorCode(self, errCode):
        self.errCode = errCode
    
        if (self.errCode != 0):
            self.hasError = True
        else:
            self.hasError = False
    
    def setValue(self, val):
        self.val = val
    
    '''
    @param data: contains the actuator data's
    '''
    def updateData(self, data):
        self.command    = data.getCommand()
        self.statusCode = data.getStatusCode()
        self.errCode    = data.getErrorCode()
        self.stateData  = data.getStateData()
        self.val        = data.getValue()
    
    def updateTimeStamp(self):
        self.timeStamp = str(datetime.now())
    
    def __str__(self):
        customStr = \
            str(self.name + ':' + \
            os.linesep + '\tTime: '         + self.timeStamp + \
            os.linesep + '\tCommand: '      + str(self.command) + \
            os.linesep + '\tStatus Code: '  + str(self.statusCode) + \
            os.linesep + '\tError Code: '   + str(self.errCode) + \
            os.linesep + '\tState Data: '   + str(self.stateData) + \
            os.linesep + '\tValue: '        + str(self.val))
            
        return customStr