'''
Created on Jan 24, 2019

@author: Navin Raman
'''
from threading      import Thread
from random         import uniform 
from time           import sleep
from datetime       import datetime

from labs.common    import SensorData
from labs.common    import ActuatorData

from labs.common    import ConfigUtil 
from labs.common    import ConfigConst

from labs.module02  import SmtpClientConnector
from labs.module03  import TempActuatorEmulator

class TempSensorAdaptor(Thread):
    '''
    Creating a class called TempSensorAdaptor where this class implements thread
    '''

    def __init__(self, name):
        '''
        This thread generates a random float variable(Current Value). 
        If the current value is greater than given threshold notification is generated.
        Creating a sensor data object.
        This Constructor is initialized in __init__; and setting enableEmulator flag to true.
        Assigning the sensor minimum temperature value = 0 and maximum value = 30.
        '''
        Thread.__init__(self)
        self.enableAdaptor = True
        self.sensor = SensorData.SensorData(name, 0, 30)
        self.temp = ConfigUtil.ConfigUtil('../../../config/ConnectedDevicesConfig.props') 
        self.tempEmulator = TempActuatorEmulator.TempActuatorEmulator()
        
    def run(self):
        while True:
            
            '''
                Enabling the Emulator and generates the current value provided within the range
                and printing the sensor data.
                '''
            if self.enableAdaptor:
                self.sensor.curVal = uniform(float(self.sensor.getMinValue()), float(self.sensor.getMaxValue())) 
                self.sensor.addValue(self.sensor.curVal)
                nominal_temp = self.temp.getProperty(ConfigConst.ConfigConst.CONSTRAINED_DEVICE, ConfigConst.ConfigConst.NOMINAL_TEMP)
                self.sensor.diffVal = self.sensor.curVal - self.sensor.avgVal
                print(self.sensor)
                
                '''
                Alert Notification will be sent if the current value exceeds or very lesser than the nomial temperature
                '''    
                if self.sensor.curVal >= (self.sensor.getAvgValue() + 3):
                    data = (self.sensor)
                    self.sensor.timestamp = datetime.now()
                    SensorData.SensorData.surpassed_values.append(self.sensor)
                    print(SensorData.SensorData.surpassed_values)
                    print("Warning: Temperature has been surpassed")
                    
                    sensor_notification = SmtpClientConnector.SmtpClientConnector() 
                    sensor_notification.publishMessage("Temperature Alert Notification: ", data) 
                
                '''
                Determining the difference between the nominal and the current temperature
                using actuator data
                '''
                if self.sensor.curVal!=nominal_temp:
                    self.actuator_data = ActuatorData.ActuatorData()
                    self.diff = (self.sensor.curVal - float(nominal_temp))
                    
                    if self.diff>0:
                        self.actuator_data.setValue(self.sensor.curVal - float(nominal_temp))
                        self.actuator_data.setCommand(ActuatorData.COMMAND_SET)
                    else:
                        self.actuator_data.setValue(float(nominal_temp) - self.sensor.curVal)
                        self.actuator_data.setCommand(ActuatorData.COMMAND_RESET)
                    
                    print("The difference between the nominal temp and the current temp is: " + str(self.actuator_data.getValue()) + chr(176) +'C')
                    self.tempEmulator.publishMessage(self.actuator_data)
                
                '''
                providing a delay for every sensor readings
                '''      
                delay = int(self.temp.getProperty(ConfigConst.ConfigConst.CONSTRAINED_DEVICE, ConfigConst.ConfigConst.POLL_CYCLES_KEY))      
                sleep(delay)