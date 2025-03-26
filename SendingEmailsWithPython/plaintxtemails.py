import smtplib, ssl

smtp_server = 'smtp.gmail.com'
port = 465

sender = 'pydevtesting22@gmail.com'
password = input("Enter your app password here: ")

recepient = 'joeldapo14@gmail.com'
message = """\
From: {}
To: {}
Subject: Sending An Email With a Python Script

Hello future me, this email was sent using a python script!
""".format(sender, recepient)

context = ssl.create_default_context()

with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender, password)
    server.sendmail(sender, recepient, message)
    print("Success")