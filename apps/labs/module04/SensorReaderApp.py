'''
Created on Feb 5, 2019

@author: Navin Raman
'''

from time           import sleep 
from labs.module04  import I2CSenseHatAdaptor

'''
Creating new thread to measure sensor data values and start the thread to run.
Daemon thread is used and start method is called to run  
'''
sensorData = I2CSenseHatAdaptor.I2CSenseHatAdaptor()
sensorData.daemon           = True
sensorData.enableEmulator   = True
sensorData.start()

'''
setting the running time 10 seconds but since it is in while loop,
it runs as an infinite loop
'''
while True:
    sleep(10)
    pass
