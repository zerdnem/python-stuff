#!/usr/bin/env python
# This code was written for Python 3.1.1
# version 0.101

# Changelog:
# version 0.100
# Basic framework
#
# version 0.101
# Fixed an error if an admin used a command with an argument, that wasn't an admin-only command

import socket, sys, threading, time

# Hardcoding the root admin - it seems the best way for now
root_admin = "maslen"

# Defining a class to run the server. One per connection. This class will do most of our work.
class IRC_Server:

    # The default constructor - declaring our global variables
    # channel should be rewritten to be a list, which then loops to connect, per channel.
    # This needs to support an alternate nick.
    def __init__(self, host, port, nick, channel , password =""):
        self.irc_host = host
        self.irc_port = port
        self.irc_nick = nick
        self.irc_channel = channel
        self.irc_sock = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
        self.is_connected = False
        self.should_reconnect = False
        self.command = ""

    
    # This is the bit that controls connection to a server & channel.
    # It should be rewritten to allow multiple channels in a single server.
    # This needs to have an "auto identify" as part of its script, or support a custom connect message.
    def connect(self):
        self.should_reconnect = True
        try:
            self.irc_sock.connect ((self.irc_host, self.irc_port))
        except:
            print ("Error: Could not connect to IRC; Host: " + str(self.irc_host) + "Port: " + str(self.irc_port))
            exit(1) # We should make it recconect if it gets an error here
        print ("Connected to: " + str(self.irc_host) + ":" + str(self.irc_port))
        
        str_buff = ("NICK %s \r\n") % (self.irc_nick)
        self.irc_sock.send (str_buff.encode())
        print ("Setting bot nick to " + str(self.irc_nick) )
        
        str_buff = ("USER %s 8 * :X\r\n") % (self.irc_nick)
        self.irc_sock.send (str_buff.encode())
        print ("Setting User")
        # Insert Alternate nick code here.
        
        # Insert Auto-Identify code here.
        
        str_buff = ( "JOIN %s \r\n" ) % (self.irc_channel)
        self.irc_sock.send (str_buff.encode())
        print ("Joining channel " + str(self.irc_channel) )
        self.is_connected = True
        self.listen()
    
    def listen(self):
        while self.is_connected:
            recv = self.irc_sock.recv( 4096 )
            if str(recv).find ( "PING" ) != -1:
                self.irc_sock.send ( "PONG ".encode() + recv.split() [ 1 ] + "\r\n".encode() )
            if str(recv).find ( "PRIVMSG" ) != -1:
                irc_user_nick = str(recv).split ( '!' ) [ 0 ] . split ( ":")[1]
                irc_user_host = str(recv).split ( '@' ) [ 1 ] . split ( ' ' ) [ 0 ]
                irc_user_message = self.data_to_message(str(recv))
                print ( irc_user_nick + ": " + irc_user_message)
                # "!" Indicated a command
                if ( str(irc_user_message[0]) == "!" ):
                    self.command = str(irc_user_message[1:])
                    # (str(recv)).split()[2] ) is simply the channel the command was heard on.
                    self.process_command(irc_user_nick, ( (str(recv)).split()[2] ) )
        if self.should_reconnect:
            self.connect()
    
    def data_to_message(self,data):
        data = data[data.find(':')+1:len(data)]
        data = data[data.find(':')+1:len(data)]
        data = str(data[0:len(data)-5])
        return data
        
    # This function sends a message to a channel, which must start with a #.
    def send_message_to_channel(self,data,channel):
        print ( ( "%s: %s") % (self.irc_nick, data) )
        self.irc_sock.send( (("PRIVMSG %s :%s\r\n") % (channel, data)).encode() )
    
    # This function takes a channel, which must start with a #.
    def join_channel(self,channel):
        if (channel[0] == "#"):
            str_buff = ( "JOIN %s \r\n" ) % (channel)
            self.irc_sock.send (str_buff.encode())
            # This needs to test if the channel is full
            # This needs to modify the list of active channels
            
    # This function takes a channel, which must start with a #.
    def quit_channel(self,channel):
        if (channel[0] == "#"):
            str_buff = ( "PART %s \r\n" ) % (channel)
            self.irc_sock.send (str_buff.encode())
            # This needs to modify the list of active channels
    
        
    # This nice function here runs ALL the commands.
    # For now, we only have 2: root admin, and anyone.
    def process_command(self, user, channel):
        # This line makes sure an actual command was sent, not a plain "!"
        if ( len(self.command.split()) == 0):
            return
        # So the command isn't case sensitive
        command = (self.command).lower()
        # Break the command into pieces, so we can interpret it with arguments
        command = command.split()
        
        # All admin only commands go in here.
        if (user == root_admin):
            # The first set of commands are ones that don't take parameters
            if ( len(command) == 1):

                #This command shuts the bot down.    
                if (command[0] == "quit"):
                    str_buff = ( "QUIT %s \r\n" ) % (channel)
                    self.irc_sock.send (str_buff.encode())
                    self.irc_sock.close()
                    self.is_connected = False
                    self.should_reconnect = False
                    
            # These commands take parameters
            else:
                
                # This command makes the bot join a channel
                # This needs to be rewritten in a better way, to catch multiple channels
                if (command[0] == "join"):
                    if ( (command[1])[0] == "#"):
                        irc_channel = command[1]
                    else:
                        irc_channel = "#" + command[1]
                    self.join_channel(irc_channel)
                    
                # This command makes the bot part a channel
                # This needs to be rewritten in a better way, to catch multiple channels
                if (command[0] == "part"):
                    if ( (command[1])[0] == "#"):
                        irc_channel = command[1]
                    else:
                        irc_channel = "#" + command[1]
                    self.quit_channel(irc_channel)

                
        # All public commands go here
        # The first set of commands are ones that don't take parameters
        if ( len(command) == 1):
        
            if (command[0] == "hi"):
                self.send_message_to_channel( ("Hello to you too, " + user), channel )
            if (command[0] == "moo"):
                self.send_message_to_channel( ("MOO yourself, " + user), channel )
            if (command[0] == "train"):
                self.send_message_to_channel( ("Choo Choo! It's the MysteryTrain!"), channel )
            if (command[0] == "poo"):
                self.send_message_to_channel( ("Don't be a potty mouth"), channel )
            if (command[0] == "readnext"):
                self.send_message_to_channel( ("Visit whatshouldIreadnext.com"), channel )
        else:
            if (command[0] == "bop"):
                self.send_message_to_channel( ("\x01ACTION bopz " + str(command[1]) + "\x01"), channel )
            

# Here begins the main programs flow:

test2 = IRC_Server("irc.irchighway.net", 6667, "masbot", "#test")
test = IRC_Server("irc.malvager.com", 6667, "masbot", "#malvager")
run_test = threading.Thread(None, test.connect)
run_test.start()

while (test.should_reconnect):
    time.sleep(5) 

