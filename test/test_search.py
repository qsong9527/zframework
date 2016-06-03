# -*- coding: utf-8 -*-

import unittest

from utils.api.request_helper import Req

class TestSearch(unittest.TestCase):

    def setUp(self):
        #1. 初始化req
        __aut_url = "https://api.douban.com/v2/movie/search"
        self.req = Req(__aut_url)

    def test_normal(self):
        ''''''
        #1. 配置参数
        self.req.add_param("q","zenist")
        #2. 发送请求并获取返回值
        resp = self.req.send()
        #3. 验证返回状态code
        assert resp.STATUS_CODE == 200, \
            "Page Status error, RET_STSTUS=%s" % resp.STATUS
        #4. 验证返回值内容
        assert resp.JSON_CONTENTS['count'] == 20, \
            "Defalut count not 20, is %s" % resp.JSON_CONTENTS['count']

    def test_normal2(self):
        ''''''
        #1. 配置参数
        self.req.add_param("q","")
        #2. 发送请求并获取返回值
        resp = self.req.send()
        #3. 验证返回状态code
        assert resp.STATUS_CODE == 200, \
            "Page Status error, RET_STSTUS=%s" % resp.STATUS
        #4. 验证返回值内容
        assert resp.JSON_CONTENTS['count'] == 20, \
            "Defalut count not 20, is %s" % resp.JSON_CONTENTS['count']