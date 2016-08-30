'''
Created on 2016年8月6日

@author: apple
'''
from tkinter import *
from tkinter.messagebox import *    
from tkinter import filedialog
from tkinter import simpledialog
from tkinter.colorchooser import askcolor

ff = Tk()

class My_Quitter(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.grid()
        button = Button(self, text='Quit', command=self.quit)
        button.grid(padx=40, pady=5)
        
    def quit(self):
        ask = askokcancel('Verify exit', 'Really quit?')
        if ask:
            Frame.quit(self)

# if __name__ == '__main__':
#     quit = My_Quitter() 
#     mainloop()

# root = Tk()
demos = {
         'Open': filedialog.askopenfilename,
         'Color': askcolor,
         'Query': lambda: askquestion('Warning', 'You typed rm * \ncofirm?'),
         'Error': lambda: showerror('Error', "He's dead, Jim"),
         'Iput': lambda: simpledialog.askfloat('Entry', 'Enter credit card number')
         }
class vvs(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.grid()
        
        
        Label(self, text='Check demos', font=("黑体", 14)).grid(row=0, column=0, columnspan=5)

        self.vars = []
        self.i = 0
        for key in demos:
            self.var = IntVar()
            Checkbutton(self, text=key, variable=self.var, command=demos[key]).grid(row=1, column=self.i)
            self.i+=1
            self.vars.append(self.var)
        self.list_items()
    def report(self):
#         for var in self.vars:
#             print(var.get(), end=' ')
#         print()
        print([var.get() for var in self.vars])
    
    def list_items(self):
#         fram = Frame(self)  #设置这个组件是为了和复选按钮更在同一个显示框里合适的显示出来
#         fram.grid(row=0, column=0)
        Button(self, text='State', command=self.report).grid(row=0, column=5)
        Button(self, text='Quit', command=self.quit).grid(row=1, column=5)

if __name__ == '__main__':
 
    vvs(ff)       
    mainloop()

def create():
    top = Toplevel()
    top.title("FishC Demo")

    msg = Message(top, text="I love FishC.com!")
    msg.pack()

# Button(root, text="创建顶级窗口", command=create).pack()

# mainloop()



