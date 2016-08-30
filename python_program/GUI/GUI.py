'''
Created on 2016年7月29日
    
@author: apple
'''
#!/usr/bin/env python 
#-*-coding:utf-8-*-

import os
import time
import threading
import os.path
from tkinter import *
from tkinter.messagebox import *    
from tkinter import filedialog
from tkinter import simpledialog
from tkinter.colorchooser import askcolor

warn_info_flag = 0

demos = {
         'Open': filedialog.askopenfilename,
         'Color': askcolor,
         'Query': lambda: askquestion('Warning', 'You typed rm * \ncofirm?'),
         'Error': lambda: showerror('Error', "He's dead, Jim"),
         'Iput': lambda: simpledialog.askfloat('Entry', 'Enter credit card number')
         }

#Quit 封装的可复用的按钮
class Quitter(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.grid()
        self.button = Button(self, text='Quit', command=self.quit)
        self.button.grid()
        
    def quit(self):
        ask = askokcancel('Verify exit', 'Really quit?') #返回True, False  第一个参数和第二参数分别表示标题和显示提示的内容
        if ask:
            Frame.quit(self)
    def button(self):
        return self.button #返button按钮实例，以便在其他调用的地方进行相关设置

#滚动条Scrollbar与文本框Text组合
class MainFrame(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid(row=0, column=0, sticky="nsew")
        self.CreateScrollbar()
        
    def CreateScrollbar(self):
        label_frame = LabelFrame(self)
        label_frame.pack(fill=X)
        
        self.label_frame_1 = LabelFrame(label_frame)
        self.label_frame_1.pack(fill=X)
        
        self.button = Button(self.label_frame_1, text="清除", width=8, height=1, command=self.clear_info)
        self.button.pack(expand=0, side=RIGHT, anchor=SE)
        
        self.scrollbar_x = Scrollbar(self.label_frame_1, orient=HORIZONTAL)#水平滚动条
        self.scrollbar_y = Scrollbar(self.label_frame_1, orient=VERTICAL)#竖向滚动条
        self.text = Text(self.label_frame_1, height=20, yscrollcommand=self.scrollbar_y.set, xscrollcommand=self.scrollbar_x.set, wrap=None)#文本框
        #这里要加self，不然return_text函数会报错
        
        #滚动事件
        self.scrollbar_x.config(command=self.text.xview)
        self.scrollbar_y.config(command=self.text.yview)
        
        #布局
        self.scrollbar_x.pack(fill=X, side=BOTTOM, anchor=N)
        self.scrollbar_y.pack(fill=Y, side=RIGHT, anchor=N)
        self.text.pack(fill=X, expand=1, side=LEFT)

        #绑定事件
        self.text.bind('<Control-Key-a>', self.selectText)
        self.text.bind('<Control-Key-A>', self.selectText)
        
    def selectText(self, event):
        self.text.tag_add(SEL, '1.0', END)
        return 'break'
    
    def clear_info(self):
        self.text.delete('0.0', END)
        
    def show_info(self):
        insert_text = "windows ID:" + e1.get() + "\nMrFiona:" + e2.get() + "\nJohn Mei:" + e3.get() + "\nvegetables ID:" + e4.get() + "\n"
        self.text.insert(INSERT, insert_text)   #INSERT表示插入光标的当前位置    

#用类实现复选框Checkbutton调用，但是按钮的状态获取不了，有待解决  pack版本
class Choose_Items(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack()
        self.list_items()
        
        Label(self, text='Check demos', font=("黑体", 14)).pack()
        self.vars = []
        for key in demos:
            self.var = IntVar()
            Checkbutton(self, text=key, variable=self.var, command=demos[key]).pack(side=LEFT)
            self.vars.append(self.var)
        
    def report(self):
        for var in self.vars:
            print(var.get(), end=' ')
        print()
        
    def list_items(self):
        fram = Frame(self)  #设置这个组件是为了和复选按钮更在同一个显示框里合适的显示出来
        fram.pack(side=RIGHT) 
        Button(fram, text='State', command=self.report).pack()
        Button(fram, text='Quit', command=self.quit).pack()
        
#用类实现复选框Checkbutton调用，但是按钮的状态获取不了，有待解决  grid版本
class vvs(Toplevel):
    def __init__(self, parent=None):
        Toplevel.__init__(self, parent)
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
        for var in self.vars:
            print(var.get(), end=' ')
        print()
    
    def list_items(self):
        Button(self, text='State', command=self.report).grid(row=0, column=5)
        Button(self, text='Quit', command=self.quit).grid(row=1, column=5)
        
#用普通的函数实现复选输入组件Checkbutton，利用顶级窗口可以实现按钮状态的实时获取
def Go_World():
    
    def report():
            print([var.get() for var in vars])    
            
    def list_items():
        Button(gg, text='State', command=report).grid(row=0, column=5)
        Button(gg, text='Quit', command=gg.quit).grid(row=1, column=5)
    
    gg =Toplevel()
    Label(gg, text='Check demos', font=("黑体", 14)).grid(row=0, column=0, columnspan=5)
    vars = []
    i = 0
    for key in demos:
        var = IntVar() 
        Checkbutton(gg, text=key, variable=var, command=demos[key]).grid(row=1, column=i)
        i+=1
        vars.append(var)
    list_items()

def func2():
    pass

#创建顶级窗口Toplevel后，进一步调用其他按钮事件
def create_top(top):
    master = Tk()
    master.title('来到此地，即是缘分')
    master.geometry('400x300')
    label = Label(master, text='您已经进入另一个世界\n请点击按钮确认是否了解更多？', bg='white', fg='black')
    label.config(justify=LEFT,  font=("黑体", 12))
    label.pack(expand=YES)
    
    Button(master, text='了解', command=Go_World, font=("黑体", 12), fg='red').pack(side=LEFT, anchor=SW)
    Button(master, text='不了解', command=func2, font=("黑体", 12), fg='blue').pack(side=RIGHT, anchor=SE)
    
#     top.destroy()  #销毁
    mainloop()

#创建顶级窗口函数
def create_toplevel():
    top = Toplevel()
    top.title('Top Level of  window')
    label = Label(top, text='欢迎您进入顶层窗口，请点击下面的按钮')
    label.config(font=("黑体", 12))
    label.pack()
    
    button = Button(top, text='进入另一个世界', command=(lambda: create_top(top)))
    button.config(relief=RAISED, font=("黑体", 12), fg='red')
    button.pack()
    
#     top.grab_set()
#     top.focus_set()
#     top.wait_window()   #等待销毁

def print_i(value):
    for i in range(1,value):
        print('i:\t%s' %i)
        time.sleep(1)
        
#创建线程函数,解决GUI假死现象start
def create_threading():
    value = 100
    t1 = threading.Thread(target=print_i, args=(value,))
    t1.start()
#     t1.join()   #去掉该语句即可以解决GUI界面假死现象
#创建线程函数,解决GUI假死现象end

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
    if e20.get() == '' or e20.get().isdigit() == False:
        askokcancel(title="yes or not?", message="are you sure the data is correctly?")
        e20.delete(0, END)
        return False
    elif e20.get().isdigit() == True:
        return True

def choose():
    filename = filedialog.askopenfilename(initialdir="please choose topo：")
    e18.delete(0, END)
    e18.insert(0, filename)
    return filename 

def built_eip():
    print("这个函数是申请EIP用的")

def print_id():
    print(var.get())
    
root = Tk()
root.title("我的自定义GUI")
root.geometry("770x800")

Label(root, text="虚拟机镜像", font=("华康少女字体", 12)).grid(row=0, column=0, columnspan=2, padx=10, pady=5)
Label(root, text="规格", font=("华康少女字体", 12)).grid(row=0, column=2, columnspan=2, padx=10, pady=5)
Label(root, text="磁盘大小(g)", font=("华康少女字体", 12), ).grid(row=0, column=4, columnspan=2, padx=10, pady=5)

#虚拟机镜像
Label(root, text="Windows", font=("黑体", 12)).grid(row=1, column=0, sticky=E, padx=10, pady=5)
Label(root, text="FTP", font=("黑体", 12)).grid(row=2, column=0, sticky=E, padx=10, pady=5)
Label(root, text="OMU", font=("黑体", 12)).grid(row=3, column=0, sticky=E, padx=10, pady=5)
Label(root, text="VIU", font=("黑体", 12)).grid(row=4, column=0, sticky=E, padx=10, pady=5)
Label(root, text="Tester", font=("黑体", 12)).grid(row=5, column=0, sticky=E, padx=10, pady=5)
Label(root, text="环境名称前缀", font=("黑体", 12)).grid(row=6, column=0, sticky=E, padx=10, pady=5)
Button(root, text="开始", font=("黑体", 12)).grid(row=6, column=2)#, padx=10, pady=5)
Button(root, text="结束", font=("黑体", 12)).grid(row=6, column=4)#, padx=10, pady=5)

e1 = Entry(root, validate="focusout", validatecommand=warn_info1)
e2 = Entry(root, validate="focusout", validatecommand=warn_info2)
e3 = Entry(root)
e4 = Entry(root)
e5 = Entry(root)
e6 = Entry(root)

e1.grid(row=1, column=1)
e2.grid(row=2, column=1)
e3.grid(row=3, column=1)    
e4.grid(row=4, column=1)
e5.grid(row=5, column=1)
e6.grid(row=6, column=1)

#规格
e6 = Entry(root)
e7 = Entry(root)    
e8 = Entry(root)
e9 = Entry(root)
e10 = Entry(root)
e11 = Entry(root)

e6.grid(row=1, column=3)
e7.grid(row=2, column=3)
e8.grid(row=3, column=3)
e9.grid(row=4, column=3)
e10.grid(row=5, column=3)
e11.grid(row=6, column=3)

#磁盘大小(g)
e12 = Entry(root)
e13 = Entry(root)    
e14 = Entry(root)
e15 = Entry(root)
e16 = Entry(root)
e17 = Entry(root)

e12.grid(row=1, column=5)
e13.grid(row=2, column=5)
e14.grid(row=3, column=5)
e15.grid(row=4, column=5)
e16.grid(row=5, column=5)
e17.grid(row=6, column=5)

Button(root, text="选择TOPO", font=("黑体", 12), command=choose).grid(row=7, column=0, padx=10, pady=5)
e18 = Entry(root)
e18.grid(row=7, column=1) #选择topo输入框
v = StringVar() 
v.set("please choose suitable topo")
e18.insert(0, v.get())  #添加输入窗口内的默认内容

Label(root, text="VPCID", font=("黑体", 12)).grid(row=8, column=0, sticky=E, padx=10, pady=5)
Button(root, text="创建EIP", font=("黑体", 12), command=built_eip).grid(row=8, column=2, padx=10, pady=5)

e19 = Entry(root)
e20 = Entry(root, validate="focusout", validatecommand=warn_info17)

e19.grid(row=8, column=1)
e20.grid(row=8, column=3) #创建EIP输入

Label(root, text="可路由子网ID", font=("黑体", 12)).grid(row=9, column=0, sticky=E, padx=10, pady=5)
e21 = Entry(root)
e21.grid(row=9, column=1)


Label(root, text="用户工号", font=("黑体", 12)).grid(row=10, column=0, sticky=E, padx=10, pady=5)
Label(root, text="tenantId", font=("黑体", 12)).grid(row=11, column=0, sticky=E, padx=10, pady=5)
Label(root, text="akValue", font=("黑体", 12)).grid(row=12, column=0, sticky=E, padx=10, pady=5)
Label(root, text="使用人", font=("黑体", 12)).grid(row=13, column=0, sticky=E, padx=10, pady=5)
Label(root, text="使用人如果有多个使用','隔开,如IWX285351,wWX233781", font=("黑体", 12)).grid(row=13, column=2, columnspan=4)

e22 = Entry(root)
e23 = Entry(root)
e24 = Entry(root)
e25 = Entry(root)

e22.grid(row=10, column=1)
e23.grid(row=11, column=1)
e24.grid(row=12, column=1)
e25.grid(row=13, column=1)

#测试窗口颜色设置模块 start
def setcolor():
    (triple, hexstr) = askcolor()
    print(triple, hexstr)
    if hexstr:
        print(hexstr)
        button.config(fg=hexstr)

button = Button(root, text="我的颜色大小\n测试文字", command=setcolor, justify=LEFT) #justify能够使多行文本对齐
button.config(height=2, bg='white')   
button.config(font=('time', 10, 'bold'))
button.grid(row=10, column=2)
#测试窗口颜色设置模块 end


#将txt文件和bat文件互相转换 start
def change_filename(flag):
    filename = e18.get()
    Path, file1 = os.path.split(filename)#分隔为路径和文件名
    file, suffx = filename.split('.') #按照'.'分隔带有路径的文件名字符串
    print(file, suffx)
    if flag == 1:
        if suffx == 'txt':
            print('更改的文件路径为：', Path)
            print('更改的文件名为：', file1)
            os.replace(filename, file + '.' + 'bat')  #os.replace(str, dest)
            print('文件', file1, '已经被修改为', file + '.bat')
        elif suffx == '':
           print('未选择文件，请选择文件!')
        else:
            pass
    elif flag == 2:
        os.chdir(Path)
        os.replace(file + '.bat', file + '.txt')
        print('文件', file + '.bat', '已经被修改回', file + '.txt')
        
flag = 0
button2 = Button(root, text="更改文件名字", command=(lambda: change_filename(1)), justify=LEFT) #justify能够使多行文本对齐
button2.config(height=2, fg='red')   
button2.config(font=('time', 10, 'bold'))
button2.grid(row=10, column=3)

button3 = Button(root, text="反悔按钮", command=(lambda: change_filename(2)), justify=LEFT) #justify能够使多行文本对齐
button3.config(height=2, fg='red')   
button3.config(font=('time', 10, 'bold'))
button3.grid(row=10, column=4)
#将txt文件和bat文件互相转换 end


#测试顶层窗口Toplevel组件 start
button1 = Button(root, text='点击创建顶级窗口', font=("黑体", 12), command=create_toplevel)
button1.grid(row=12, column=2)
#测试顶层窗口Toplevel组件 end

#测试线程start
button22 = Button(root, text='线程测试', font=("黑体", 12), command=create_threading)
button22.grid(row=12, column=3)
#测试线程end

var = StringVar()
var.set("True")

main_frame = MainFrame(root)

Checkbutton(root, text="新创建一个VPC", variable=var, onvalue="True", offvalue="False", command=print_id, font=("黑体", 10)).grid(row=14, column=0, columnspan=2, sticky=W)#, padx=10, pady=5)
Button(root, text="检测", font=("黑体", 14)).grid(row=14, column=2, padx=10, pady=5)
Button(root, text="确定", command=main_frame.show_info, font=("黑体", 14)).grid(row=14, column=3, padx=10, pady=5)
Button(root, text="创建", font=("黑体", 14)).grid(row=14, column=4, padx=10, pady=5)
#Button(root, text="退出", font=("黑体", 14), command=root.quit).grid(row=14, column=5, padx=10, pady=5)

#新的方法设置退出按钮  start
quit = Quitter(root)
quit.button.config(text='退出',  font=("黑体", 14))
quit.grid(row=14, column=5, padx=10, pady=5)
#新的方法设置退出按钮  end

e26 = Entry(root)
e26.grid(row=14, column=1)

main_frame.grid(row=15, column=0, columnspan=6, sticky=N+S+E+W)

mainloop()
