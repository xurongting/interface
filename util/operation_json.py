# -*- coding: utf-8 -*-
# @Time    : 2018/6/11 0011 上午 10:55
# @Author  : 许榕亭
# @File    : operation_excel.py
# @Software: PyCharm
import json


# 定义操作json类
class OperationJson:

    def __init__(self, file_path=None):
        """
        初始化json类
        :param file_path: json文件名
        """
        if file_path is None:
            self.file_path = '../data_config/user.json'
        else:
            self.file_path = file_path
        self.data = self.read_data()

    def read_data(self):
        """
        读取json文件内容
        :return: 文件内容
        """
        with open(self.file_path) as fp:
            data = json.load(fp)
            return data

    def get_data(self, json_id):
        """
        根据关键字json_id获取数据
        :param json_id: json关键字
        :return: json_id对应的数据
        """
        return self.data[json_id]

    def write_data(self, data):
        """
        写入json到文件中
        :param data: 写入的内容
        """
        with open('../data_config/cookie.json', 'w') as fp:
            fp.write(json.dumps(data))
