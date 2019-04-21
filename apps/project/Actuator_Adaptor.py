'''
Created on Mar 26, 2019

@author: Navin Raman
'''

from project import ActuatorData
from project import SenseHatLedActivator
from project import SmtpClientConnector

'''
This class is used to process the actuator message and assign message
to the SenseHat
'''
class Actuator_Adaptor(object):

    ActuatorData            = None #instance of Actuatordata class 
    SenseHatLedActivator    = None #instance of SenseHatLedActivator class
    
    '''
    Constructor
    '''
    def __init__(self):
        
        self.ActuatorData           = ActuatorData.ActuatorData()
        self.connector              = SmtpClientConnector.SmtpClientConnector()
        self.SenseHatLedActivator   = SenseHatLedActivator.SenseHatLedActivator()
        
        #Enabling the Thread
        self.SenseHatLedActivator.setEnableLedFlag(True) #Enabling the Thread  
        self.SenseHatLedActivator.start() #Starting the SenseHatLedActivator Thread

    '''
    This function is used to process the ActuatorData and change the message
    to the SenseHat
    @param pActuatorData: ActuatorData which has to be processed
    '''
    def processMessage(self, key, pActuatorData):
        
        if (key != None):
            if(self.ActuatorData != pActuatorData):
                
                if (key == "temperatureactuator"):
                    self.SenseHatLedActivator.setDisplayMessage('THERMOSTAT temperature has been changed to ' + str(pActuatorData.temperatureactuator) + chr(176)+' ˚C');
                    self.connector.publishMessage('WARNING!!! Temperature has been breached the limit' , 'setting the temperature to' + str(abs(pActuatorData.temperatureactuator)) + ' ˚C');
                    
                elif(key == "gasactuator"):
                    self.SenseHatLedActivator.setDisplayMessage('GAS HAS BEEN LEAKED !!!EXHAUST TURNED ON!! level: ' + str(pActuatorData.gasactuator) + ' Pa ');
                    self.connector.publishMessage('WARNING!!! GAS has been leaked' , 'Turning on the Exhaust fan' + ' Pa ');
                    
                elif(key == "humidityactuator"):
                    self.SenseHatLedActivator.setDisplayMessage('HUMIDIFIER has been changed to ' + str(pActuatorData.humidityactuator) + ' RH ');
                    self.connector.publishMessage('WARNING!!! Humidity breached the limit', 'setting the humidity in humidifier to ' + str(abs(pActuatorData.humidityactuator)) + ' RH ');
    
        self.ActuatorData.updateData(pActuatorData)