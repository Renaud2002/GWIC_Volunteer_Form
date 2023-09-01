from email.message import EmailMessage
import ssl
import smtplib

sender = 'andrearante12@gmail.com'
password = 'vazaegqqqgkgunls'
reciever = 'andre.arante@gwmail.gwu.edu'

subject = 'Testing Python Email Script'
message = """ This is a test message sent by python to a gmail account """

em = EmailMessage()
em['From'] = sender
em['To'] = reciever
em['Subject'] = subject
em.set_content(message) 

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
	smtp.login(sender, password)
	smtp.sendmail(sender, reciever, em.as_string())

