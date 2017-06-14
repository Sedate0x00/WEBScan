#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : Sedate

import re
import urlparse


class HtmlParser(object):
    def __init__(self, hostname=None):
        self.hostname = hostname

    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return

        new_urls = self._get_new_urls(page_url, html_cont)
        return new_urls

    '''
    # get response's urls
    '''

    def _get_new_urls(self, page_url, html_cont):
        # print self.hostname
        new_urls = set()
        links = re.findall(r"(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')", html_cont, re.I | re.S | re.M)

        for link in links:
            new_full_url = urlparse.urljoin(page_url, link)
            if self.hostname == urlparse.urlparse(new_full_url).hostname:
                new_urls.add(new_full_url)
        return new_urls

    '''
    # get response
    '''

    def _get_new_data(self, page_url):
        res_data = {}

        # url

        return res_data
