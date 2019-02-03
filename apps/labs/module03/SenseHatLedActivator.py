'''
Created on Feb 1, 2019

@author: Navin Raman
'''
from time       import sleep
from sense_hat  import SenseHat
import threading

class SenseHatLedActivator(threading.Thread):
    enableLed   = False
    rateInSec   = 1
    rotateDeg   = 270
    sh          = None
    displayMsg  = None
    
    '''
    @param rotateDeg: is used for the text orientation and set to 270 degree
    @param rateInSec: is set to 1 second
    '''
    def __init__(self, rotateDeg = 270, rateInSec = 1):
        super(SenseHatLedActivator, self).__init__()
        
        if rateInSec > 0:
            self.rateInSec = rateInSec
        if rotateDeg >= 0:
            self.rotateDeg = rotateDeg
        
        self.sh = SenseHat()
        self.sh.set_rotation(self.rotateDeg)
    
    '''
    Run function is used to check whether their is any message is available
    which is to be displayed, if not then "no message" will be displayed at
    the console output
    '''
    def run(self):
        while True:
            if self.enableLed:
                if self.displayMsg != None:
                    self.sh.show_message(str(self.displayMsg))
                else:
                    print('No message')
                    self.sh.show_letter(str('No message'))
                
                sleep(self.rateInSec)
                self.sh.clear()
                
            sleep(self.rateInSec)
            
    def getRateInSeconds(self):
        return self.rateInSec
    
    def setEnableLedFlag(self, enable):
        self.sh.clear()
        self.enableLed = enable;
    
    '''
    setDisplayMessage Function is used to display the sensor values and
    processing data's in the console output
    
    @param message: Accepts a message value which is to be displayed 
    '''   
    def setDisplayMessage(self, message):
        self.displayMsg = message      