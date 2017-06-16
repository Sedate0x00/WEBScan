#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : Sedate

import re, requests, random
from threadpool import *


class ProxyPool(object):
    def __init__(self, threads):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:53.0) Gecko/20100101 Firefox/53.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Connection': 'keep-alive',
            'Accept-Encoding': 'gzip, deflate'
        }
        self.threads = threads
        self.true_ip = []

    def get_proxy_ip(self):
        proxy_list = []
        print '获取代理ip...\n'
        for i in range(3):
            r = requests.get('http://www.xicidaili.com/nn/%s' % str(i + 1), headers=self.headers, timeout=10)
            _html_count = r.content
            ip_list = re.findall(r'\d+\.\d+\.\d+\.\d+', _html_count)
            port_list = re.findall(r'<td>(\d+)</td>', _html_count)
            for i in range(len(ip_list)):
                proxy_list.append('%s:%s' % (ip_list[i], port_list[i]))

        print '已获取%sip\n' % len(proxy_list)
        print '测试ip可用性\n'
        pool = ThreadPool(self.threads)
        request = makeRequests(self.test_proxy_ip, proxy_list)
        [pool.putRequest(req) for req in request]
        pool.wait()
        print '可用ip : %d' % len(self.true_ip)
        print '%s\n' % self.true_ip

    def test_proxy_ip(self, proxy_ip):
        try:
            # print proxy_ip
            proxies = {'http': 'http://%s' % proxy_ip}
            r = requests.get(' http://www.cip.cc', headers=self.headers, timeout=3, proxies=proxies)
            print 'time:%s\n' % r.elapsed.seconds
            print re.findall(r'<pre>(.*?)</pre>', r.content, re.S)[0]
            self.true_ip.append(proxies)
        except Exception, e:
            pass

# ProxyPool().get_proxy_ip()
