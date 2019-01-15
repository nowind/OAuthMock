#!/usr/bin/python
# -*- coding: utf-8 -*-
import web,requests,yaml,json,random,time,sys
from OAuthMock import OAuthMock
class WeiBoAuth(OAuthMock):
	def __getWeiBoUid(self):
		return self._MockGetToken()+'_uid'
	def Mockaccess_token(self):
		return  {
       "access_token": self._MockGetToken()+'_atoken',
       "expires_in": random.randint(1234,9994),
       "remind_in":"%d"%random.randint(1234,9994),
       "uid":self.__getWeiBoUid()
 			}
 	def Mockget_token_info(self):
		token=self._MockGetToken()
		return {'uid':self.__getWeiBoUid(),'appKey':'testKey','scope':None,'create_at':0,'expire_in':random.randint(1234,9994)}
 	def Mockshow(self):
 		if 'uid' in self.webIunpt:
 			uid=hash(self.webIunpt['uid'])
 		else:
 			uid=self._getUidHash()
 		return {
 			'id':uid,
 			"screen_name": "zaku",
 			  "name": "zaku123",
			    "province": "11",
			    "city": "5",
			    "location": "北京 朝阳区",
			    "description": "人生五十年，乃如梦如幻；有生斯有死，壮士复何憾。",
			    "url": "http://blog.sina.com.cn/zaku",
			    "profile_image_url": "http://tp1.sinaimg.cn/1404376560/50/0/1",
			    "domain": "zaku",
			    "gender": "m",
			    "followers_count": 1204,
			    "friends_count": 447,
			    "statuses_count": 2908,
			    "favourites_count": 0,
			    "created_at": "Fri Aug 28 00:00:00 +0800 2009",
			    "following": False,
			    "allow_all_act_msg": False,
			    "geo_enabled": True,
			    "verified": False,
			      "status": {
			        "created_at": "Tue May 24 18:04:53 +0800 2011",
			        "id": 11142488790,
			        "text": "我的相机到了。",
			        "source": '<a href="http://weibo.com" rel="nofollow">新浪微博</a>',
			        "favorited": False,
			        "truncated": False,
			        "in_reply_to_status_id": "",
			        "in_reply_to_user_id": "",
			        "in_reply_to_screen_name": "",
			        "geo": None,
			        "mid": "5610221544300749636",
			        "annotations": [],
			        "reposts_count": 5,
			        "comments_count": 8
			    },
			    "allow_all_comment": True,
			    "avatar_large": "http://tp1.sinaimg.cn/1404376560/180/0/1",
			    "verified_reason": "",
			    "follow_me": False,
			    "online_status": 0,
			    "bi_followers_count": 215
 		}