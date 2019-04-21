'''
Created on Jan 19, 2019

@author: Navin Raman
'''

import configparser
import os
from project import ConfigConst

'''
This class is used to load and get configuration properties.
'''
class ConfigUtil(object):
   
    configConst     = None #ConfigConst instance.
    isLoaded        = False #boolean to check configuration file loaded or not.
    configFilePath  = None #path of configuration file.
    configData      = None #configparser instance.

    '''
    ConfigUtil Constructor.
    '''
    def __init__(self):
        
        if (self.configData == None):
            self.configData = configparser.ConfigParser()
            
            
        if (self.configConst == None):
            self.configConst = ConfigConst.ConfigConst()

        self.configFilePath = self.configConst.DEFAULT_CONFIG_FILE_NAME
    
    '''
    This function checks whether configuration file is loaded.
    @return: 'isLoaded' - True, configuration file loaded orelse False. 
    '''
    def isConfigDataLoaded(self):
        return self.isLoaded

    '''
    This function is used to read the properties from configuration file
    and sets 'isLoaded' member variable.
    '''
    def loadConfig(self):
        
        if (os.path.exists(self.configFilePath)):
            self.configData.read(self.configFilePath)
            
            self.isLoaded = True

    '''
    This function is used to return the configuration file path.
    @return: 'configFilePath' - path of the configuration file.
    '''    
    def getConfigFile(self):
        return self.configFilePath

    '''
    This function is used to load the configuration properties data
    and return's it.
    @param forceReload: False, to forcefully reload the configuration file else True.
    @return: 'configData' - configuration file data.
    '''
    def getConfigData(self, forceReload = False):
        
        if (self.isLoaded == False or forceReload):
            self.loadConfig()
        return self.configData

    '''
    This function is used to return the individual property's value
    under the given section.
    @param section: name of the section in configuration file.
    @param key: name of the key under the section whose value is needed.
    @return: value of a given property.
    '''
    def getProperty(self, section, key, forceReload = False):
        return self.getConfigData(forceReload).get(section, key)    