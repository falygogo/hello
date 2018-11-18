# coding:utf-8
import requests

base = 'http://127.0.0.1:81'  # 禅道的服务器地址

loginUrl = base+"/zentao/user-login.html"

h = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
    "Accept-Encoding": "gzip, deflate",
    "Referer": base+"/zentao/user-login.html",
    # "Cookie":  # 头部没登录前不用传cookie，因为这里cookie就是保持登录的
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded",
    }

body = {"account": "admin",
        "password": "e10adc3949ba59abbe56e057f20f883e",
        "keepLogin[]": "on",
        "referer": base+"/zentao/my/"
        }

s = requests.session()  # 保持会话
r = s.post(loginUrl, data=body, headers=h)
print r.content  # 打印结果看到location='http://127.0.0.1/zentao/my/'说明登录成功了

# 提交bug
url1 = base+"/zentao/bug-create-1-0-moduleID=0.html"
f = {
    "product": "1",
    "module": "0",
    "project": "",
    "openedBuild[]": "trunk",
    "assignedTo": "admin",
    "type": "codeerror",
    "os": "all",
    "browser": "all",
    "color": "",
    "title": "yoyoketang-这是一个bug描述1122",
    "severity": "3",
    "pri": "0",
    "steps": '<p>[步骤]</p>\
            <p>1、第一步点</p>\
            <p>2、第二步点</p>\
            <p>3、点三步点</p>\
            <p>[结果]</p>\
            <p><img src="data/upload/1/201712/072254170557cdn.png" alt="" /></p>\
            <p>[期望]</p>',
    "story": "0",
    "task": "0",
    "mailto[]": "",
    "keywords": "",
    "files[]": "",
    "labels[]": "",
    "uid": "5a2955c884f98",
    "case": "0",
    "caseVersion": "0",
    "result": "0",
    "testtask": "0"
    }

r = s.post(url1, data=f)
print r.content