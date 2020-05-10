import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
def feedback(msg,name,emailid):
    mail_content = '\nName: ' +name+ '\nEmail: '+emailid+'\nMessage: '+msg
    
    #The mail addresses and password
    sender_address = 'test@spm.technofiz.com'
    sender_pass = 'test@123'
    receiver_address = 'hyderdanyal@gmail.com'
    #Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'Feedback recieved from The New Chapter(TNC)'   #The subject line
    #The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'plain'))
    #Create SMTP session for sending the mail
    session = smtplib.SMTP('mail.spm.technofiz.com', 587) #use gmail with port
    session.starttls() #enable security
    session.login(sender_address, sender_pass) #login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print('Mail Sent')
    