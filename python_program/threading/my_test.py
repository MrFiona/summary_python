'''
Created on 2016年8月28日

@author: apple
'''

# encoding: UTF-8
import threading
import time
import datetime
 
data = 0
lock = threading.Lock()
# 方法1：将要执行的方法作为参数传给Thread的构造方法
def func1():
    t1 = datetime.datetime.now()
    print("this is %s use data process!" % threading.current_thread().getName())
    global data
    print(" %s acquire lock ...." % threading.current_thread().getName())
    
    if lock.acquire():
        print(" %s get lock ...." % threading.current_thread().getName())
        for i in range(5):
            data += i
            
        lock.release()
        print(" %s release lock ...." % threading.current_thread().getName())
        
    t2 = datetime.datetime.now()
    print(t2-t1)

def func2():
    print("this is  %s print process!" % threading.current_thread().getName())
    global data
#     time.sleep(3)
    print("data: %d" % data)

# t1 = threading.Thread(target=func1)
# t2 = threading.Thread(target=func2)
# t1.start()
# t2.start()
# t1.join()
# t2.join()
 
# # 方法2：从Thread继承，并重写run()
# class MyThread(threading.Thread):
#     def run(self):
#         print ('MyThread extended from Thread')
#   
# t = MyThread()
# t.start()


rlock = threading.RLock()

def func():
    # 第一次请求锁定
    print ('%s acquire lock...' % threading.currentThread().getName())
    if rlock.acquire():
        print ('%s get the lock.' % threading.currentThread().getName())
        time.sleep(2)

        # 第二次请求锁定
        print ('%s acquire lock again...' % threading.currentThread().getName())
        if rlock.acquire():
            print ('%s get the lock.' % threading.currentThread().getName())
            time.sleep(2)

        # 第一次释放锁
        print ('%s release lock...' % threading.currentThread().getName())
        rlock.release()
        time.sleep(2)

        # 第二次释放锁
        print ('%s release lock...' % threading.currentThread().getName())
        rlock.release()

t1 = threading.Thread(target=func)
t2 = threading.Thread(target=func)
t3 = threading.Thread(target=func)
t1.start()
t2.start()
t3.start()
