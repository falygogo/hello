# coding:utf-8
import requests
import unittest
from page.loginclass import Login
from page.fatieapi import FaTie

class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.s = requests.session()

    def setUp(self):
        self.login = Login(self.s)
        self.fatie = FaTie(self.s)

    def tearDown(self):
        # 每次用例之后，清空cookie
        self.s.cookies.clear_session_cookies()

    def test_fatie_01(self):
        self.login.login()  # 1登录
        self.fatie.fatie() # 2发帖
        result =self.fatie.is_fatie_sucess() # 3获取结果
        self.assertTrue(result)



if __name__ == "__main__":
    unittest.main()
