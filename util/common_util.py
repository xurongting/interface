# -*- coding: utf-8 -*-
# @Time    : 2018/6/11 0011 下午 5:29
# @Author  : 许榕亭
# @File    : common_util.py
# @Software: PyCharm
# coding:utf-8


class CommonUtil:
    def is_contain(self, str_one, str_two):
        """
        判断一个字符串是否再另外一个字符串中
        :param str_one: 查找的字符串
        :param str_two: 被查找的字符串
        :return: 是否存在的布尔值
        """
        flag = None
        # if isinstance(str_one, str):
        #     str_one = str_one.encode('unicode-escape').decode('string')
        if str_one in str_two:
            flag = True
        else:
            flag = False
        return flag

    # def is_equal_dict(self, dict_one, dict_two):
    #     """
    #     判断两个字典是否相等
    #     :param dict_one: 第一个字典
    #     :param dict_two: 第二个字典
    #     :return: 是否相等布尔值
    #     """
    #     if isinstance(dict_one, str):
    #         dict_one = json.loads(dict_one)
    #     if isinstance(dict_two, str):
    #         dict_two = json.loads(dict_two)
    #     return cmp(dict_one, dict_two)
