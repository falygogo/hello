# coding:utf-8
import unittest,time
import requests
import re

host = "http://127.0.0.1:81"

class FaTie():
    def __init__(self, s):
        self.s = s   # 初始化

    def fatie(self):
        url = ""
        body = {}
        r = self.s.post(url, data=body)
        return r.content

    def is_fatie_sucess(self):
        res = self.fatie()
        if "xx" == res:
            return True
        else:
            return False

if __name__ == "__main__":
    import loginclass
    s = requests.session()  # 定义一次
    login = loginclass.Login(s)
    login.login()

    fatie = FaTie(s)
    fatie.fatie()
    result = fatie.is_fatie_sucess()

