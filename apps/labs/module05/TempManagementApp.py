'''
Created on Jan 24, 2019

@author: Navin Raman
'''

from time           import sleep
from labs.module05  import TempSensorAdaptor  

'''
New thread to measure temperature values and start the thread to run.
Creating a new temperature measurement object 
'''
print('Created DataUtil instance.\nStarting data formatter app test...\nCreated DataUtil instance.\nStarting temp adaptor app daemon thread...\n')
print('----------------------------------------------------------------')
sensorData = TempSensorAdaptor.TempSensorAdaptor("NEW TEMPERATURE DATA")  
sensorData.daemon = True;
sensorData.start() #starting the daemon thread

'''
setting the running time 10 seconds but since it is in while loop,
it runs as an infinite loop
'''
while True:
    sleep(1);
    pass
