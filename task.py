#coding:utf-8
import writetotxt
import download
import time

writetotxt.writetotxtt(parrent=r'(?ui)data-src="(.*?\.png)"',url=r'http://octodex.github.com')	
time.sleep(1)
download.downloadd(txt1="1.txt",path='./pictures/',houz='.png')
