#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : Sedate

import urllib
import urlparse


class UrlManger(object):
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

        self.bool_type = (
            '.js', '.css', '.ico', '.jpg', '.png', '.swf', '.pdf', '.htm', '.html', '.shtml', '.jsp', '.jspx', '.java',
            '.jspy', '.do', '.action', '.asp', '.aspx', '.php', '.phpx'
        )

    '''
    # add start url
    '''

    def add_new_url(self, url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    '''
    # add response's urls
    '''

    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            if url not in self.old_urls:
                self.new_urls.add(url)

    '''
    # is new url
    '''

    def has_new_url(self):
        return len(self.new_urls) != 0

    '''
    # get url
    '''

    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url

    '''
    # remove url
    '''

    def remove_new_url(self, new_url):
        self.new_urls.remove(new_url)
        self.old_urls.add(new_url)

    '''
    # set http request
    '''

    def set_protocol(self, url):
        # if 'http' != url[0:4]:
        if not url.startswith('http://'):
            url = 'http://%s' % url
        return url

    '''
    # bool url
    '''

    def bool_url_type(self, url):
        if '#' in url:
            return None

        if urlparse.urlparse(url).path.count('/') < 2 and urlparse.urlparse(url).query == '':
            return None

        if (url[-3:] in self.bool_type or
                    url[-4:] in self.bool_type or
                    url[-5:] in self.bool_type or
                    url[-6:] in self.bool_type or
                    url[-7:] in self.bool_type):
            return None

        # http://www.test.com/test.jsp?id=1
        if '?' in url:
            # return self.eary_get_url(url,payload)
            return 1

        # http://www.test.com/test/id/1
        # 只简单过滤http://www.test.com/ http://www.test.com/test
        else:
            return 2
            # return self.route_get_url(url,payload)

    '''
    # http://www.test.com/test.jsp?id=1
    # http://www.test.com/test.jsp?id=1&type=1
    '''

    def eary_get_url(self, url, payload):
        u = url.split('&')
        payload_urls = []
        temp_url = ''

        for i in range(0, len(u)):
            for j in range(0, len(u)):
                if j == i:
                    temp_url = temp_url + '&' + u[j] + urllib.quote(payload)
                else:
                    temp_url = temp_url + '&' + u[j]
            payload_urls.append(temp_url[1:])
            temp_url = ''
        return payload_urls

    '''
    # http://www.test.com/id/1
    # http://www.test.com/test/id/1
    '''

    def route_get_url(self, url, payload):
        payload_urls = ['%s%s' % (url, urllib.quote(payload))]
        return payload_urls
