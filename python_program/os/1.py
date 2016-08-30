'''
Created on 2016年8月24日

@author: apple
'''

#coding:utf-8
import os
import json

file = open('test.txt', 'w')
file.write(u'这个是测试的信息!')
file.close()
dict1 ={1:'python周末培训班',2:'咨询010-68165761 QQ：1465376564'}

print(dict1) 
# 这样输出的没有显示汉字，是显示汉字的其它编码

a = {"中国": 1, "china": 11, "北京天安门": 111}  
a_dumps = json.dumps(a, skipkeys=False, ensure_ascii=False, check_circular=True, allow_nan=True, cls=None, \
           indent=4, separators=(',',':'), default=None, sort_keys=None)
print(a_dumps)
print(type(a_dumps))
file = open('json.log', 'a+')
file.write(a_dumps)
file.close()
with open('json1.log', 'w') as f:
    json.dump(a, f)
with open('json1.log', 'r') as f:
    d= json.load(f)
    print(d)