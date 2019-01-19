'''
Created on Jan 18, 2019

@author: Navin Raman
'''
import psutil #importing psutil library
import datetime #importing datetime library for executing the boot time value
from time import sleep #importing sleep function from time library to set delay
from threading import Thread #importing Thread function from threading

class SystemPerformanceAdaptor(Thread): 
    '''
    Creating a class called SystemPerformanceAdaptor where this class implements thread
    '''
    def __init__(self):
        
        Thread.__init__(self) #used to initialize the class object
        self.enable_adap = False
        '''   
        This Constructor is initialized in __init__; and the enable_adap flag is set to False
        '''
  
    def run(self):#This function contains all the code items which has to execute and print in the console output tab
        while self.enable_adap:
                        
            print('-----------------------------------------------------------------------------------------------------------------------------------------');
            print("                                                New system performance readings:                                                         ");
            print("Boot Time: " + str(datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")))#Returns boot time of the device in date HH/MM/SS format

            print("                                          **********PRINTING MEMORY DETAILS**********                                                   \n");
            print("Memory details:  " + str(psutil.virtual_memory()) + "\n")#Returns memory status of the device
            
            print("                                          ***********PRINTING CPU DETAILS************                                                    ");
            print("No. of CPU:      " + str(psutil.cpu_count()))#Returns number of logical CPUs in the device
            print("CPU status:      " + str(psutil.cpu_stats()))#Returns CPU status of the device
            print("Freq details:    " + str(psutil.cpu_freq()))#Return CPU frequency as a nameduple including current, min and max frequencies expressed in Mhz
            print("Time details:    "+ str(psutil.cpu_times(True)) + "\n")#Return system CPU times as a named tuple for each CPU
            
            sleep(7) #Delay of 7 seconds for every new system performance readings
                 
                          
    def en_Adaptor(self):
        self.enable_adap = True #Thread will be executed only when the enable_adap flag is to True in the en_Adaptor function