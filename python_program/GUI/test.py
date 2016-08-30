'''
Created on 2016年7月31日

@author: apple
'''
#!/usr/bin/env python 
#coding:utf-8
    
from tkinter import *
from tkinter import colorchooser#使用colorchooser模块下方法必须导入colorchooser

root = Tk()
root.title("我的测试窗口") 

# Label(root, text="用户名").grid(row=0, padx=10, pady=5)
# Label(root, text="密码").grid(row=1, padx=10, pady=5)

# Entry(root).grid(row=0, column=1, padx=10, pady=5)
# Entry(root, show="*").grid(row=1, column=1, padx=10, pady=5)
# listbox = Listbox(root)
# listbox.pack(fill=BOTH, expand=True)

# for i in range(10):
#     listbox.insert(0, str(i))

# Button(root, text="asdsadqwe").pack(anchor=W)#padx=100, pady=50, ipadx=10, ipady=10)
# b = Button(root, text="asdsadqwe")
# b.pack_configure(padx=50, pady=30)
# b.pack_forget()
# b.pack()
# print(b.pack_info())
# print(root.pack_slaves())

check_flag = 0

def func():
    global check_flag
    if var.get() == "ON":
        check_flag = 1
#         print("check_flag:", check_flag, "已开启按钮")
        print("check_flag: %s 已开启按钮" %check_flag)
    elif var.get() == "OFF":
        check_flag = 0
        print("check_flag:", check_flag, "已关闭按钮")

v = StringVar()
v.set('新的文本行')

Label(root, text="用户名", justify=LEFT).grid(row=0, column=0, sticky=W)
Label(root, text="密码", justify=LEFT).grid(row=1, column=0, sticky=W)
Label(root, textvariable=v, justify=LEFT).grid(row=2, column=0, sticky=W)

Entry(root).grid(row=0, column=1)
Entry(root).grid(row=1, column=1)
Entry(root).grid(row=2, column=1)

# photo = PhotoImage(file="22.gif")
# Label(root, image=photo).grid(row=0, column=2, rowspan=3, padx=5, pady=5)

var = StringVar()
var.set("ON")

Button(root, text="提交", relief=GROOVE).grid(row=3, columnspan=3, pady=5)
Checkbutton(root, text="测试按钮", onvalue="ON", offvalue="OFF", variable=var, command=func).grid(row=4, column=0, pady=5)
print(var.get())

def callback():
    fileName = colorchooser.askcolor(title="选择颜色", parent=root)
    print(fileName)

Button(root, text="选择颜色", command=callback).grid(row=5, column=0, pady=5)


mainloop()