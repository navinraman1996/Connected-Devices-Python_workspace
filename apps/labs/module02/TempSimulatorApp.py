'''
Created on Jan 24, 2019

@author: Navin Raman
'''

from time           import sleep
from labs.module02  import TempSensorEmulator

'''
New thread to measure data processing values and start the thread to run
creating a new temperature measurement object 
'''
sensor_dat = TempSensorEmulator.TempSensorEmulator("NEW TEMPERATURE DATA")
sensor_dat.daemon = True
sensor_dat.start()

'''
#setting the running time 10 seconds but since it is in while loop,
this will automatically regain the next 10 seconds and run until the loop is false
'''
while True:
    sleep(10)
    pass