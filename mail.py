import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

mail_content = '''Hello,
This is a simple mail. There is only text, no attachments are there The mail is sent using Python SMTP library.
Thank You
'''
message = MIMEMultipart()
message['From'] = "sender_address"
message['To'] = "reciever_address"
message['Subject'] = 'A test mail sent by Python.' 
context = ssl.create_default_context()
server=smtplib.SMTP_SSL("smtp.gmail.com",465)
server.login("sender_address","password")
subject='sending mail through python code'
message.attach(MIMEText(mail_content, 'plain'))
text = message.as_string()
server.sendmail("sender_address","reciever_address",text)
server.quit()