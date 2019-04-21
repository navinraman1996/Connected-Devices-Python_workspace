'''
Created on Jan 19, 2019

@author: Navin Raman
'''

import smtplib  # Import smtplib for the actual sending function
from email.mime.text import MIMEText    # Import the email modules we'll need
from email.mime.multipart import MIMEMultipart
from project import ConfigUtil

'''
This class is for Simple Mail Transfer Protocol (SMTP) client
which is used to send mail to the user
'''
class SmtpClientConnector(object):
    config = None

    '''
    Constructor to initialize and load configuration file.
    '''
    def __init__(self):
        self.config = ConfigUtil.ConfigUtil()
        self.config.loadConfig()

    '''
    This function gets the individual configuration properties
    to establish SMTP client and sends mail.
    @param topic: email subject.
    @param data: email body. 
    '''
    def publishMessage(self, topic, data):
        
        host        = self.config.getProperty(self.config.configConst.SMTP_CLOUD_SECTION, self.config.configConst.HOST_KEY)
        port        = self.config.getProperty(self.config.configConst.SMTP_CLOUD_SECTION, self.config.configConst.PORT_KEY)
        fromAddr    = self.config.getProperty(self.config.configConst.SMTP_CLOUD_SECTION, self.config.configConst.FROM_ADDRESS_KEY)
        toAddr      = self.config.getProperty(self.config.configConst.SMTP_CLOUD_SECTION, self.config.configConst.TO_ADDRESS_KEY)
        authToken   = self.config.getProperty(self.config.configConst.SMTP_CLOUD_SECTION, self.config.configConst.USER_AUTH_TOKEN_KEY)
        
        msg         = MIMEMultipart()
        msg['From'] = fromAddr
        msg['To']   = toAddr
        msg['Subject'] = topic
        msgBody     = str(data)
        
        msg.attach(MIMEText(msgBody))
        msgText = msg.as_string()
        
        print('\nmsgText : ' + msgText)
        
        # send e-mail notification
        smtpServer = smtplib.SMTP_SSL(host, port)
        smtpServer.ehlo()
        smtpServer.login(fromAddr, authToken)
        smtpServer.sendmail(fromAddr, toAddr, msgText)
        smtpServer.close()