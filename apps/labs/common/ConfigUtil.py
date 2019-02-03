'''
Created on Jan 24, 2019
@author: Navin Raman
'''

import configparser
import os
DEFAULT_CONFIG_FILE = "../data/ConnectedDevicesConfig.props"

'''
A simple utility wrapper around the built-in Python
configuration infrastructure.
'''
class ConfigUtil:
    '''
    classdocs
    '''
    configFile = DEFAULT_CONFIG_FILE
    configData = configparser.ConfigParser()
    isLoaded = False
    
    '''
    Constructor for ConfigUtil.
    
    @param configFile The name of the configuration file to load.
    '''
    def __init__(self, configFile = None):
        if (configFile != None):
            self.configFile = configFile
    
    '''
    Attempts to load the config file using the name passed into
    the constructor.

    '''      
    def loadConfig(self):
        if (os.path.exists(self.configFile)):
            self.configData.read(self.configFile)
            self.isLoaded = True
            
    '''
    Returns the entire configuration object. If the config file hasn't
    yet been loaded, it will be loaded.
    
    @param forceReload Defaults to false; if true, will reload the config.
    @return: The entire configuration file.
     
    '''           
    def getConfig(self, forceReload = False):
        if (self.isLoaded == False or forceReload):
            self.loadConfig()
            
        return self.configData
    
    '''
    Returns the name of the configuration file.
    
    @return: The name of the config file.
    '''
    def getConfigFile(self):
        return self.configFile
    
    '''
    Attempts to retrieve the value of 'key' from the config.
    
    @param: section The name of the section to parse.
    @param: key The name of the key to lookup in 'section'.
    @param: forceReload Defaults to false; if true will reload the config.
    @return: The property associated with 'key' in 'section'.
    '''
    def getProperty(self, section, key, forceReload = False):
        return self.getConfig(forceReload).get(section, key)
    
    '''
    Simple boolean check if the config data is loaded or not.
    
    @return: boolean True on success; false otherwise.
    '''
    def isConfigDataLoaded(self):
        return self.isLoaded