#!/urs/bin/env python3
#coding:utf-8
import urllib.request
import os
import re
from random import choice
import time
import uuid


def bug(lists,parrent):
	'''
	html=urllib.request.urlopen('http://www.python.org').read().decode('utf-8')
	'''
	txt=open('1.txt','w')#以写的形式打开，会删除原先的内容
	
	#通过url获取页面源码，通过正则表达式获取图片地址,存入文件
	for url in lists:
		time.sleep(1)
		iplists=['211.138.121.38:80','211.142.236.137:9000','122.96.59.107:82','122.96.59.106:82']
		ip=choice(iplists)
		headers={
					 "GET":url,
					 #"HOST":"",
					 "Referer":"http://www.python.org/",
					 "User-Agent":"Mozilla/5.0",
				}
		req=urllib.request.Request(url)
		for key in headers:
			req.add_header(key,headers[key])
		
		proxy_handler = urllib.request.ProxyHandler({'http': 'http://'+ip})
		#proxy_auth_handler = urllib.request.ProxyBasicAuthHandler()
		#proxy_auth_handler.add_password('realm', 'host', 'username', 'password')
		opener = urllib.request.build_opener(proxy_handler)
		urllib.request.install_opener(opener)
	
		html=urllib.request.urlopen(req).read().decode('utf-8')

		prog = re.compile(parrent)
		ss = prog.findall(html)
		for sss in ss:
			txt.write(sss+"\n")
			#print(sss)
			'''
			#不直接下载，先将内容写到文件中
			urllib.request.urlretrieve(sss)
			'''
	txt.close()#关闭文件

def writetotxtt(parrent,url):
	#获取匹配的url写入文本
	#parrent=r'(?ui)src="(.*?\.jpg)"'
	i=0
	lists=[]#定义列表存放url
	while i<1:
		try:
			i=i+1
			#if i==1:
				#url=r'http://www.ivsky.com'
			#else:
				#url=r'http://www.ivsky.com'
			lists.append(url)#将所有url存入列表

		except:
			pass
	try:
		bug(lists,parrent)#调用方法bug.py的方法bug()
	except:
		pass
	
#if __name__=="__main__":
	#writetotxtt(parrent=r'(?ui)src="(.*?\.jpg)"',url=r'http://www.ivsky.com')	
