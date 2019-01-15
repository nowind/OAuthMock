#!/usr/bin/python
# -*- coding: utf-8 -*-
import web,requests,yaml,json,random,time
from OAuthMock import OAuthMock
class WeiXinAuth(OAuthMock):
        def getResultForMethod(self,method):
                token=self._MockGetToken()
                if token.startswith('tel'):
                        return '__pass'
                return OAuthMock.getResultForMethod(self,method)
	def Mockaccess_token(self):
		token=self._MockGetToken()
		scope=['snsapi_base','snsapi_userinfo','snsapi_login'][random.randint(0,2)]
		return {'access_token':token+'_atoken','expires_in':self.expires_in,'refresh_token':token+'_rtoken','scope':scope,'unionid':token+'_uid'}
	def Mockrefresh_token(self):
		token=self._MockGetToken()
		retJson={'refresh_token':token+'_rtoken','access_token':token+'_atoken','expires_in':self.expires_in,'openid':token+'_openid'}
		return retJson
	def Mockuserinfo(self):#结构参看https://mp.weixin.qq.com/wiki/17/c0f37d5704f0b64713d5d2c37b468d75.html
		token=self._MockGetToken()
		retJson={
		'openid':token+'_opendid','nickname':'mock%s'%time.time(),
		'sex':'%d'%random.randint(0,2),'city':"北京",'province':'北京',
		'country':['CN','OTHER'][random.randint(0,1)],
		 "headimgurl":    "http://wx.qlogo.cn/mmopen/g3MonUZtNHkdmzicIlibx6iaFqAc56vxLSUfpb6n5WKSYVY0ChQKkiaJSgQ1dZuTOgvLLrhJbERQQ4eMsv84eavHiaiceqxibJxCfHe/46", 
		"privilege":[
			"chinaunicom"
	    ],
    	"unionid": token+'_uid'
		}
		return retJson
	def Mockauth(self):
		return { "errcode":0,"errmsg":"ok"}
