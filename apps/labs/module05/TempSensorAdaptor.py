'''
Created on Jan 24, 2019

@author: Navin Raman
'''
import json 

from threading      import Thread
from random         import uniform 
from time           import sleep
from datetime       import datetime

from labs.common    import SensorData

from labs.common    import DataUtil
from labs.common    import ConfigUtil 
from labs.common    import ConfigConst

from labs.module02  import SmtpClientConnector
from labs.module03  import TempActuatorEmulator

'''
Creating a class called TempSensorAdaptor where this class implements thread
'''
class TempSensorAdaptor(Thread):

    '''
    This thread generates a random float variable(Current Value). 
    If the current value is greater than given threshold notification is generated.
    Creating a sensor data object.
    This Constructor is initialized in __init__; and setting enableEmulator flag to true.
    @param name: takes the name in the argument 
    '''
    def __init__(self, name):
        
        Thread.__init__(self)
        self.enableAdaptor = True
        self.sensor = SensorData.SensorData(name, 0, 30)
        self.temp = ConfigUtil.ConfigUtil('../../../config/ConnectedDevicesConfig.props') 
        self.tempEmulator = TempActuatorEmulator.TempActuatorEmulator()
        
    '''
    This function is used to write the generated Sensor data content as JSON
    to a file to the filesystem.
    
    @param value: value of the JSON content
    @param filename: name of the file  
    '''    
    def fileWrite(self, value, filename):
        with open(filename,'w'):
            json.dumps(value)
        
    '''
    This funtion is send the generated SensorData content as JSON to a file
    to the filesystem
    '''    
    def run(self):
        while True:
            
            '''
                Enabling the Emulator and generates the current value provided 
                within the range and printing the sensor data.
                '''
            if self.enableAdaptor:
                self.sensor.curVal = uniform(float(self.sensor.getMinValue()), float(self.sensor.getMaxValue())) 
                self.sensor.addValue(self.sensor.curVal)
                self.sensor.diffVal = self.sensor.curVal - self.sensor.avgVal
                print(self.sensor)
                
                '''
                Alert Notification will be sent if the current value exceeds
                the average value by 3 then the mail will be sent, and
                printing the JSON string in the console output
                '''    
                if self.sensor.curVal >= (self.sensor.getAvgValue() + 3):
                    data = DataUtil.DataUtil()
                    self.sensor.timestamp = datetime.now()
                    json_data = data.SensorDataToJson(self.sensor)
                    SensorData.SensorData.surpassed_values.append(self.sensor)
                    #print(SensorData.SensorData.surpassed_values)
                    print("Warning: Temperature has been surpassed")
                    print("\nJSON data: " + json_data +'\n')
                    
                    sensor_notification = SmtpClientConnector.SmtpClientConnector() 
                    sensor_notification.publishMessage("Temperature Alert Notification: ",json_data) 
                
                '''
                providing a delay for every sensor readings
                '''      
                delay = int(self.temp.getProperty(ConfigConst.ConfigConst.CONSTRAINED_DEVICE, ConfigConst.ConfigConst.POLL_CYCLES_KEY))      
                sleep(delay)