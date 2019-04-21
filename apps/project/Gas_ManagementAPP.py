'''
Created on April 18, 2019

@author: Navin Raman

This Script runs the main function of the whole project,
Starting the thread
'''
from project import Sensor_Adaptor

Project_Emulator = None  # Sensor_Adaptor instance variable

# getting singleton instance of Sensor_Adaptor
Project_Emulator = Sensor_Adaptor.Sensor_Adaptor.getInstance()
Project_Emulator.daemon = True  # initializing the daemon thread

# Passing True, to start the Sensor_Adaptor
Project_Emulator.setSensorAdaptor(True)  
Project_Emulator.start()  # starting the Sensor_Adaptor thread

# running into a infinite loop
while(True):
    pass