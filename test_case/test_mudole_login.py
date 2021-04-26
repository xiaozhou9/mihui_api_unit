import unittest

from ddt import ddt, data, unpack

from common.HttpRequest import Httprequests
from common.logger import *
from common.read_excel import read_login

url = 'http://test-www.mihuiai.com'
login_uri = '/r/user/login'
http = Httprequests(url)


@ddt()
class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        logger.info('执行前置')
        logger.warning('=====================执行本次自动化测试用例用例=====================')
        pass
    @classmethod
    def tearDown(self) -> None:
        logger.info('执行后置')
        pass

    @data(*read_login())
    @unpack
    def test_login(self, username, password, autoLogin, as_message, as_success, as_status, tips, text):
        logger.info('******开始执行登录用例*******')
        logger.info(f'输入用户信息>>>>>>>>> {username} {password} {text}')
        payload = {"userName": username, "password": password, "autoLogin": autoLogin}
        response = http.post(login_uri, json=payload)
        logger.info(f'测试结果>>>>>>>>>>{response.json()["message"]}')
        logger.info(f'期望结果>>>>>>>>>>{as_message}')
        self.assertEqual(as_message, response.json()['message'], msg=tips)
        self.assertEqual(as_success, response.json()['success'], msg=tips)
        self.assertEqual(as_status, response.status_code, msg=tips)

