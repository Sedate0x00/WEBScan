#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : Sedate

import urlparse
from spider import html_downloader


class DirScan(object):
    def __init__(self, proxy_pool=None, url=None):
        self.downloader = html_downloader.HtmlDownloader(proxy_pool)
        self.url = url

    def dir_buster(self, dir):
        if self.url != None:
            _payload_url = urlparse.urljoin(self.url.replace('\n', '').replace('\r', ''),
                                            dir.replace('\n', '').replace('\r', ''))
            resp_code = self.downloader.get_resp_code(_payload_url)
            if resp_code != None:
                print '发现敏感目录 : %s' % _payload_url

    def read_dir(self, dir='dir/data/dirlist.txt'):
        try:
            print '读取敏感目录文件\n'
            file = open(dir, 'rb')
            _dir_list = file.readlines()
            print '敏感目录扫描'
            return _dir_list
        except Exception, e:
            print e
            print 'dir read error'
            return None

# DirScan().read_dir()
