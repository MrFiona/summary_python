'''
Created on 2016年7月30日

@author: apple
'''
#!/usr/bin/env python 
#-*-coding:utf-8-*-

from tkinter import *
from tkinter.messagebox import *    

warn_info_flag = 0

def warn_info1():
    if e1.get() == '' or e1.get().isdigit() == False:
        askokcancel(title="yes or not?", message="are you sure the data is correctly?")
        e1.delete(0, END)
        return False
    elif e1.get().isdigit() == True:
        return True
        
def warn_info2():
    if e2.get() == '' or e2.get().isdigit() == False:
        askokcancel(title="yes or not?", message="are you sure the data is correctly?")
        e2.delete(0, END)
        return False
    elif e2.get().isdigit() == True:
        return True

def warn_info17():
    if e17.get() == '' or e17.get().isdigit() == False:
        askokcancel(title="yes or not?", message="are you sure the data is correctly?")
        e17.delete(0, END)
        return False
    elif e17.get().isdigit() == True:
        return True
    
def show_info():
    insert_text = "windows ID:" + e1.get() + "\nMrFiona:" + e2.get() + "\nJohn Mei:" + e3.get() + "\nvegetables ID:" + e4.get() + "\n"
    text.insert(INSERT, insert_text)

def clear_info():
    text.delete(1.0, END)
    
def start():
    pass
    
def end():
    pass

def choose():
    filename = filedialog.askopenfilename(initialdir="please choose topo：")
    e16.insert(0, filename)
    return filename 

def built_eip():
    print("这个函数是申请EIP用的")

def print_id():
    print(var.get())
    
root = Tk()
root.geometry("912x611")

Label(root, text="windows镜像", font=("华康少女字体", 14)).grid(row=0, column=0, columnspan=2, padx=10, pady=5)
Label(root, text="FTP镜像", font=("华康少女字体", 14)).grid(row=0, column=2, columnspan=2, padx=10, pady=5)
Label(root, text="其他镜像", font=("华康少女字体", 14), ).grid(row=0, column=4, columnspan=2, padx=10, pady=5)

Label(root, text="windows ID:", font=("黑体", 14)).grid(row=1, column=0, sticky=E, padx=10, pady=5)
Label(root, text="MrFiona:", font=("黑体", 14)).grid(row=2, column=0, sticky=E, padx=10, pady=5)
Label(root, text="John Mei:", font=("黑体", 14)).grid(row=3, column=0, sticky=E, padx=10, pady=5)
Label(root, text="Li Hua:", font=("黑体", 14)).grid(row=4, column=0, sticky=E, padx=10, pady=5)
Label(root, text="vegetables ID:", font=("黑体", 14)).grid(row=5, column=0, sticky=E, padx=10, pady=5)

e1 = Entry(root)
e2 = Entry(root)
e3 = Entry(root)
e4 = Entry(root)
e5 = Entry(root)

e1.grid(row=1, column=1)
e2.grid(row=2, column=1)
e3.grid(row=3, column=1)    
e4.grid(row=4, column=1)
e5.grid(row=5, column=1)

e6 = Entry(root)
e7 = Entry(root)    
e8 = Entry(root)
e9 = Entry(root)
e10 = Entry(root)

e6.grid(row=1, column=3)
e7.grid(row=2, column=3)
e8.grid(row=3, column=3)
e9.grid(row=4, column=3)
e10.grid(row=5, column=3)

e11 = Entry(root)
e12 = Entry(root)    
e13 = Entry(root)
e14 = Entry(root)
e15 = Entry(root)

e11.grid(row=1, column=5)
e12.grid(row=2, column=5)
e13.grid(row=3, column=5)
e14.grid(row=4, column=5)
e15.grid(row=5, column=5)

Button(root, text="开始", width=10, font=("华康少女字体", 12), command=start).grid(row=5, column=2, padx=20, pady=5)
Button(root, text="结束", width=10, font=("华康少女字体", 12), command=end).grid(row=5, column=4, padx=20, pady=5)
Button(root, text="选择TOPO", width=10, font=("黑体", 12), command=choose).grid(row=6, column=0, padx=10, pady=5)
Button(root, text="创建EIP", width=10, font=("黑体", 12), command=built_eip).grid(row=6, column=2, padx=10, pady=5)

e16 = Entry(root)
e17 = Entry(root, validate="focusout", validatecommand=warn_info17)
e18 = Entry(root)

e16.grid(row=6, column=1)
e17.grid(row=6, column=3)
e18.grid(row=7, column=1)

v = StringVar() 
v.set("please choose suitable topo")
e16.insert(0, v.get())

var = StringVar()
var.set("True")

Checkbutton(root, text="创建新的VPC", variable=var, onvalue="True", offvalue="False", command=print_id).grid(row=7, column=0, padx=10, pady=5)
Button(root, text="获取信息", command=show_info).grid(row=7, column=3, padx=10, pady=5)
Button(root, text="退出", command=root.quit).grid(row=7, column=4, padx=10, pady=5)
Button(root, text="显示", command=show_info).grid(row=7, column=5, padx=10, pady=5)
Button(root, text="清除", command=clear_info).grid(row=7, column=6, padx=10, pady=5)

text = Text(root)
w = text.grid(row=8, columnspan=7, rowspan=4, sticky=N+S+W+E)
#w.grid_bbox(column=0, row=8, clo2=6, row2=10)
#w.grid_configure(row=8, columnspan=4, rowspan=4, sticky=N+S+W+E)

mainloop()
