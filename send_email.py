import smtplib
from email.mime.text import MIMEText

smtp_server = 'smtp.gmail.com'
port=587 #for TLS

#if we were using SSL the port number would be 465

sender_email = 'rohitdhamdhere953@gmail.com'
receiver_email = 'rohitdhamdhere43@gmail.com'

msg = "Hello!! This is an automated mail"

#Create a MIMEText objects for the email content 

msg = MIMEText(msg)
msg['Subject'] = 'Automated mail'
msg['From'] = sender_email
msg['To'] = receiver_email

#Set up connection to smtp server 

with smtplib.SMTP(smtp_server, port) as server:
    
    #start TLS encryption 
    server.starttls()
    
    #login to your gmail account
    
    password = input("enter your email password and press enter ")
    server.login(sender_email, password)
    
    #send email 
    
    server.sendmail(sender_email,[receiver_email], msg.as_string())
    





