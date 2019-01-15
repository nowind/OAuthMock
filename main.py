#!/usr/bin/python
# -*- coding: utf-8 -*-  


import sys
default_encoding = 'utf-8' 
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)
import web
import json,re
import os
import yaml
import QQAuth,RenRenAuth,WeiBoAuth,WeiXinAuth,OAuthMock
import requests

urls = (
    '/(.*)', 'Index',
)
hostMap={
    'graph.qq.com':QQAuth.QQAuth(),
    'graph.renren.com':RenRenAuth.RenRenAuth(),
    'api.weibo.com':WeiBoAuth.WeiBoAuth(),
    'api.weixin.qq.com':WeiXinAuth.WeiXinAuth()
}

app = web.application(urls, globals())

class Index:
    def POST(self,urlpath=''):
        host=web.ctx.host.split(':')[0]
        if host in hostMap:
            hostMap[host].init()
            return hostMap[host].run()
        other=OAuthMock.OAuthMock()
        return other.simpleBypass()
    def GET(self,urlpath=''):
        return self.POST()

if __name__ == "__main__":
    app.run()
