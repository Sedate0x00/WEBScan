#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : Sedate

import urlparse
from threadpool import *

from proxy import proxy_pool

from dir import dir_scan
from cms import cms_scan
from sqli import sqli_scan
from xss import xss_scan

from spider import url_manager, html_downloader, html_outputer, html_parser

'''
# spider start
'''


class SpiderMain(object):
    def __init__(self, hostname, proxy_pool):
        self.manager = url_manager.UrlManger()
        self.downloader = html_downloader.HtmlDownloader(proxy_pool)
        self.parser = html_parser.HtmlParser(urlparse.urlparse(hostname).hostname)
        self.outputer = html_outputer.HtmlOutputer()

        # self.proxy_pool = proxy_pool

        self.dir = dir_scan.DirScan(proxy_pool, self.manager.set_protocol(root_url))
        self.cms = cms_scan.CMSScan(proxy_pool)
        self.sqli = sqli_scan.SqliScan(proxy_pool)
        self.xss = xss_scan.XSSScan(proxy_pool)

        self.pool = ThreadPool(30)

    '''
    # spider
    '''
    # def crawl(self,root_url):
    #     root_url = self.manager.set_protocol(root_url)
    #     self.manager.add_new_url(root_url)
    #     hostname = urlparse.urlparse(root_url).hostname
    #     while self.manager.has_new_url(): #判断set里是否还有url
    #         try:
    #             new_url = self.manager.get_new_url() # 从set里pop获取并删除一个url
    #             print new_url
    #             self.sqli.error_sqli(new_url) # 对url进行测试
    #             html_count = self.downloader.download(new_url) # 请求这个url并获取响应
    #             new_urls = self.parser.parse(new_url,html_count,hostname) # 正则取响应页面里的url
    #             self.manager.add_new_urls(new_urls) # 把获取的url加入set里
    #             # self.outputer.collect_data(new_data)
    #         except:
    #             print 'crawl : failed'
    #
    #     # self.outputer.output_html()

    '''
    # spider
    '''

    def crawl(self, root_url):
        print 'pentest : %s' % root_url
        root_url = self.manager.set_protocol(root_url)
        self.cms.cms_scan(root_url)
        dirs = self.dir.read_dir()
        requests = makeRequests(self.dir.dir_buster, dirs)
        [self.pool.putRequest(req) for req in requests]
        self.pool.wait()
        self.manager.add_new_url(root_url)
        print '\nsqli xss 扫描'
        while self.manager.has_new_url():
            try:
                requests = makeRequests(self.request_url, self.manager.new_urls)
                [self.pool.putRequest(req) for req in requests]
                self.pool.wait()
            except:
                print 'crawl : failed'
        print '扫描结束\n'

        # self.outputer.output_html()

    '''
    # get url list
    '''

    def request_url(self, new_url):
        # new_urla = self.manager.get_new_url()
        self.manager.remove_new_url(new_url)
        self.pentest(new_url)
        html_count = self.downloader.download(new_url)
        new_urls = self.parser.parse(new_url, html_count)
        self.manager.add_new_urls(new_urls)

    '''
    # pentest
    '''

    def pentest(self, url):
        # if 'admin' in url.lower() or 'manage' in url.lower() or 'manager' in url.lower():
        #     print 'URL : %s' % url
        #     print 'Find admin\'s url :%s' % url

        bool = self.manager.bool_url_type(url)
        if bool == None:
            return

        # sqli
        self.sqli.error_sqli(url, bool)
        self.sqli.bool_sqli(url, bool)
        self.sqli.time_sqli(url, bool)

        # expression
        self.sqli.exp_inj(url, bool)

        # xss
        self.xss.reflex_xss(url, bool)

        # ......


if __name__ == '__main__':
    # get proxy pool
    proxy = proxy_pool.ProxyPool()
    proxy.get_proxy_ip()
    if len(proxy.true_ip) == 0:
        print '代理池为空'
    else:
        file = open('target.txt', 'rb')
        targets = file.readlines()
        for root_url in targets:
            # start spider
            obj_spider = SpiderMain(root_url, proxy.true_ip)
            obj_spider.crawl(root_url)
