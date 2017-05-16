#!/usr/bin/env python
# -*- coding: utf-8 -*-
# User    : apple
# File    : os_exercise.py
# Author  : MrFiona 一枚程序员
# Time     : 2017-05-16 23:28

import os

# print dir(os)

variable_value_list = []
#可以取代操作系统特定的路径分隔符。windows下为 “\\”,Linux下为"/"
variable_value_list.append(os.sep)
#字符串给出当前平台使用的行终止符。例如，Windows使用'\r\n'，Linux使用'\n'而Mac使用'\r'。
variable_value_list.append(os.linesep)
#输出用于分割文件路径的字符串，系统使用此字符来分割搜索路径（像PATH），例如POSIX上':',Windows上的';'
variable_value_list.append(os.pathsep)
#alternate pathname separator (None or '/')
variable_value_list.append(os.altsep)
#extension separator ('.' or '/')
variable_value_list.append(os.extsep)
#default search path for executables
variable_value_list.append(os.defpath)
#a string representing the current directory ('.' or ':')
variable_value_list.append(os.curdir)
#a string representing the parent directory ('..' or '::')
variable_value_list.append(os.pardir)
print variable_value_list

variable_value_list_1 = []
#字符串指示你正在使用的平台。比如对于Windows，它是'nt'，而对于Linux/Unix用户，它是'posix'。
variable_value_list_1.append(os.name)
#one of the modules posixpath, or ntpath
variable_value_list_1.append(os.path)
#the file path of the null device ('/dev/null', etc.)
variable_value_list_1.append(os.devnull)
print variable_value_list_1

print 'os.getcwd():\t获取当前工作目录，即当前python脚本工作的目录路径\t', os.getcwd()
print 'os.chdir(path):\t改变当前脚本工作目录到指定目录下\t', os.chdir('.')
print 'os.mkdir(path):\t创建目录\t', os.mkdir(os.getcwd() + os.sep +'gg')
print 'os.removedirs(path):\t若目录为空，则删除，并递归到上一级目录，如若也为空，则删除，依此类推\t', os.removedirs(os.getcwd() + os.sep + 'gg')
print 'os.listdir(path):\t出指定目录下的所有文件和子目录，包括隐藏文件，但不包括.和..\t', os.listdir(os.getcwd())
f = open('test.txt', 'w')
f.close()
print 'os.rename(old, new):\t重命名文件/目录,如果new存在则替换出现错误\t', os.rename('test.txt', 'ggg')
print 'os.remove(path):\t删除一个文件\t', os.remove('ggg')
os.makedirs(os.getcwd() + os.sep + 'old_dir')
if os.path.exists('new_dir'):
    print 'os.rmdir(path):\t删除单级空目录，若目录不为空则无法删除，报错\t', os.rmdir(os.getcwd() + os.sep + 'new_dir')
print 'os.renames(old, new):\t重命名文件/目录,如果new存在则替换出现错误\t', os.renames('old_dir', 'new_dir')
if os.path.exists('new_dir'):
    os.rmdir(os.getcwd() + os.sep + 'new_dir')
print 'os.putenv(key, value):\t改变或者增加一个环境变量值\t', os.putenv('key', 'value')
print 'os.getenv(key, value):\t获取一个环境变量，如果没有返回None\t', os.getenv('TEMP')
print 'os.environ:\t获取环境变量值 os.environ[key]\t', os.environ['TEMP']
print 'os.environ:\t获取所有环境变量值\t', os.environ

# print os.environ


