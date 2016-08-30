'''
Created on 2016年8月10日

@author: apple
'''
#coding: utf-8
import xml.dom.minidom
import os
import subprocess  

print('del.xml文件内容如下:')
file = open('del.xml', 'r')
lines = file.readlines()
for line in lines:
    print(line, end=' ')
file.close()
print('\n')

# value = os.system('cat del.xml')
# if value == False:
#     return

dom = xml.dom.minidom.parse("del.xml")  #打开xml文档

root = dom.documentElement              #得到xml文档对象
print ("nodeName:", root.nodeName)        #每一个结点都有它的nodeName，nodeValue，nodeType属性
print ("nodeValue:", root.nodeValue)      #nodeValue是结点的值，只对文本结点有效
print ("nodeType:", root.nodeType)
print ("ELEMENT_NODE:", root.ELEMENT_NODE)

root = dom.documentElement
son_root = root.getElementsByTagName('maxid')
son = son_root[0]
# son2 = son_root[1]
print('ss:', son.getAttribute('maxid'))
print(son.firstChild.data)
# print(son2.firstChild.data)
print(son.nodeName)
print(son.nodeValue)

itemlist = root.getElementsByTagName('item')
item = itemlist[0]
print(item.getAttribute('id'))
print(item.childNodes[0].nodeValue)

item2 = itemlist[1]
print(item2.getAttribute('id'))


# cmd = 'cmd.exe c:\Users\apple\Desktop\ww.bat'  
# p = subprocess.Popen("cmd.exe /c" + "c:\\Users\\apple\\Desktop\\ww.bat  abc", stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
#    
# curline = p.stdout.readline()  
# while(curline != b''):  
#     print(curline)  
#     curline = p.stdout.readline()  
#         
# p.wait()  
# print(p.returncode)


cmd = 'cmd.exe c:\\sam.bat'  
p = subprocess.Popen("cmd.exe /c" + "c:\\Users\\apple\\Desktop\\ww.bat abc", stdout=subprocess.PIPE, stderr=subprocess.STDOUT)    
   
   
byte_data = p.stdout.read(1)      
   
word_data = b''                   
while(byte_data != b''):  
    word_data += byte_data  
    try:  
        showdata = word_data.decode('gb2312')   
   
        print(showdata, end="", flush=True)   
        word_data = b''  
    except Exception as e:  
        #print(e)  
        a=0  
    byte_data = p.stdout.read(1)  
       
p.wait()      
print(p.returncode)  

 

