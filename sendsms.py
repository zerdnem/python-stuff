import ssh, sys, time



HOST = '192.168.1.17' 
USERNAME = 'root'
PASSWORD = 'alpine'
PORT = 22

def tel_number():
    """ recipient
    """
    number = raw_input("\n\nRecipient number : ")
    return number

def message():
    """ message to send
    """
    sms = raw_input("\n\nType your message : ")
    return str(sms)

def send(data):
    """ ssh socket command
    """
    s.execute(data)

try:
    s = ssh.Connection(host = HOST, username = USERNAME,
                   password = PASSWORD, port = PORT)
    title()
    print "Connection established on", HOST
except:
    print "Host unreachable.. check iPhone IP & PORT"
    print "Your config is : ",HOST,":",PORT
    sys.exit(1)
    
recipient = tel_number()
hold = message()
data = 'sendsms ' + recipient + ' ' + '"' + hold + '"'

while len(data) <= 8:
                            
    if len(tel_number) < 10:
        print "tel number error"
        
    if len(contenu) <= 0:
        print "the message box is empty !?"
        
    sys.exit(1)

send(data)
print "\n\nMessage Sent !"      
s.close()
