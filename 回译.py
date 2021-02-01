#!/user/bin/env python
# coding=utf-8
"""
@file: 回译.py
@author: zwt
@time: 2021/2/1 16:22
@desc: 
"""

import http.client
import hashlib
import urllib
import random
import json


class BaiduFanyi():

    def __init__(self, toLang, query):
        self.appid = ''  # 填写你的appid
        self.secretKey = ''  # 填写你的密钥
        self.url = 'http://api.fanyi.baidu.com/api/trans/vip/translate'
        self.salt = random.randint(32768, 65536)
        self.q = query
        self.toLang = toLang
        self.fromLang = 'auto'
        self.generate()

    def generate(self):
        self.sign = self.appid + self.q + str(self.salt) + self.secretKey
        self.sign = hashlib.md5(self.sign.encode()).hexdigest()
        self.myurl = self.url + '?appid=' + self.appid + '&q=' + urllib.parse.quote(
            self.q) + '&from=' + self.fromLang + '&to=' + self.toLang + '&salt=' + str(
            self.salt) + '&sign=' + self.sign

    def execute(self):
        httpClient = None
        try:
            httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
            httpClient.request('GET', self.myurl)

            # response是HTTPResponse对象
            response = httpClient.getresponse()
            result_all = response.read().decode("utf-8")
            result = json.loads(result_all)

            return result['trans_result'][0]['src'], result['trans_result'][0]['dst']

        except Exception as e:
            print(e)
        finally:
            if httpClient:
                httpClient.close()


if __name__ == '__main__':
    demo = BaiduFanyi('en', '中国')
    src, dst = demo.execute()