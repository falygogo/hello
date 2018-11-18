# coding:utf-8
import requests
import unittest
from page import loginapi
from page.loginclass import Login

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.s = requests.session()  # 实例化


    def test_login_01(self):
        a = loginapi.login(self.s , "admin", "e10adc3949ba59abbe56e057f20f883e")
        result = loginapi.is_login_sucess(a)
        print result
        self.assertTrue(result)

    def test_login_02(self):
        a = loginapi.login(self.s, "admin11", "e10adc3949ba59abbe56e057f20f883e")
        result = loginapi.is_login_sucess(a)
        print result
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()

