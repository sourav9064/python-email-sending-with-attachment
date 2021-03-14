#!/usr/bin/env python
# coding: utf-8

# In[3]:


import smtplib, ssl

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "sourav.das1498@gmail.com"  # Enter your address
receiver_email = "sdas121196@gmail.com","sourav.das2k2k@gmail.com"  # Enter receiver address
password = "Tula@123"
message = """Subject: Hi there

Take Care."""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)


# In[ ]:




