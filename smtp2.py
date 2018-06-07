#!/usr/bin/python3

# send_attachment.py
# import necessary packages
import os
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
import smtplib
 
# create message object instance
msg = MIMEMultipart()
 
 
# setup the parameters of the message
password = "*********"
msg['From'] = "abc@gmail.com"
msg['To'] = "xyz@rst.com"
msg['Subject'] = "photos"
# attach image to message body

# Assume we know that the image files are all in PNG format
#for file in pngfiles:
    # Open the files in binary mode.  Let the MIMEImage class automatically
    # guess the specific image type.
with open("messi.jpeg", 'rb') as fp:
	img = MIMEImage(fp.read())
	msg.attach(img)
#msg.as_string = msg.attach(MIMEImage(file("messi.jpeg").read())
 
 
# create server
server = smtplib.SMTP('smtp.gmail.com: 587')

server.starttls()
 
# Login Credentials for sending the mail
server.login(msg['From'], password)
 
 
# send the message via the server.
server.sendmail(msg['From'], msg['To'],msg.as_string())
 
server.quit()

