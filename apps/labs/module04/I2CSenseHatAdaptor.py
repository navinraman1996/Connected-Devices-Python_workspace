'''
Created on Feb 5, 2019

@author: Navin Raman
'''

import smbus
import threading

from time import sleep

from labs.common import ConfigUtil
from labs.common import ConfigConst

i2cBus          = smbus.SMBus(1) # Use I2C bus No.1 on Raspberry Pi3 +

enableControl   = 0x2D
enableMeasure   = 0x08

accelAddr       = 0x1C # address for IMU (accelerometer)
magAddr         = 0x6A # address for IMU (magnetometer)
pressAddr       = 0x5C # address for pressure sensor
humidAddr       = 0x5F # address for humidity sensor

begAddr         = 0x28
totBytes        = 6

DEFAULT_RATE_IN_SEC = 5
    
'''
Creating a class called I2CSenseHatAdaptor where this class implements thread
'''    
class I2CSenseHatAdaptor(threading.Thread):
    rateInSec = DEFAULT_RATE_IN_SEC
    
    '''
    Getting configuration data from ConfigUtil and ConfigConst
    and initiating the initI2CBus function
    '''
    def __init__(self):
        super(I2CSenseHatAdaptor, self).__init__()
        
        self.config = ConfigUtil.ConfigUtil(ConfigConst.ConfigConst.DEFAULT_CONFIG_FILE_NAME)
        self.config.loadConfig()
        
        print('Configuration data...\n' + str(self.config))
        
        self.initI2CBus()
    
    '''
    Initializing I2C bus with respective to the sensor address and 
    enabling I2C addresses
    '''    
    def initI2CBus(self):
        print("Initializing I2C bus and enabling I2C addresses...")
        
        i2cBus.write_quick(accelAddr)
        i2cBus.write_quick(magAddr)
        i2cBus.write_quick(pressAddr)
        i2cBus.write_quick(humidAddr)
        
    '''
    This thread is used to call the display functions when the enableEmulator
    is set to true and the display function displays the sensor data for a 
    given period of time : rateInSec
    '''    
    def run(self):
        while True:
            if self.enableEmulator:
                
                self.displayAccelerometerData()
                self.displayMagnetometerData()
                self.displayPressureData()
                self.displayHumidityData()
                
            sleep(self.rateInSec)
            
    '''
    This function is used to display the Accelerometer data from the sensor.
    Reading data from the sensor will look like the following:
    data = i2cBus.read_i2c_block_data({sensor address}, {starting read address}
    , {number of bytes})
    '''
    def displayAccelerometerData(self):
        self.accl_data = i2cBus.read_i2c_block_data(0x1C, begAddr, 6)
        i2cBus.write_byte_data(0x1C, enableControl, enableMeasure)
        print("Accelerometer value:    "+ str(self.accl_data));
      
    '''
    This function is used to display the Magnetometer data from the sensor.
    '''    
    def displayMagnetometerData(self):
        self.mag_data = i2cBus.read_i2c_block_data(0x6A, begAddr, 6)
        i2cBus.write_byte_data(0x6A, enableControl, enableMeasure)
        print("Magnetometer value:     "+ str(self.mag_data));
    
    '''
    This function is used to display the Pressure data from the sensor.
    '''    
    def displayPressureData(self):
        self.pres_data = i2cBus.read_i2c_block_data(0x5C, begAddr, 6)
        i2cBus.write_byte_data(0x5C, enableControl, enableMeasure)
        print("Pressure value: "+ str(self.pres_data));
    
    '''
    This function is used to display the Humidity data from the sensor.
    '''
    def displayHumidityData(self):
        self.humid_data = i2cBus.read_i2c_block_data(0x5F, begAddr, 6)
        i2cBus.write_byte_data(0x5F, enableControl, enableMeasure)
        print("Humidity value: "+ str(self.humid_data));