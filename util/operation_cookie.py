# -*- coding: utf-8 -*-
# @Time    : 2018/6/12 0012 上午 11:42
# @Author  : 许榕亭
# @File    : operation_cookie.py
import requests
import json
from util.operation_json import OperationJson
from base.run_method import RunMain


class OperationCookie:
    def __init__(self, response):
        """
        初始化cookie类
        :param response: 响应数据
        """
        self.response = response

    # def get_response_url(self):
    #     """
    #     获取登录返回的token的url
    #     :return: 带token的url
    #     """
    #     response_url = self.response['data']['url'][0]
    #     return response_url
    #     pass

    def get_cookie(self):
        """
        获取cookie的jar文件
        :return:
        """
        # request_url = self.get_response_url() + "&callback=jQuery21008240514814031887_1508666806688&_=1508666806689"
        # cookie = requests.get(request_url).cookies
        # return cookie
        cookie = self.response.cookies
        return cookie

    def write_cookie(self):
        """
        写入cookie到json文件中
        :return:
        """
        cookie = requests.utils.dict_from_cookiejar(self.get_cookie())
        op_json = OperationJson()
        op_json.write_data(cookie)

#
# url = 'http://zz.fetv.cn/YcE/ashx/Login.ashx'
# data = {
#     "action": "getVerifyCode"
# }
# r = RunMain()
# res = r.run_main('post', url, data)
# # code = requests.utils.dict_from_cookiejar(res)['validateCookie'][8:]
#
# c = OperationCookie(res)
# c.write_cookie()



# data2 = {
#     "action": "userLogin",
#     "user": "admin",
#     "psw": "123456",
#     "yzm": code
# }
# cookie2 = requests.post(url, data2).cookies
# print(requests.utils.dict_from_cookiejar(cookie2))
#
# url1 = 'http://zz.fetv.cn/YcE/ashx/NavigationList.ashx'
# data3 = {
#     'action': 'getNavigationList'
# }
# res = requests.post(url1, data3, cookies=cookie2)
# print(res.text)