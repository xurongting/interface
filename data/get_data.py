# -*- coding: utf-8 -*-
# @Time    : 2018/6/11 0011 下午 2:54
# @Author  : 许榕亭
# @File    : get_data.py
# @Software: PyCharm
from util.operation_excel import OperationExcel
from util.operation_json import OperationJson
from data.data_config import GlobalVar


# 定义获取数据类
class GetData:
    def __init__(self):
        """
        初始化获取数据类
        """
        self.opera_excel = OperationExcel()
        self.data_config = GlobalVar()

    def get_case_num(self):
        """
        获取excel行数,就是我们的case个数
        :return: case个数
        """
        return self.opera_excel.get_row()

    def is_run(self, row):
        """
        获取是否运行
        :param row: 所在行数
        :return: 是否运行的布尔值
        """
        col = int(self.data_config.get_run())
        run_model = self.opera_excel.get_cell(row, col)
        if run_model == 'yes':
            return True
        else:
            return False

    def is_cookie(self, row):
        """
        获取是否携带cookie
        :param row: 所在行数
        :return: cookie
        """
        col = int(self.data_config.get_cookie())
        cookie = self.opera_excel.get_cell(row, col)
        if cookie == "no":
            return None
        return cookie

    def is_header(self, row):
        """
        获取是否携带header
        :param row: 所在行数
        :return: header
        """
        col = int(self.data_config.get_header())
        header = self.opera_excel.get_cell(row, col)
        if header == "no":
            return None
        return header

    def get_method(self, row):
        """
        获取请求方式
        :param row: 所在行数
        :return: 请求方式
        """
        col = int(self.data_config.get_method())
        return self.opera_excel.get_cell(row, col)

    def get_request_url(self, row):
        """
        获取请求地址
        :param row: 所在行数
        :return: 请求地址
        """
        col = int(self.data_config.get_url())
        return self.opera_excel.get_cell(row, col)

    def get_request_data(self, row):
        """
        获取请求参数
        :param row: 所在行数
        :return: 请求参数
        """
        col = int(self.data_config.get_data())
        data = self.opera_excel.get_cell(row, col)
        if data == '':
            return None
        return data

    def get_data_for_json(self, row):
        """
        通过json获取关键字对应的数据
        :param row: 所在行数
        :return: 关键字对应的数据
        """
        operation_json = OperationJson()
        return operation_json.get_data(self.get_request_data(row))

    def get_expect_data(self, row):
        """
        获取预期结果
        :param row: 行数
        :return: 预期结果
        """
        col = int(self.data_config.get_expect())
        expect_data = self.opera_excel.get_cell(row, col)
        if expect_data == ' ':
            return None
        return expect_data

    def write_result(self, row, value):
        """
        写入实际结果
        :param row: 行数
        :param value: 写入的值
        """
        col = int(self.data_config.get_result())
        self.opera_excel.write_value(row, col, value)

    def get_depend_key(self, row):
        """
        获取依赖的返回数据
        :param row: 行数
        :return: 返回数据的格式
        """
        col = int(self.data_config.get_data_depend())
        depend_key = self.opera_excel.get_cell(row, col)
        if depend_key == "":
            return None
        else:
            return depend_key

    def is_depend(self, row):
        """
        判断是否有case依赖
        :param row: 行数
        :return: 返回依赖的用例id
        """
        col = int(self.data_config.get_case_depend())
        depend_case_id = self.opera_excel.get_cell(row, col)
        if depend_case_id == "":
            return None
        else:
            return depend_case_id

    def get_depend_field(self, row):
        """
        获取数据依赖字段
        :param row: 行数
        :return: 返回依赖字段
        """
        col = int(self.data_config.get_field_depend())
        data = self.opera_excel.get_cell(row, col)
        if data == "":
            return None
        else:
            return data
