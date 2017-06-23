#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : Sedate

from xss_payload import *
from spider import url_manager,html_downloader

class XSSScan(object):
    def __init__(self,proxy_pool):
        self.downloader = html_downloader.HtmlDownloader(proxy_pool)
        self.manager = url_manager.UrlManger()

    def reflex_xss(self,url,bool):
        for payload in XSSPayload.xss_payload:
            if bool == 1:
                _payload_urls = self.manager.eary_get_url(url,payload)
            elif bool == 2:
                _payload_urls = self.manager.route_get_url(url, payload)

            if _payload_urls:
                for _payload_url in _payload_urls:
                    _html_count = self.downloader.download(_payload_url)

                    if _html_count:
                        if payload in _html_count:
                            print 'URL : %s' % _payload_url
                            print 'Find XSS\nPayload :%s\n' % (payload)
                            return