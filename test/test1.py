#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : Sedate

import re
import urlparse
import time
import threading
from threadpool import *
import requests
from sqli.sqli_payload import *
from cms.cms_list import *

# a = "http://www.baidu.com/main"
# b = "/index.jsp?id=1"

# a1 = urlparse.urljoin(a,b)
# print a1
#
# print urlparse.urlparse(a).hostname

# def aa(a):
#     if len(a) != 0:
#         print a.pa()
#
# test = {'a','b','c','d','e','f','g'}
# t = []
# [t.append(i) for i in test]
# print t
# threads = []
start = time.time()


# pool = ThreadPool(10)
# requests = makeRequests(aa,test)
# [pool.putRequest(req) for req in requests]
# pool.wait()


# for i in range(10):
#     t = threading.Thread(target=aa,args=(test,))
#     threads.append(t)
#
# for i in range(len(threads)):
#     threads[i].start()
# for i in range(len(threads)):
#     threads[i].join()
# r = requests.get('http://192.168.1.108/sqltest.php?id=1')
# a =  r.elapsed.seconds
# for i in SqliPayload.sleep_payload:
#     url = 'http://192.168.1.108/sqltest.php?id=1%s' % i
#     r = requests.get(url)
#     b = r.elapsed.seconds
#     print url
#     print b
#     print a
#     if b - a >= 5:
#         print 'find time sqli'
#         # break
#     else:
#         print 'lol'

# url = 'http://192.168.1.108/sqltest.php?id=1'
# r = requests.get(url)
# a = r.content
# r1 = requests.get(url)
# b = r1.content
# if a is b:
#     print 1
# if a == b:
#     print 2

# print r.content
# print r.headers['Content-type']
# print r.headers['Server']
# if 'X-Powered-By' not in r.headers:
#     print 1
# # print r.headers['X-Powered-By']
# a = 'http://www.aa.com/a.html'
# print a[-4:]

# url = 'http://www.test.com?id=1&aa=2&cc=3&css=4'
# surl=""
# for i in xrange(len(url)):
#     if i > url.find('?'):
#         surl+=surl.join(url[i]).replace(' ',"%20")
#     else:
#         surl+=surl.join(url[i])
# print surl

# url1 = 'http://www.badu.com/f.php'
# if urlparse.urlparse(url1).query == '':
#     print 1


# _html_count = "fdsafasdfsadfsdf  MySQL Error fasdfasdfsadfsadfsadf"
# for (dbms, regex) in ((dbms, regex) for dbms in SqliPayload.dbms_errors for regex in SqliPayload.dbms_errors[dbms]):
#     if (re.search(regex, _html_count)):
#         print 1


# def urlsplit(url):
#     domain = url.split("?")[0]
#     _url = url.split("?")[-1]
#     pararm = {}
#     for val in _url.split("&"):
#         pararm[val.split("=")[0]] = val.split("=")[-1]
#
#     #combine
#     urls = []
#     for val in pararm.values():
#         new_url = domain + _url.replace(val,"my_Payload")
#         urls.append(new_url)
#     return urls
# print urlsplit('http://www.baidu.com/index.php?id=1&a=1&c=1')
# dict = {'Alice': '2341'}
# print dict
# print SqliPayload.exp_inj

# url = input('输入要识别的网址')
# if url.startswith('http://'):
#     url = url
# else:
#     url = 'http://'+url
# headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.0.1471.914 Safari/537.36'}
# response = requests.get(url=url,headers=headers)
# bresponse = BeautifulSoup(response.text,"lxml")
# title = bresponse.findAll('title') #titlefor i in title:
#
# title = i.get_text()
# head = response.headers
# response = response.text
# header = ''
# for key in head.keys(): #将 header集合
#     header = header+key+':'+head[key]
#     print('收集主页信息完毕')

# url1 = 'http://www.wacai.com/intro/aboutus.jsp'
# url2 = 'http://www.wacai.com/'
# r1 = requests.get(url1)
# r2 = requests.get(url2)
# c = r1.elapsed.microseconds
# d = r2.elapsed.microseconds
# print c
# print d
# print c - d

# url1 = 'http://192.168.1.139/eadmin'
# r1 = requests.get(url1)
# # list = {'phpcmd-tpe':'phpcms','eadminsdfs':'eadmin','dfededed':'dede','phpmyadmindsf':'phpmyamdin','wordsf':'wordpress'}
# con = r1.content
# def ttt(i):
#     pass
# pool = ThreadPool(15)
# requests = makeRequests(ttt,CMSList.cms_list.keys())
# [pool.putRequest(req) for req in requests]
# pool.wait()

#
# a = 'http://192.168.1.139/eadmin'
# b = '/back.rar'
# print urlparse.urlparse(a)
# print urlparse.urljoin(a,b)
def abc(a):
    b = a
file = open('target.txt', 'rb')
targets = file.readlines()
for root_url in targets:
    abc(root_url)

end = time.time()
print end-start
