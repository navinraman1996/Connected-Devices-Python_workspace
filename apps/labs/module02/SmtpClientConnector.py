'''
Created on Jan 24, 2019
@author: Navin Raman
'''

import smtplib # Importing smtplib for the actual sending function

from labs.common            import ConfigUtil
from labs.common            import ConfigConst

from email.mime.multipart   import MIMEMultipart
from email.mime.text        import MIMEText # Importing the email modules we'll need

class SmtpClientConnector(object):
    '''
    This class is used to email sensor data's to a remote service
    '''

    def __init__(self):
        self.config = ConfigUtil.ConfigUtil('../../../config/ConnectedDevicesConfig.props')
        self.config.loadConfig()
        
        print('Configuration data...\n' + str(self.config) +'\n')
    
    '''
    The function publishMessage is used to create a Notification message which
    will be sent to the user if the temperature surpassed the threshold value
    
    @param topic: Subject of the Email
    @param data: Sensor data which is the notification        
    '''    
    def publishMessage(self, topic, data):
        host        = self.config.getProperty(ConfigConst.ConfigConst.SMTP_CLOUD_SECTION, ConfigConst.ConfigConst.HOST_KEY)
        port        = self.config.getProperty(ConfigConst.ConfigConst.SMTP_CLOUD_SECTION, ConfigConst.ConfigConst.PORT_KEY)
        fromAddr    = self.config.getProperty(ConfigConst.ConfigConst.SMTP_CLOUD_SECTION, ConfigConst.ConfigConst.FROM_ADDRESS_KEY)
        toAddr      = self.config.getProperty(ConfigConst.ConfigConst.SMTP_CLOUD_SECTION, ConfigConst.ConfigConst.TO_ADDRESS_KEY)
        authToken   = self.config.getProperty(ConfigConst.ConfigConst.SMTP_CLOUD_SECTION, ConfigConst.ConfigConst.USER_AUTH_TOKEN_KEY)
        '''
        assigning the values host and port key, from and to address and
        the user authorization key from ConfigConst
        '''
        
        msg = MIMEMultipart() 
        #contains a list of more than one message
        msg['From'] = fromAddr
        msg['To'] = toAddr
        msg['Subject'] = topic
        msgBody = str(data)
        #attaching the MIME text with the data in the body into one message
        msg.attach(MIMEText(msgBody)) 
        
        msgText = msg.as_string()
        # send e-mail notification
        try:  
            smtpServer = smtplib.SMTP_SSL(host, port)
            #An SMTP instance encapsulates an SMTP connection
            smtpServer.ehlo()
            smtpServer.login(fromAddr, authToken)
            smtpServer.sendmail(fromAddr, toAddr, msgText)
            smtpServer.close()
        
        except:
            print("Error appeared during Sending Mail")
            
        finally:
            smtpServer.close();