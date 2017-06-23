#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : Sedate

from cms_list import *
from spider import url_manager, html_downloader


class CMSScan(object):
    def __init__(self, proxy_pool=None):
        self.downloader = html_downloader.HtmlDownloader(proxy_pool)

    '''
    # fingerprint identification
    '''

    def cms_scan(self, url):
        _html_count = self.downloader.download(url)
        if _html_count:
            for i in CMSList.cms_list.keys():
                if i in _html_count:
                    print '指纹识别结果:%s\n' % CMSList.cms_list[i]
                    return
        print '未识别出CMS\n'
