# -*- coding: utf-8 -*-
# @Time    : 2018/6/12 0012 上午 8:53
# @Author  : 许榕亭
# @File    : dependent_data.py
# @Software: PyCharm
from util.operation_excel import OperationExcel
from base.run_method import RunMain
from data.get_data import GetData
from jsonpath_rw import jsonpath, parse
import json
from util.operation_cookie import OperationCookie
from util.operation_json import OperationJson


class DependentData:
    def __init__(self, case_id):
        """
        初始化数据依赖类
        :param case_id: 依赖的用例id
        """
        self.case_id = case_id
        self.opera_excel = OperationExcel()
        self.data = GetData()

    def get_case_line_data(self):
        """
        根据case_id获取行的内容
        :param case_id: 用例id
        :return:整行内容
        """
        return self.opera_excel.get_rows_data(self.case_id)

    def run_dependent(self):
        """
        执行依赖的用例id，获取响应数据
        :return: 返回响应数据
        """
        run_method = RunMain()
        row_num = self.opera_excel.get_row_index(self.case_id)
        request_data = self.data.get_data_for_json(row_num)
        url = self.data.get_request_url(row_num)
        method = self.data.get_method(row_num)
        header = self.data.is_header(row_num)
        res = run_method.run_main(method, url, request_data, header)
        return res

    def get_data_for_key(self, row):
        """
        获取响应数据中的依赖返回值
        :param row: 行数
        :return: 依赖返回值
        """
        depend_data = self.data.get_depend_key(row)

        response_data = self.run_dependent()
        if "validateCookie" in depend_data:
            cookie = OperationCookie(response_data)
            cookie.write_cookie()
            code = OperationJson('../data_config/cookie.json')
            return code.get_data(depend_data)[8:]
        else:
            json_rules = parse(depend_data)
            result = json_rules.find(json.loads(response_data.text))
            return [math.value for math in result][0]
