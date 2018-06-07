#usr/lib/python3

import smtplib

sender_mail1 = "rohansinghal.cse19@jecrc.ac.in"
sender_passwd2 = "tycoon27"

#creating smtp object

sm = smtplib.SMTP("smtp.gmail.com" ,587)
try:
	sm.starttls()   #start TLS for security

	sender_mail = sender_mail1
	sender_passwd = sender_passwd2


#authentic

	sm.login(sender_mail,sender_passwd)
	print("authentication success")

	receiver_mail = input("receiver mail id:")
	msg = input("enter message:")

	sm.sendmail(sender_mail,receiver_mail,msg)
	print("successfully sent")

except Exception as e:
	print("ERROR:e")
sm.quit()
