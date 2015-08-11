from Tkinter import *

class calc(Frame):
    def __init__(self):
        global result
        top = Tk()
        top.title('UberCalc v2.0')
        Frame.__init__(self)
        result = Entry()
        result.pack(side=TOP)
        buttons = ['1', '2', '3','4', '5', '6','7', '8', '9','.', '0', 'Clear']
        operbtn = ['-','+', '*','/', '=']
        ro = 1
        col = 0
        for x in buttons:
            action = lambda y=x: onclick(y)
            Button(self, text=x, width=5, relief='ridge', command=action).grid(row=ro, column=col)
            col += 1
            if col > 2:
                col = 0
                ro += 1
        col = 4
        ro = 1
        for x in operbtn:
            action = lambda y=x:onclick(y)
            Button(self, text=x, width=5, relief='ridge', command=action).grid(row=ro, column=col)
            ro += 1

        def onclick(key):
            global result
            if key != '=' and key != 'Clear':
                result.insert(END, key)
            if key == '=':
                fetch = result.get()
                answer = eval(fetch)
                result.delete(0, END)
                result.insert(0, answer)
            if key == 'Clear':
                result.delete(0, END)

if __name__ == '__main__':
    window = calc()
    window.pack()
    window.mainloop()
