import smtplib, ssl, send
from socket import gaierror
port = 465
smtp_server = "smtp.gmail.com"
login = "seth.benson.test.email@gmail.com" # your login generated by Mailtrap
password = "test123test" # your password generated by Mailtrap
context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(login, password)

# specify the sender’s and receiver’s email addresses
sender = "seth.benson.test.email@gmail.com"
receiver = "seththebenson@gmail.com"

# type your message: use two newlines (\n) to separate the subject from the message body, and use 'f' to  automatically insert variables in the text
message = f"""\
Subject: Hi Mailtrap
To: {receiver}
From: {sender}

This is my first message with Python."""

try:
    #send your message with credentials specified above
    #with smtplib.SMTP(smtp_server, port) as server:
     #   server.login(login, password)
      #  server.sendmail(sender, receiver, message)
    yag = send.SMTP()
    contents = [
        "This is the body, and here is just text"
    ]
    yag.send('seththebenson@gmail.com', 'subject', contents)
    # tell the script to report if your message was sent or which errors need to be fixed
    print('Sent')
except (gaierror, ConnectionRefusedError):
    print('Failed to connect to the server. Bad connection settings?')
except smtplib.SMTPServerDisconnected:
    print('Failed to connect to the server. Wrong user/password?')
except smtplib.SMTPException as e:
    print('SMTP error occurred: ' + str(e))