'''
Created on 2016年8月18日

@author: apple
'''
#-*- coding:utf-8 -*-

#开发出一个日志系统，既要把日志输出到控制台，还要写入日志文件

import logging
import time
import os
import os.path

class Logger():
    def __init__(self, log_name, logger_name):
        
        '''
                指定保存日志的文件路径，日志级别以及调用文件
                将日志    存入到指定的文件中
    
        '''
        #设置日志文件名称：time.time()取得当前时间；time.localtime()取得本地时间；time.strftime()格式化日期；
        time_str = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime(time.time()))
        logname = time_str + '_' + log_name + '.log'
        
        #设置日志文件所在的路径
        log_filedir = 'Log'
        if not os.path.isdir(log_filedir):
            print("日志文件夹 %s 不存在，开始创建此文件夹" %log_filedir)
            os.mkdir('Log')
        else:
            print("日志文件夹 %s 存在" %log_filedir)
        
        os.chdir('Log')
        
        #创建一个logger以及设置日志级别
        #logging有6个日志级别:NOTSET, DEBUG, INFO, WARNING, ERROR, CRITICAL对应的值分别为：0,10,20,30,40,50
        #例如:logging.DEBUG和10是等价的表示方法
        #可以给日志对象(Logger Instance)设置日志级别，低于该级别的日志消息将会被忽略，也可以给Hanlder设置日志级别
        #对于低于该级别的日志消息, Handler也会忽略。
        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(logging.DEBUG)
        
        #创建文件handler，用于写入日志文件并设置文件日志级别
        file_handler = logging.FileHandler(logname)
        file_handler.setLevel(logging.DEBUG)
        
        #创建控制端输出handler，用于输出到控制端兵设置输出日志级别
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)
        
        #定义handler的输出格式并将格式应用到handler
        formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)
        
        #将handler加入到logger
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)
        
        self.logger.debug("这个是debug日志信息")
        self.logger.info("欢迎大家来到 Python的世界")
        
        
        #将handler从logger中移除
        self.logger.removeHandler(file_handler)
        self.logger.removeHandler(console_handler)

if __name__ == '__main__':       
    print(os.getcwd())
    Log = Logger('create_log', "logger的名字")
        


# 模块级函数
# 
# logging.getLogger([name]):返回一个logger对象，如果没有指定名字将返回root logger
# logging.debug()、logging.info()、logging.warning()、logging.error()、logging.critical()：设定root logger的日志级别
# logging.basicConfig():用默认Formatter为日志系统建立一个StreamHandler，设置基础配置并加到root logger中
# 
# Loggers
# 
# Logger.setLevel(lel):指定最低的日志级别，低于lel的级别将被忽略。debug是最低的内置级别，critical为最高
# Logger.addFilter(filt)、Logger.removeFilter(filt):添加或删除指定的filter
# Logger.addHandler(hdlr)、Logger.removeHandler(hdlr)：增加或删除指定的handler
# Logger.debug()、Logger.info()、Logger.warning()、Logger.error()、Logger.critical()：可以设置的日志级别

# Handlers
# 
# handler对象负责发送相关的信息到指定目的地。可以通过addHandler()方法添加多个多handler
# Handler.setLevel(lel):指定被处理的信息级别，低于lel级别的信息将被忽略
# Handler.setFormatter()：给这个handler选择一个格式
# Handler.addFilter(filt)、Handler.removeFilter(filt)：新增或删除一个filter对象

# Formatters
# 
# Formatter对象设置日志信息最后的规则、结构和内容，默认的时间格式为%Y-%m-%d %H:%M:%S，下面是Formatter常用的一些信息


# %(name)s                       Logger的名字
#  
# %(levelno)s                    数字形式的日志级别
#  
# %(levelname)s                文本形式的日志级别
#  
# %(pathname)s                调用日志输出函数的模块的完整路径名，可能没有
# 
# %(filename)s                  调用日志输出函数的模块的文件名
#  
# %(module)s                    调用日志输出函数的模块名
#  
# %(funcName)s                调用日志输出函数的函数名
#  
# %(lineno)d                     调用日志输出函数的语句所在的代码行
#  
# %(created)f                    当前时间，用UNIX标准的表示时间的浮 点数表示
#  
# %(relativeCreated)d        输出日志信息时的，自Logger创建以 来的毫秒数
#  
# %(asctime)s                  字符串形式的当前时间。默认格式是 “2003-07-08 16:49:45,896”。逗号后面的是毫秒
# 
# %(thread)d                   线程ID。可能没有
# 
# %(threadName)s           线程名。可能没有
# 
# %(process)d                 进程ID。可能没有
#  
# %(message)s               用户输出的消息




        
        
        