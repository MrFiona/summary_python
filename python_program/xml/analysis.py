'''
Created on 2016年8月18日

@author: apple
'''
#-*-coding:utf-8-*-

import sys
import os
import xml.dom.minidom

#获取name节点对象
def get_xmlnode(node, name):
    return node.getElementsByTagName(name) if node else []    

#获取标签属性值
def get_attrvalue(node, attrname):
    if node != None:
        print('dd', node.nodeName, node.nodeValue)
        #排除没有passwd标签属性或者passwd便签属性值为空的情况
        if node.getAttribute(attrname) == '':
            return '222'
        if node.getAttribute(attrname) == ' ':
            return '111'
        return node.getAttribute(attrname)

#获取标签对之间的数据,对于文本节点，data和nodeValue是等价的
def get_nodevalue(node, index=0):
    return node.childNodes[index].data if node else ' '

#获取标签对之间的数据等价版
def get_nodevalue1(node):
    return node.firstChild.nodeValue if node else ' ' 

#获取xml文档
dom = xml.dom.minidom.parse(r"C:\Users\apple\workspace\python_program\xml\del.xml")
# print(dom.toxml('UTF-8'))
# print(dom.toxml())
#获取xml文档对象
root = dom.documentElement

user_nodes = get_xmlnode(root, 'user') #返回子节点列表

#测试start
itemlist = root.getElementsByTagName('user')
item1= itemlist[0]
item2 = itemlist[1]
# print(item1.getAttribute('id'), item1.getAttribute('passwd'))
# print(item2.getAttribute('id'))

print(root.tagName)
print(root.parentNode.nodeName)
print(root.localName)
user_sex_list = root.getElementsByTagName('sex')
print(user_sex_list.length)  #含有节点的个数

#这里确定要选择哪个节点
user_sex = user_sex_list[5]   #del.xml文档共有6个sex节点 0-5，值超过就会报错
# print(user_sex.lastChild.data) 
# print(user_sex.firstChild.data)
# print(user_sex.childNodes[0].nodeValue)
# print(user_sex.nodeValue, user_sex.nodeType, user_sex.nodeName)
#测试end

print("user_nodes:\t", user_nodes)
# print('fff', user_nodes[0].childNodes)
# print(user_nodes[0].lastChild.nodeType, user_nodes[0].firstChild.nodeType)

user_list = []
#元素节点的 attributes 属性返回属性节点的列表, x.length 等于属性的数量，可使用 x.getNamedItem() 返回属性节点
x = user_nodes[0].attributes
print(x.getNamedItem('passwd').nodeValue, '', x.length) 

for node in user_nodes:
    user_id = get_attrvalue(node, 'id')
    
    #测试1 start
#     user_id1 = get_attrvalue(None, 'id')
#     print(user_id1)
    #测试1 end
    user_passwd = get_attrvalue(node, 'passwd')
    node_username = get_xmlnode(node, 'username')
    
#     for node1 in node_username[0].childNodes:
#         print("::", node1.data)
    
    node_email = get_xmlnode(node, 'email')
#     print(node_email[0].childNodes[0].nodeValue) #获取元素节点的文本节点的值
   
    node_age = get_xmlnode(node, 'age')
    node_sex = get_xmlnode(node, 'sex')
    
#     if node_username[0].parentNode.tagName == 'user':
#         print("yes")                          #或者nodeValue等价
    
    user_username = get_nodevalue1(node_username[0])
    user_email = get_nodevalue(node_email[0])
    user_age = get_nodevalue(node_age[0])
    user_sex = get_nodevalue(node_sex[0])
    
    user = {}
    user[ 'id' ], user[ 'passwd' ], user[ 'username' ], user[ 'email' ], user[ 'age' ], user[ 'sex' ] = \
    int(user_id), int(user_passwd), user_username, user_email, user_age, user_sex
    
    user_list.append(user)
    
for user in user_list:
    print('-------------------------------------------------------------------------------------')
    if user:
        user_str = 'No:\t%15d\npasswd:\t%d\nname:\t%s\nemail:\t%s\nage:\t%10s\nsex:\t%12s' % (int(user[ 'id' ]), int(user[ 'passwd' ]), \
                                                                           user[ 'username' ], user[ 'email' ], user[ 'age' ], user[ 'sex' ])
        print(user_str)
         
         
# xml有如下特征：
# 
# 它是有标签对组成，<aa></aa>
# 标签可以有属性：<aa id='123'></aa>
# 标签对可以嵌入数据：<aa>abc</aa>
# 标签可以嵌入子标签（具有层级关系）

# minidom.parse(filename)
# 加载读取XML文件
#
# minidom.parseString(xmlstr)
# 加载读取XML字符串

# doc.documentElement
# 获取XML文档对象
#  
# node.getAttribute(AttributeName)
# 获取XML节点属性值
#  
# node.getElementsByTagName(TagName)
# 获取XML节点对象集合
#  
# node.childNodes #返回子节点列表。
#  
# node.childNodes[index].nodeValue
# 获取XML节点值
#  
# node.firstChild
# #访问第一个节点。等价于pagexml.childNodes[0]
#  
# doc = minidom.parse(filename)
# doc.toxml('UTF-8')
# 返回Node节点的xml表示的文本
#  
# Node.attributes["id"]
# a.name #就是上面的 "id"
# a.value #属性的值
# 访问元素属性

# 元素类型    节点类型
# 元素                1
# 属性                2
# 文本                3
# 注释                8
# 文档                9
#     