#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : Sedate

import sys, getopt
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
    def __init__(self, root_url, proxy_pool, threads):
        self.manager = url_manager.UrlManger()
        self.downloader = html_downloader.HtmlDownloader(proxy_pool)
        self.parser = html_parser.HtmlParser(urlparse.urlparse(root_url).hostname)
        self.outputer = html_outputer.HtmlOutputer()

        # self.proxy_pool = proxy_pool

        self.dir = dir_scan.DirScan(proxy_pool, self.manager.set_protocol(root_url))
        self.cms = cms_scan.CMSScan(proxy_pool)
        self.sqli = sqli_scan.SqliScan(proxy_pool)
        self.xss = xss_scan.XSSScan(proxy_pool)

        self.pool = ThreadPool(threads)

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
        if 'admin' in url.lower() or 'manage' in url.lower() or 'manager' in url.lower():
            print 'URL : %s' % url
            print 'Find admin\'s url :%s' % url

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


def usage():
    print 'Usage:python spider_main.py -f target.txt -t 50'
    print '-f --file    choose file'
    print '-t --threads threads defaults:30'
    print '-h --help    show usage'
    sys.exit(0)


def main():
    threads = 30

    if not len(sys.argv[1:]):
        usage()

    # read argv
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'ht:f:', ['help', 'thread=', 'file='])
    except getopt.GetoptError:
        usage()

    for o, a in opts:
        if o in ('-h', '--help'):
            usage()
        elif o in ('-t', '--thread'):
            try:
                threads = int(a)
            except:
                print 'type error'
                return
        elif o in ('-f', '--file'):
            dir = a
        else:
            usage()

    # get proxy pool
    proxy = proxy_pool.ProxyPool(threads)
    proxy.get_proxy_ip()
    if not len(proxy.true_ip):
        print '代理池为空'
    else:
        try:
            file = open(dir, 'rb')
            targets = file.readlines()
        except:
            print 'No such file or directory:%s' % dir
            return
        finally:
            file.close()
        for root_url in targets:
            # start spider
            obj_spider = SpiderMain(root_url, proxy.true_ip, threads)
            obj_spider.crawl(root_url)


if __name__ == '__main__':
    main()
