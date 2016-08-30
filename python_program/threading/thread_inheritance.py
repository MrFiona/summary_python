'''
Created on 2016年8月30日

@author: apple
'''

#!/usr/bin/env python
#coding:utf-8

import threading
import time

exitFlag = 0

lock = threading.Lock()
# 使用 threading 模块创建线程
# 我们可以通过直接从 threading.Thread 继承创建一个新的子类，并实例化后调用 start() 方法启动新线程，即它调用了线程的 run() 方法：
class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print ("开始线程：" + self.name)
        print("%s acquire lock..." % threading.current_thread().getName())
        #获取锁，用于线程同步
        if lock.acquire():
            print("%s get lock..." % threading.current_thread().getName())
            print_time(self.name, self.counter, 5)
        #释放锁，开启下一个线程
        lock.release()
        print("%s release lock..." % threading.current_thread().getName())
        print ("退出线程：" + self.name)

def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print ("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1

# 创建新线程
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# 开启新线程
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print ("退出主线程")


# 线程模块
# Python3 通过两个标准库 _thread 和 threading 提供对线程的支持。
# _thread 提供了低级别的、原始的线程以及一个简单的锁，它相比于 threading 模块的功能还是比较有限的。
# threading 模块除了包含 _thread 模块中的所有方法外，还提供的其他方法：
# threading.currentThread(): 返回当前的线程变量。
# threading.enumerate(): 返回一个包含正在运行的线程的list。正在运行指线程启动后、结束前，不包括启动前和终止后的线程。
# threading.activeCount(): 返回正在运行的线程数量，与len(threading.enumerate())有相同的结果。
# 除了使用方法外，线程模块同样提供了Thread类来处理线程，Thread类提供了以下方法:
# run(): 用以表示线程活动的方法。
# start():启动线程活动。
# join([time]): 等待至线程中止。这阻塞调用线程直至线程的join() 方法被调用中止-正常退出或者抛出未处理的异常-或者是可选的超时发生。
# isAlive(): 返回线程是否活动的。
# getName(): 返回线程名。
# setName(): 设置线程名。


# 线程同步
# 如果多个线程共同对某个数据修改，则可能出现不可预料的结果，为了保证数据的正确性，需要对多个线程进行同步。
# 使用 Thread 对象的 Lock 和 Rlock 可以实现简单的线程同步，这两个对象都有 acquire 方法和 release 方法，对于那些需要每次只允许一个线程操作的数据，可以将其操作放到 acquire 和 release 方法之间。如下：
# 多线程的优势在于可以同时运行多个任务（至少感觉起来是这样）。但是当线程需要共享数据时，可能存在数据不同步的问题。
# 考虑这样一种情况：一个列表里所有元素都是0，线程"set"从后向前把所有元素改成1，而线程"print"负责从前往后读取列表并打印。
# 那么，可能线程"set"开始改的时候，线程"print"便来打印列表了，输出就成了一半0一半1，这就是数据的不同步。为了避免这种情况，引入了锁的概念。
# 锁有两种状态——锁定和未锁定。每当一个线程比如"set"要访问共享数据时，必须先获得锁定；如果已经有别的线程比如"print"获得锁定了，那么就让线程"set"暂停，也就是同步阻塞；等到线程"print"访问完毕，释放锁以后，再让线程"set"继续。
# 经过这样的处理，打印列表时要么全部输出0，要么全部输出1，不会再出现一半0一半1的尴尬场面。
# 实例：

#!/usr/bin/python3

# import threading
# import time
# 
# class myThread (threading.Thread):
#     def __init__(self, threadID, name, counter):
#         threading.Thread.__init__(self)
#         self.threadID = threadID
#         self.name = name
#         self.counter = counter
#     def run(self):
#         print ("开启线程： " + self.name)
#         # 获取锁，用于线程同步
#         threadLock.acquire()
#         print_time(self.name, self.counter, 3)
#         # 释放锁，开启下一个线程
#         threadLock.release()
# 
# def print_time(threadName, delay, counter):
#     while counter:
#         time.sleep(delay)
#         print ("%s: %s" % (threadName, time.ctime(time.time())))
#         counter -= 1
# 
# threadLock = threading.Lock()
# threads = []
# 
# # 创建新线程
# thread1 = myThread(1, "Thread-1", 1)
# thread2 = myThread(2, "Thread-2", 2)
# 
# # 开启新线程
# thread1.start()
# thread2.start()
# 
# # 添加线程到线程列表
# threads.append(thread1)
# threads.append(thread2)
# 
# # 等待所有线程完成
# for t in threads:
#     t.join()
# print ("退出主线程")

# 执行以上程序，输出结果为：
# 开启线程： Thread-1
# 开启线程： Thread-2
# Thread-1: Wed Apr  6 11:52:57 2016
# Thread-1: Wed Apr  6 11:52:58 2016
# Thread-1: Wed Apr  6 11:52:59 2016
# Thread-2: Wed Apr  6 11:53:01 2016
# Thread-2: Wed Apr  6 11:53:03 2016
# Thread-2: Wed Apr  6 11:53:05 2016
# 退出主线程