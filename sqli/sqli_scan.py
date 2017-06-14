#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : Sedate

import re
from sqli_payload import *
from spider import url_manager, html_downloader


class SqliScan(object):
    def __init__(self, proxy_pool=None):
        self.downloader = html_downloader.HtmlDownloader(proxy_pool)
        self.manager = url_manager.UrlManger()

    '''
    # error sqli
    '''

    def error_sqli(self, url, bool):
        for payload in SqliPayload.error_payload:
            if bool == 1:
                _payload_urls = self.manager.eary_get_url(url, payload)
            elif bool == 2:
                _payload_urls = self.manager.route_get_url(url, payload)

            if _payload_urls != None:
                for _payload_url in _payload_urls:
                    _html_count = self.downloader.download(_payload_url)

                    if _html_count != None:
                        for (dbms, regex) in ((dbms, regex) for dbms in SqliPayload.dbms_errors for regex in
                                              SqliPayload.dbms_errors[dbms]):
                            if (re.search(regex, _html_count)):
                                print 'URL : %s' % _payload_url
                                print 'Find %s Error Sqli\nPayload :%s\n' % (dbms, payload)
                                return

    '''
    # time sqli
    '''

    def time_sqli(self, url, bool):
        for payload in SqliPayload.sleep_payload:
            if bool == 1:
                _payload_urls = self.manager.eary_get_url(url, payload)
            elif bool == 2:
                _payload_urls = self.manager.route_get_url(url, payload)

            if _payload_urls != None:
                _basis_time = self.downloader.get_resp_time(url)
                for _payload_url in _payload_urls:
                    _payload_time = self.downloader.get_resp_time(_payload_url)

                    if _payload_time != None:
                        try:
                            if _payload_time - _basis_time >= 5:
                                print 'URL : %s' % _payload_url
                                print 'Find Time Sqli\nPayload :%s\n' % (payload)
                                return
                        except:
                            pass

    '''
    # bool sqli
    '''

    def bool_sqli(self, url, bool):
        for payload in SqliPayload.bool_payload:
            if bool == 1:
                _true_payload_urls = self.manager.eary_get_url(url, payload[1])
                _false_payload_urls = self.manager.eary_get_url(url, payload[0])
            elif bool == 2:
                _true_payload_urls = self.manager.route_get_url(url, payload[1])
                _false_payload_urls = self.manager.route_get_url(url, payload[0])

            if _true_payload_urls != None and _false_payload_urls != None and len(_true_payload_urls) == len(
                    _false_payload_urls):
                for i in range(len(_true_payload_urls)):
                    _true_count = self.downloader.download(_true_payload_urls[i])
                    _false_count = self.downloader.download(_false_payload_urls[i])
                    if _true_count != _false_count:
                        print 'URL : %s' % _false_payload_urls[i]
                        print 'Find Bool Sqli\nPayload :%s\n' % (payload[0])
                        return

    '''
    # exp_inj
    '''

    def exp_inj(self, url, bool):
        if bool == 1:
            _payload_urls = self.manager.eary_get_url(url, SqliPayload.exp_inj.keys()[0])
        elif bool == 2:
            _payload_urls = self.manager.eary_get_url(url, SqliPayload.exp_inj.keys()[0])

        if _payload_urls != None:
            for _payload_url in _payload_urls:
                _html_count = self.downloader.download(_payload_url)

                if _html_count != None:
                    if SqliPayload.exp_inj.values()[0] in _html_count:
                        print 'URL : %s' % _payload_url
                        print 'Find Expression Injection\nPayload :%s\n' % (SqliPayload.exp_inj.keys()[0])
                        return
