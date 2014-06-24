import smtplib
from email.mime.text import MIMEText as text

def send_email(sender,receiver,message,subject):
    sender=sender
    receivers=receiver
    m=text(message)
    m['Subject']=subject
    m['From']=sender
    m['To']=receiver

    try:
        smtpObj=smtplib.SMTP('localhost')
        smtpObj.sendmail(sender,receivers,str(m))
        print "Success"
    except smtplib.SMTPException:
        print "Error"
