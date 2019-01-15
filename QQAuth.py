#!/usr/bin/python
# -*- coding: utf-8 -*-
import web,requests,yaml,json,random,time
from OAuthMock import OAuthMock
class QQAuth(OAuthMock):
	def Mocktoken(self):
		token=self._MockGetToken()
		return 'access_token=%s&expires_in=3600000&refresh_token=%s'%(token+'_atoken',token+'_rtoken')
	def Mockme(self):
		retJson={'client_id':'MockQQ','openid':self._MockGetToken()+'_openid',"unionid":self._MockGetToken()+'_uid'}
		return 'callback(%s);'%json.dumps(retJson)
	def Mockget_user_info(self):#结构参看http://connect.qq.com/sdk/webtools/index.html#get_user_info
		retJson={
		'ret':0,'msg':'','gender':['男','女'][random.randint(0,1)],
		'is_yellow_vip':'%d'%random.randint(0,1),'vip':'%d'%random.randint(0,1),
		'yellow_vip_level':'%d'%random.randint(0,7),'level':'%d'%random.randint(0,7),
		'is_yellow_year_vip':'%d'%random.randint(0,1),'city':"北京",'year':'1854','is_lost':0,
		'province':'北京','nickname':'mock%s'%time.time(),
		'figureurl':'http://qzapp.qlogo.cn/qzapp/100330589/397448B23EFB11D0F697386D44E1916C/30',
		'figureurl_1':'http://qzapp.qlogo.cn/qzapp/100330589/397448B23EFB11D0F697386D44E1916C/50',
		'figureurl_2':'http://qzapp.qlogo.cn/qzapp/100330589/397448B23EFB11D0F697386D44E1916C/100',
		'figureurl_qq_1':'http://q.qlogo.cn/qqapp/100330589/397448B23EFB11D0F697386D44E1916C/40',
		"figureurl_qq_2":'http://q.qlogo.cn/qqapp/100330589/397448B23EFB11D0F697386D44E1916C/100'
		}
		return retJson

