#!/urs/bin/env python3
#coding:utf-8
import re
import os
import uuid
import threading
import queue
import time
import urllib.request

queue=queue.Queue()
class ThreadUrl(threading.Thread):
	def __init__(self,queue,path,houz):#默认路径和后缀
		threading.Thread.__init__(self)
		self.queue=queue
		self.path=path
		self.houz=houz
		
	def run(self):
		while True:
			url=self.queue.get()
			#try:
			urllib.request.urlretrieve(url,filename='{0}{1}{2}'.format(self.path,uuid.uuid4(),self.houz))
			#except:
				#pass
			self.queue.task_done()


def downloadd(txt1,path,houz):
	
	'''-----------------------------------------------------------------------------------------------------'''
	#读取文本文件中的url返回列表
	txt=open(txt1,'r')
	for line in txt.readlines():
		queue.put(line.strip('\n').strip())#将列表中的url放入队列中
	txt.close()
	'''-----------------------------------------------------------------------------------------------------'''
	
	'''
	# 1.普通下载
	start=time.time()
	for line in lines:
		try:
			urllib.request.urlretrieve(line.strip('\n').strip(),filename='%s%s%s'% (path='./pictures/',uuid.uuid4(),houz=".jpg"))
		except:
			pass
	print(time.time()-start)
	'''
	
	
	# 2.多线程下载
	start=time.time()
	for i in range(20):
		t=ThreadUrl(queue,path,houz)
		t.setDaemon(True)#守护进程#穿衣出门
		t.start()
	queue.join()
	print(time.time()-start)
	
#if __name__=="__main__":
	#downloadd(txt1="1.txt",path='./pictures/',houz='.jpg')


