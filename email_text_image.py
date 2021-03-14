#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import necessary packages
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
import smtplib
 
# create message object instance
msg = MIMEMultipart()

message = "Thank you"

# setup the parameters of the message
password = "Tula@123"
msg['From'] = "sourav.das1498@gmail.com"
msg['To'] = "sdas121196@gmail.com"
msg['Subject'] = "Photos"
file = "C:/Users/HP/DEASYSOFT Tech Pvt Ltd/1st project/database/train_new/Sourav/1.jpg"


# attach image to message body
fp = open(file, 'rb')
img = MIMEImage(fp.read())
fp.close()
msg.attach(img)
msg.attach(MIMEText(message, 'plain'))
 # create server
server = smtplib.SMTP('smtp.gmail.com: 587')
 
server.starttls()
 
# Login Credentials for sending the mail
server.login(msg['From'], password)
 
# send the message via the server
server.sendmail(msg['From'], msg['To'], msg.as_string())
 
server.quit()
 
print ("successfully sent email to %s:" % (msg['To']))


# In[ ]:




