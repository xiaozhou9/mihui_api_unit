# -*- coding: UTF-8 -*-
import os
import time
import unittest
import HTMLTestRunner
from test_case.test_mudole_login import TestLogin

if __name__ == '__main__':
    # suite = unittest.TestSuite()
    # suite.addTest(TestLogin('test_login'))
    # unittest.main(defaultTest=suite)
    # unittest.TextTestRunner().run(suite)
    suite_login = unittest.TestLoader().loadTestsFromTestCase(TestLogin)
    suite0 = unittest.TestSuite([suite_login])
    mow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
    report_title = '米绘企业版测试环境测试报告' + mow + '.html'
    exce_path = '/Users/baiwenkai/PycharmProjects/mihuiTestProject/mihuiapi_test_unittest/report'
    result_path = os.path.join(exce_path, report_title)
    des = '用于展示修改样式后的html'
    with open(result_path, 'wb') as report:
        runner = HTMLTestRunner.HTMLTestRunner(stream=report, title=report_title, description=des, verbosity=2)
        runner.run(suite0)
