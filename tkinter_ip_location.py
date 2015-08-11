from Tkinter import *
import tkMessageBox
import json
import urllib
import sys

def wmi():
    uip = urllib.urlopen("http://www.networksecuritytoolkit.org/nst/tools/ip.php").read()
    tkMessageBox.showinfo("Whats my IP", "Your IP is "+uip)
def mbt():

    global ew1
    
    tget = ew1.get().strip()
    
    jd = json.load(urllib.urlopen("http://ipinfo.io/"+tget+"/geo"))
    
    if tget == "":
        tkMessageBox.showerror(tget, "Type a IP Please")
    else:
        tkMessageBox.showinfo(tget, tget+" lives in "+jd["city"]+", "+jd["region"]+" "+jd["country"]) 

if __name__ == "__main__":

    root = Tk()
    
    root.title("-|IP2Location|-")
    
    textFrame = Frame(root)
    
    entryLabel = Label(textFrame)
    entryLabel["text"] = "IP :"
    entryLabel.pack(side=LEFT)

    ew1 = Entry(textFrame)
    ew1["width"] = 24
    ew1.pack(side=LEFT)

    textFrame.pack()
    
    bmi = Button(root, text="Whats my IP", command=wmi)
    bmi.pack()
    
    bs = Button(root, text="Submit", command=mbt)
    bs.pack()
    
    def enterPress(event):
        mbt()

    root.bind("<Return>", enterPress)
    
    def enterPress(event):
        exit()
        sys.exit(0)

    root.bind("<Escape>", enterPress)
    root.mainloop()
