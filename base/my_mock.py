# -*- coding: utf-8 -*-
# @Time    : 2018/6/11 0011 下午 2:33
# @Author  : 许榕亭
# @File    : my_mock.py
# @Software: PyCharm
from mock import mock


def mock_test(mock_method, request_data, url, method, response_data):
    """
    mock模拟请求响应
    :param mock_method: 方法名称
    :param request_data: 请求参数
    :param url: 请求url
    :param method: 请求方式
    :param response_data: 相应数据
    :return: 请求数据
    """
    mock_method = mock.Mock(return_value=response_data)
    return mock_method(url, method, request_data)
