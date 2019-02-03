'''
Created on Feb 1, 2019

@author: Navin Raman
'''
from labs.common    import ActuatorData
from labs.module03  import SenseHatLedActivator

class TempActuatorEmulator():
    '''
    classdocs
    '''
        
    def __init__(self):
        '''
        Constructor which calls the ActuatorData class
        '''
        self.actuator_data = ActuatorData.ActuatorData();
        
    '''
    Publish message function is used send a message about the nominal temp changes,
    This function takes the data from the actuator data class and compare the 
    current value and the nominal value.
    
    @param actData: data from ActuatorData
    '''    
    def publishMessage(self,actData):
        if actData!=self.actuator_data:
            self.val = actData.getValue();
        
            if actData.getCommand()==2:
                message = "DECREASE the Temperature by %.2f" %(self.val) + chr(176) + "C" + " to reach the NOMINAL Temp";
            else:
                message = "INCREASE the Temperature by %.2f" %(self.val) + chr(176) + "C" + " to reach the NOMINAL Temp";
                  
            senseHat = SenseHatLedActivator.SenseHatLedActivator();
            senseHat.setDisplayMessage(message);
            print("-----------------------------------------------------------------------------------------------------")
            senseHat.setEnableLedFlag('enable');
        
            try:
                senseHat.start();
            except:
                print("Can't Activate The Actuator");
            finally:
                senseHat.enableLed = False
        self.actuator_data.updateData(actData);