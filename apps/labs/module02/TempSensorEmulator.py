'''
Created on Jan 24, 2019

@author: Navin Raman
'''
from threading      import Thread
from random         import uniform
from time           import sleep

from labs.common    import ConfigUtil
from labs.common    import ConfigConst

from labs.common    import SensorData
from labs.module02  import SmtpClientConnector

class TempSensorEmulator(Thread):
    '''
    Creating a class called TempSensorEmulator where this class implements thread
    '''
    def __init__(self,name):
        '''
        This Constructor is initialized in __init__; and setting enableEmulator flag to true.
        Assigning the sensor minimum temperature value = 0 and maximum value = 30.
        '''
        Thread.__init__(self)
        self.enableEmulator = True
        self.sensor = SensorData.SensorData(name,0,30)
        self.temp_delay = ConfigUtil.ConfigUtil('../../../config/ConnectedDevicesConfig.props')
    
    def run(self):
        while True:
            
            '''
                Enabling the Emulator and generates the current value provided within the range
                and printing the sensor data.
                '''
            if self.enableEmulator:
                self.sensor.curVal = uniform(float(self.sensor.getMinValue()), float(self.sensor.getMaxValue()))
                self.sensor.addValue(self.sensor.curVal)
                print(self.sensor)
                
            '''
                Alert Notification will be sent if the current value exceeds the threshold value
                which is the addition of the average value and 10
                '''     
            if self.sensor.curVal >= (self.sensor.getAvgValue() + 10):
                data = (self.sensor)
                print(data)
                print("Warning: Temperature has been surpassed")
                
                
                sensor_notification = SmtpClientConnector.SmtpClientConnector()
                sensor_notification.publishMessage("Temperature Alert Notification", data)
            
            '''
            providing a delay for every sensor readings
            '''    
            delay = int(self.temp_delay.getProperty(ConfigConst.ConfigConst.CONSTRAINED_DEVICE, ConfigConst.ConfigConst.POLL_CYCLES_KEY))     
            sleep(delay)