#!/usr/bin/python
# -*- coding: utf-8 -*-
import web,requests,yaml,json,random,time,sys
from OAuthMock import OAuthMock
class RenRenAuth(OAuthMock):
	def Mocktoken(self):
		token=self._MockGetToken()
		return {
		 "token_type":["bearer","mac"][random.randint(0,1)],
		  "expires_in":self.expires_in,
		   "refresh_token":token+'_rtoken',
		   "user":{ 
		   "id":self._getUidHash(), 
		   "name":"二小姐",
		    "avatar":[ 
		    { "type":"avatar", "url":"http://hdn.xnimg.cn/photos/hdn121/20130805/2055/h_head_KFTQ_d536000000d0111b.jpg" },
		     { "type":"tiny", "url":"http://hdn.xnimg.cn/photos/hdn221/20130805/2055/tiny_jYQe_ec4300051e7a113f.jpg" },
		      { "type":"main", "url":"http://hdn.xnimg.cn/photos/hdn121/20130805/2055/h_main_ksPJ_d536000000d0111b.jpg"}, 
		      { "type":"large", "url":"http://hdn.xnimg.cn/photos/hdn121/20130805/2055/h_large_yxZz_d536000000d0111b.jpg" } 
		      ] },
		       "access_token":token+'_atoken',
		       "scope":"read_user_feed read_user_album"
		}