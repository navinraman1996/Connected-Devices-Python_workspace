'''
Created on Jan 26, 2019

@author: Navin Raman
'''

from time       import sleep
from sense_hat  import SenseHat
import threading

'''
This class is for LED to show message on the sense hat display
'''
class SenseHatLedActivator(threading.Thread):

    enableLed   = False
    rateInSec   = 1
    rotateDeg   = 270
    sh          = None
    displayMsg  = None
     
    '''
    constructor
    @param rotateDeg: angle of rotation in degree for lED display
    @param rateInSec: time in seconds
    ''' 
    def __init__(self, rotateDeg = 180, rateInSec = 1):
        
        super(SenseHatLedActivator, self).__init__()
        
        if rateInSec > 0:
            self.rateInSec = rateInSec
        if rotateDeg >= 0:
            self.rotateDeg = rotateDeg
            
        self.sh = SenseHat()
        self.sh.set_rotation(self.rotateDeg)
         
    '''
    Function for SenseHatLedActivator thread
    '''     
    def run(self):
        
        while True:
            if self.enableLed:
                
                if self.displayMsg != None:
                    #show scrolling LED message
                    self.sh.show_message(str(self.displayMsg))  
                else:
                    #self.sh.show_letter(str('R'))
                    self.sh.show_letter('')
    
                sleep(self.rateInSec)
                self.sh.clear()

            sleep(self.rateInSec)
     
    
    '''
    This function is used to get display rate
    @return: 'rateInSec' - time in seconds
    ''' 
    def getRateInSeconds(self):
        return self.rateInSec
 
    '''
    This function is used to enable LED display
    @param enable: True, to set the LED flag else False 
    '''
    def setEnableLedFlag(self, enable):
        self.sh.clear()
        self.enableLed = enable
     
    '''
    This function is used to set the message to be displayed in LED
    @param msg: String message to be displayed
    '''
    def setDisplayMessage(self, msg):
        self.displayMsg = msg