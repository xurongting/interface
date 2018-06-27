class GlobalVar:

    def __init__(self):
        self._id = '0'
        self._request_name = '1'
        self._url = '2'
        self._run = '3'
        self._method = '4'
        self._cookie = '5'
        self._header = '6'
        self._case_depend = '7'
        self._data_depend = '8'
        self._field_depend = '9'
        self._data = '10'
        self._expect = '11'
        self._result = '12'

    def get_id(self):
        """
        获取用例id
        :return: 用例id
        """
        return self._id

    def get_url(self):
        """
        获取请求地址
        :return: 请求地址
        """
        return self._url

    def get_run(self):
        """
        获取是否运行
        :return: 是否运行
        """
        return self._run

    def get_cookie(self):
        """
        获取是否有cookie
        :return: 是否有cookie
        """
        return self._cookie

    def get_method(self):
        """
        获取请求方式
        :return: 请求方式
        """
        return self._method

    def get_header(self):
        """
        获取是否携带header
        :return: 是否携带header
        """
        return self._header

    def get_case_depend(self):
        """
        获取case依赖
        :return: case依赖
        """
        return self._case_depend

    def get_data_depend(self):
        """
        获取依赖的返回数据
        :return: 依赖的返回数据
        """
        return self._data_depend

    def get_field_depend(self):
        """
        获取数据依赖字段
        :return: 数据依赖字段
        """
        return self._field_depend

    def get_data(self):
        """
        获取请求数据
        :return: 请求数据
        """
        return self._data

    def get_expect(self):
        """
        获取预期结果
        :return: 数据预期结果
        """
        return self._expect

    def get_result(self):
        """
        获取实际结果
        :return: 实际结果
        """
        return self._result