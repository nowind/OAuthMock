#!/usr/bin/python
# -*- coding: utf-8 -*-
import web,requests,yaml,sys,random,json,os

class OAuthMock:
    def _getUidHash(self):
        return hash(self._MockGetToken())%sys.maxsize
    def isPost(self):
        return web.ctx.method=='POST'
    def init(self):
        self.expires_in=3600*random.randint(1,4)
        self.webIunpt=web.input()
        self.charset='utf-8'
    def setCharset(self,charset):
        self.charset=charset
    def simpleBypass(self):
        fullurl=web.ctx.homedomain.replace('http://','https://')+web.ctx.homepath+web.ctx.fullpath
        headers={}
        AuthHeader=web.ctx.env.get('HTTP_AUTHORIZATION')
        if AuthHeader:
            headers['Authorization']=AuthHeader
        try:
            if self.isPost():
                headers['Content-Type']='application/x-www-form-urlencoded'
                proxyResponse=requests.post(fullurl,web.data(),stream=True,headers=headers)
            else:
                proxyResponse=requests.get(fullurl,stream=True,headers=headers)
            willReturn=proxyResponse.text
            if proxyResponse.encoding and proxyResponse.encoding!='':
                print 'find encoding:'+proxyResponse.encoding
                willReturn=willReturn.encode(proxyResponse.encoding)
            return willReturn
        except Exception,e:
            print e
        return ''
    def _GetInputByOrder(self,orderlist):
        for i in orderlist:
            if i in self.webIunpt:
                return self._earseEnds(self.webIunpt[i])
        return ''
    def _earseEnds(self,method):
        if method.endswith('_atoken') or method.endswith('_rtoken') or method.endswith('_openid'):
            method=method[0:-7]
        elif method.endswith('_uid'):
            method=method[0:-4]
        return method
    def _MockGetToken(self):
        r= self._GetInputByOrder(['code','access_token','refresh_token','openid','uid'])
        return r
    def getSelfClassName(self):
        return self.__class__.__name__
    def verifyMethodInPattern(self,method,pattern):
        methods=set(pattern.split(','))
        method=self._earseEnds(method)
        if '*' in methods:
            return True
        if method in methods:
            return True
        return False
    def getResultForMethod(self,method):
        method=method.split('.')[0]
        try:
            with open('oauth.yaml') as f:
                authDataStore=yaml.load(f)
                className=self.getSelfClassName()
                if className in authDataStore: #第一层是类名
                    oauthMap=authDataStore[className]
                    token=self._MockGetToken()
                    if token in oauthMap: 
                        if ('hook' in oauthMap[token]) and self.verifyMethodInPattern(method,oauthMap[token]['hook']):
                            if method in oauthMap[token]:
                                ret=oauthMap[token][method]
                            elif '*' in oauthMap[token]:
                                ret=oauthMap[token]['*']
                            else:
                                ret=''
                            return ret
                        elif ('mock' in oauthMap[token]) and self.verifyMethodInPattern(method,oauthMap[token]['mock']):
                            return '__pass'
        except Exception,e:
            print e
        return None
    def sendResult(self,method):
        try:
            print method
            MockOrHook=self.getResultForMethod(method)
            if self.isPost():
                print 'postdata:'
                print web.data()
            if MockOrHook=='__pass':
                if hasattr(self,'Mock%s'%method):#没有的话也pass
                    result= getattr(self,'Mock%s'%method)()
                    if type(result)==type('') or type(result)==type(u''):
                        return result
                    else:
                        return json.dumps(result,ensure_ascii=False)
            elif  MockOrHook != None:
                return MockOrHook
            return self.simpleBypass()
        except Exception,e:
            print e
            return ''
    def run(self): 
        self.pathSplit=web.ctx.path.split('/')
        method=(self.pathSplit[-1].split('.'))[0]
        web.header('Content-type','text/plain;charset='+self.charset, unique=True)
        return self.sendResult(method)

