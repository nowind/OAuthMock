# OAuthMock
本项目通过Mock OAuth的接口，实现第三方UI测试登陆第三方需要扫码等认证。
## 实现方式
基于webpy架构一台具备mock hook pass 功能的服务器，实现对qq 微博 微信 人人 oauth登陆的mock
## 依赖
  * requests 转发请求
  * webpy web框架
  * pyaml 配置文件格式支持
## 配置方法
配置文件为oauth.yaml 一个案例如下：
``` yaml
WeiXinAuth:
  test:
    mock: ['userinfo','other']
  testfail:
    hook: '*'
    '*' : '{}'
  othertest:
    hook: 'userinfo'
    userinfo: '{"openid":"osiQlt455778bbLvFqrReBNPHq1","nickname":"朋友","sex":1,"language":"zh_CN","city":"","province":"","country":"CN","headimgurl":"http:\/\/wx.qlogo.cn\/111","privilege":[],"unionid":"oP4xHuIYS-8mmcr890ykooQLY8sM1"}'
    mock: '*'
```
  * WeiXinAuth 对应处理的类
  * test 为登陆回调给的access token
  * mock 表示用类内的函数调用返回
  * hook 表示使用指定的值返回
  *  * 替代所有
  * 其他未列出的直接pass
