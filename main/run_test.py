# -*- coding: utf-8 -*-
# @Time    : 2018/6/11 0011 下午 4:05
# @Author  : 许榕亭
# @File    : run_test.py
# @Software: PyCharm
import sys
sys.path.append('E:/python/test_frame')
from base.run_method import RunMain
from data.get_data import GetData
from util.common_util import CommonUtil
from data.dependent_data import DependentData
from base.my_mock import mock_test
from util.send_email import SendEmail
from util.operation_cookie import OperationCookie
from util.operation_json import OperationJson

class RunTest:
    def __init__(self):
        """
        初始化RunTest类
        """
        self.run_method = RunMain()
        self.data = GetData()
        self.common_util = CommonUtil()
        self.send_email = SendEmail()

    def go_on_run(self):
        """
        执行测试用例
        :return: 通过用例和失败用例
        """
        pass_list = []
        fail_list = []
        rows_count = self.data.get_case_num()
        for i in range(1, rows_count):
            is_run = self.data.is_run(i)
            if is_run:
                url = self.data.get_request_url(i)
                method = self.data.get_method(i)
                data = self.data.get_data_for_json(i)
                cookie = self.data.is_cookie(i)
                header = self.data.is_header(i)
                expect = self.data.get_expect_data(i)
                if isinstance(expect, float):
                    expect = str(int(expect))
                depend_case = self.data.is_depend(i)
                if depend_case is not None:
                    depend_data = DependentData(depend_case)
                    # 获取依赖响应的返回数据
                    depend_response_data = depend_data.get_data_for_key(i)
                    # # 使用mock-test模拟请求
                    # depend_response_data = mock_test(self.run_method.run_main, data, url, "POST", order)
                    # 获取依赖的字段
                    depend_field = self.data.get_depend_field(i)
                    # 更新
                    data[depend_field] = depend_response_data
                if cookie == 'write':
                    res = self.run_method.run_main(method, url, data, header)
                    opera_cookie = OperationCookie(res)
                    opera_cookie.write_cookie()
                elif cookie == 'yes':
                    op_json = OperationJson('../data_config/cookie.json')
                    cookie = op_json.get_data('ASP.NET_SessionId')
                    cookies = {
                        'ASP.NET_SessionId': cookie
                    }
                    res = self.run_method.run_main(method, url, data, cookies)
                else:
                    res = self.run_method.run_main(method, url, data)
                if self.common_util.is_contain(expect, res.text):
                    # print("PASS")
                    pass_list.append(i)
                    self.data.write_result(i, 'PASS')
                else:
                    # print("FAILED")
                    fail_list.append(i)
                    self.data.write_result(i, 'FAILED')
        self.send_email.send_main(pass_list, fail_list)


if __name__ == '__main__':
    run = RunTest()
    run.go_on_run()
