#Connecting to the Gmail sever with Python's smtplib library
import smtplib, ssl

smtp_server = 'smtp.gmail.com' # Gmail's SMTP server, which is used for sending emails
port = 465 #SSL port for securely connecting to Gmail’s SMTP server

sender = 'pydevtesting22@gmail.com' 
password = input("Enter your app password here: ")

context = ssl.create_default_context() # creates an SSL context, ensuring that the connection between Python and the SMTP server is encrypted and secure

with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender, password)
    print("Success")