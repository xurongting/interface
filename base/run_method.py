# -*- coding: utf-8 -*-
# @Time    : 2018/6/11 0011 下午 3:52
# @Author  : 许榕亭
# @File    : run_method.py
# @Software: PyCharm
import requests


class RunMain:
    def send_post(self, url, data, header=None):
        """
        发送post请求
        :param url: 请求地址
        :param data: 请求参数
        :param header: 请求头部
        :return: 响应数据
        """
        res = requests.post(url=url, data=data, headers=header)
        return res

    def send_get(self, url, data=None, header=None):
        """
        发送get请求
        :param url: 请求地址
        :param data: 请求参数
        :param header: 请求头部
        :return: 响应数据
        """
        res = requests.get(url=url, data=data,  headers=header)
        return res

    def run_main(self, method, url, data=None, header=None):
        """
        根据请求方式发送请求
        :param method: 请求方式
        :param url: 请求地址
        :param data: 请求参数
        :param header: 请求头部
        :return: 响应数据
        """
        if method == 'get':
            res = self.send_get(url, data, header)
        else:
            res = self.send_post(url, data, header)
        return res
