'''
Created on 2016年8月16日

@author: apple
'''

from urllib.request import *
import urllib.request
import re
import os
 
# url="http://tieba.baidu.com/p/2460150866"
# response = urllib.request.urlopen(url)
# html = response.read()
# resp = html.decode("utf-8")
# # print(resp)
#  
# reg = r'src="(.+?\.jpg)" pic_ext'
# imgre = re.compile(reg)
# imglist = re.findall(imgre, resp)
# print(imglist)
# 
# x = 0
# print(os.getcwd())
# os.chdir('..')
# print(os.getcwd())
# for imgurl in imglist:
#     urllib.request.urlretrieve(imgurl, r'C:\Users\apple\workspace\python_program\download_jpg\%s.jpg' %x)
#     x+=1

import requests as req
import re
import tkinter as tk
import threading

lock=threading.Lock()

Headers = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding':'gzip,deflate,sdch',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'Connection':'keep-alive',
    'Host':'image.baidu.com',
    'User-Agent':'Mozilla/5.0 (Windows NT 5.1)'
}

def getPicUrl():
    bd_url='http://image.baidu.com/search/flip'
    Param = {
        'tn':'baiduimage',
        'ie':'utf-8',
        'word':'壁纸',
        'pn':'0',
        'gsm':'500000064'
    }

    ssn= req.Session()
    ssn.headers=Headers
    rsp=ssn.get(bd_url,params = Param)
    rsp.encoding='utf-8'
    html=rsp.text
    pic_url = re.findall('"objURL":"([^"]*)",', html)
    return pic_url

def down_thd(pic_url,num):
    picPath='C:/Users/apple/Desktop/search_picture/pic%d.jpg'
    
    lock.acquire()
    screen2.insert(tk.INSERT,'正在下载第%d张:%s\n' % (num, pic_url))
    lock.release()
    
    headers=Headers
    headers['Host']=re.findall('://(.*?)/',pic_url)[0]
    try:
        rsp=req.get(pic_url,headers=headers) # 下载图片
    except:
        lock.acquire()
        screen2.insert(tk.INSERT,'%d 下载失败！\n'  % num)
        lock.release()
        return
        
    try:
        with open(picPath % num,'xb') as picf:
            picf.write(rsp.content) # 保存图片
    except:
        lock.acquire()
        screen2.insert(tk.INSERT,'%d 保存失败！\n'  % num)
        lock.release()
        return
        
    lock.acquire()
    screen2.insert(tk.INSERT,'%d完成\n'  % num)
    lock.release()
    return
    
def run():
    pic_url = getPicUrl()
    pic_url = pic_url[:10] # 只下10张，示范

    thds=[]
    for i in range(len(pic_url)):
        t=threading.Thread(target=down_thd, args=(pic_url[i],i))
        thds.append(t)
        
    for t in thds:
        t.start()        
    return

##import os
os.mkdir('C:/Users/apple/Desktop/search_picture')  ##这个文件夹就自己手动新建一个吧
root=tk.Tk()
screen2=tk.Text(root,height=25,width=110)
screen2.pack()

bot=tk.Button(root,text='开始下载',command = run)
bot.pack()
root.mainloop()
