'''
Created on Jan 18, 2019

@author: Navin Raman
'''

from time import sleep #importing sleep function from time library to set delay
from labs.module01 import SystemPerformanceAdaptor #importing SystemperformaceAdaptor class for executing system performance value

sys_Perf_Adaptor = SystemPerformanceAdaptor.SystemPerformanceAdaptor() #New thread to measure system performance values
sys_Perf_Adaptor.daemon = True #setting this Thread as Daemon thread
sys_Perf_Adaptor.en_Adaptor() #To start the thread to running, enabling the adaptor

print("Starting system performance app daemon thread...\n")
sys_Perf_Adaptor.start() #starting the Thread 

while (True):
    sleep(7) #setting the running time for 7 seconds but since it is in while loop, this will automatically start the next 7 seconds and run until the loop is false
    pass













