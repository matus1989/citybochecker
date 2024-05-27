import argparse
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

# parser = argparse.ArgumentParser()
# parser.add_argument("sender",help="Sender Email",type=str)
# parser.add_argument("reciver", help="Reciver Email",type=str)
# parser.add_argument("password",help="Sender Password",type=str)

# args = parser.parse_args()

# sender_email = args.sender 
# receiver_email = str(args.reciver) 
# password = str(args.password) 

# print(sender_email)
# print(receiver_email)
# print(password)

def send(sender,reciver,password,body):
    sender_email = sender
    receiver_email = reciver 
    password = password 

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = Header('City Box available rooms', 'utf-8').encode()
    
    b = "\n"
    b = b.join(body)
    print (b)
    msg_content = MIMEText(b, 'plain', 'utf-8')
    msg.attach(msg_content)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP("smtp-mail.outlook.com", 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()