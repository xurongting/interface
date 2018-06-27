# -*- coding: utf-8 -*-
# @Time    : 2018/6/11 0011 上午 10:55
# @Author  : 许榕亭
# @File    : operation_excel.py
# @Software: PyCharm
import xlrd
from xlutils.copy import copy


# 定义表格操作类
class OperationExcel:
    def __init__(self, file_name='../data_config/case1.xls', sheet_id=0):
        """
        初始化表格类
        :param file_name: 表格文件名
        :param sheet_id: 表格索引值（从0开始）
        """
        self.file_name = file_name
        self.sheet_id = sheet_id
        self.data = self.get_data()

    def get_data(self):
        """
        获取表格内容
        :return: 表格内容
        """
        execl_file = xlrd.open_workbook(self.file_name)
        return execl_file.sheet_by_index(self.sheet_id)

    def get_row(self):
        """
        获取表格行数
        :return: 表格行数
        """
        return self.data.nrows

    def get_col(self):
        """
        获取表格列数
        :return: 表格列数
        """
        return self.data.ncols

    def get_cell(self, row, col):
        """
        根据行数和列数获取单元格内容
        :param row: 单元格所在行
        :param col: 单元格所在列
        :return: 单元格内容
        """
        return self.data.cell_value(row, col)

    def get_row_values(self, row):
        """
        根据行号获取整行内容
        :param row: 行数索引
        :return: 行内容
        """
        return self.data.row_values(row)

    def get_col_values(self, col=0):
        """
        根据列数获取整列内容
        :param col: 列数索引
        :return: 列内容
        """
        return self.data.col_values(col)

    def get_row_index(self, case_id):
        """
        根据对应的case_id获取所在行
        :param case_id: 用例id
        :return: 用例id所在行
        """
        text = self.get_col_values()
        index = 0
        for col_text in text:
            if case_id in col_text:
                return index
            index += 1

    def get_rows_data(self, case_id):
        """
        根据对应的case_id获取所在行的内容
        :param case_id: 用例id
        :return: 用例id所在行的内容
        """
        index = self.get_row_index(case_id)
        return self.get_row_values(index)

    def write_value(self, row, col, value):
        """
        测试结果写入excel
        :param row: 行数
        :param col: 列数
        :param value: 要写入的值
        """
        read_data = xlrd.open_workbook(self.file_name)
        write_data = copy(read_data)
        sheet_data = write_data.get_sheet(0)
        sheet_data.write(row, col, value)
        write_data.save(self.file_name)
