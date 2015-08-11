import shutil
import time
import os
import wx

class Spoofer(wx.Frame):
    extensions = {'.exe' : 'exe',
                  '.jpg' : 'gpj',
                  '.png' : 'gnp',
                  '.pdf' : 'fdp',
                  '.mp4' : '4pm',
                  '.avi' : 'iva',
                  '.txt' : 'txt'}

    def __init__(self):
        self.InitUI()

    def InitUI(self):
        wx.Frame.__init__(self, None, -1, 'Extension Spoofer', size=(335,100), style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER ^ wx.MAXIMIZE_BOX)

        self.panel = wx.Panel(self)
        self.SetBackgroundColour('#ECF0F1')
        
        wx.StaticText(self, -1, '   File:', pos=(16,11))
        self.file_input = wx.TextCtrl(self, -1, pos=(48,8), size=(267,24), style=wx.TE_READONLY)
        self.file_input.SetValue('PRESS OPEN TO CHOOSE A FILE')
        
        wx.StaticText(self, -1, '    Ext:', pos=(16,38))
        self.ext = wx.ComboBox(self, -1, '', pos=(48,35), choices=self.extensions.keys(), style=wx.CB_READONLY)
        
        self.open_file = wx.Button(self, 101, 'Open', pos=(136,34))
        self.Bind(wx.EVT_BUTTON, self.OpenFile, id=101)
        
        self.spoof = wx.Button(self, 102, 'Spoof', pos=(228,34))
        self.Bind(wx.EVT_BUTTON, self.SpoofFile, id=102)
        
        self.Centre()
        self.Show()
        
    def OpenFile(self, event):
        default_path = os.path.splitdrive(os.getenv('WINDIR'))[0] + '\\'
        file_dialog = wx.FileDialog(self, 'Open File', default_path, '', 'All Files (*.*)|*.*', wx.OPEN)
        
        if file_dialog.ShowModal() == wx.ID_OK:
            self.fname = str(file_dialog.GetFilename())
            self.fdir = str(file_dialog.GetDirectory())
            self.curr_extension = os.path.splitext(self.fname)[1]

            self.file_input.SetValue(os.path.join(self.fdir, self.fname))
            return 0
        else:
            return 1
    
    def SpoofFile(self, event):
        self.error = 0

        if self.file_input.GetValue() == '' or self.file_input.GetValue() == 'PRESS OPEN TO CHOOSE A FILE':
            wx.MessageBox('Please choose the file to be spoofed.', 'Error!', wx.OK | wx.ICON_ERROR)
            self.error += 1

        if self.ext.GetValue() == '':
            wx.MessageBox('Please choose the extension to use.', 'Error!', wx.OK | wx.ICON_ERROR)
            self.error += 1

        if self.error != 0:
            return 1
        
        dir_dialog = wx.DirDialog(self, 'Choose A Backup Location', self.fdir)
        
        if dir_dialog.ShowModal() == wx.ID_OK:
            self.bak_dir = str(dir_dialog.GetPath())
            self.bak_path = os.path.join(self.bak_dir, (self.fname + '.bak'))
            
            self.ext_type = self.ext.GetValue()
            self.path = str(self.file_input.GetValue())
            
            try:
                shutil.copyfile(self.path, self.bak_path)
            except IOError:
                wx.MessageBox('An IO error hase occured.\nTry running as administrator.', 'Error!', wx.OK | wx.ICON_ERROR)
                return 1
        else:
            return 1

        time.sleep(2)
        
        try:
            new_fname = os.path.splitext(self.fname)[0] + u'\u202E' + self.extensions.get(self.ext_type) + self.curr_extension
            os.chdir(self.fdir)
            os.rename(self.path, new_fname)
        
            wx.MessageBox('Successfuly Spoofed Extension.', 'Success!', wx.OK | wx.ICON_INFORMATION)
            return 0
        except:
            wx.MessageBox('An error during spoofing has occured.\nTry running as administrator.', 'Error!', wx.OK | wx.ICON_ERROR)
            return 1


if __name__ == '__main__':
    app = wx.App()
    Spoofer()
    app.MainLoop()
