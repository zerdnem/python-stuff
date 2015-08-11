import time
import os
BT = 'bittorrent'
Word = 'word'
PPT = 'powerpoint'
GC = 'google chrome'
GP = 'gimp'
FF = 'firefox'

name = raw_input ('Enter name: ')
if name == 'Isabella':
    access = raw_input ('Enter password to access this application: ')
    if access == 'isabella':
        password = raw_input ('Enter program name: \n \n bittorrent, word, powerpoint, \n google chrome, firefox, gimp.....\n \n ')
    else:
        print 'Incorrect password; try again'
        raw_input ('Click <enter> to exit program... ')

    if password == BT:
        print 'Opening BitTorrent'
        time.sleep(2)
        os.chdir(r'C:\Program Files (x86)\BitTorrent')
        os.startfile('bittorrent.exe')
    elif password == Word:
        print 'Opening MS Word Enterprise'
        time.sleep(2)
        os.chdir(r'C:\Program Files (x86)\Microsoft Office\Office12')
        os.startfile('WINWORD.exe')
    elif password == PPT:
        print 'Opening MS PowerPoint Enterprise'
        time.sleep(2)
        os.chdir(r'C:\Program Files (x86)\Microsoft Office\Office12')
        os.startfile('POWERPNT.exe')
    elif password == GC:
        print 'Opening MS PowerPoint Enterprise'
        time.sleep(2)
        os.chdir(r'C:\Users\Isabella\AppData\Local\Google\Chrome\Application')
        os.startfile('chrome.exe')
    elif password == GP:
        print 'Opening GIMP'
        time.sleep(2)
        os.chdir(r'C:\Program Files (x86)\GIMP-2.0\bin')
        os.startfile('gimp-2.6.exe')
    elif password == FF:
        print 'Opening FireFox'
        time.sleep(2)
        os.chdir(r'C:\Program Files (x86)\Mozilla Firefox')
        os.startfile('firefox.exe')
    else:
        print ('Sorry, this program is not currently in the database... ')
        time.sleep(2)
        raw_input ('Click <enter> to exit program... ')
else:
    print 'Incorrect username; try again'
    raw_input ('Click <enter> to exit program... ')
