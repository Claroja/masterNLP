# /usr/bin/env python
# coding=utf8

import http.client as httplib
import hashlib
import urllib.parse
import random
import json
class trans():
    def __init__(self,id,sk,fromLang,toLang):
        self.appKey = id
        self.secretKey = sk
        self.fromLang = fromLang
        self.toLang = toLang
        self.md5 = hashlib.md5()
    def trans(self,q):
        httpClient = None
        myurl = '/api'
        salt = random.randint(1, 65536)
        sign = self.appKey + q + str(salt) + self.secretKey
        self.md5.update(sign.encode("utf8"))
        sign = self.md5.hexdigest()
        myurl = myurl + '?appKey=' + self.appKey + '&q=' + urllib.parse.quote(q) + '&from=' + self.fromLang + '&to=' + self.toLang + '&salt=' + str(
            salt) + '&sign=' + sign
        httpClient = httplib.HTTPConnection('openapi.youdao.com')
        httpClient.request('GET', myurl)
        response = httpClient.getresponse()
        a= response.read()
        return json.loads(a,encoding='utf8')


id = ''
secretKey = ''
fromLang = 'zh-CHS'
toLang = 'EN'
q = '严禁与碱类、胺类、碱金属、易燃物或可燃物、食用化学品等混装混运。'
trans = trans(id=id,sk=secretKey,fromLang=fromLang,toLang=toLang)
trans.trans(q)