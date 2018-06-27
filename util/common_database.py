# -*- coding: utf-8 -*-
# @Time    : 2018/6/12 0012 下午 3:34
# @Author  : 许榕亭
# @Site    : 
# @File    : common_database.py
# @Software: PyCharm
#coding:utf-8
import MySQLdb.cursors
import json
class OperationMysql:
	def __init__(self):
		self.conn = MySQLdb.connect(
			host='localhost',
			port=3306,
			user='root',
			passwd='123456',
			db='le_study',
			charset='utf8',
			cursorclass=MySQLdb.cursors.DictCursor
			)
		self.cur = self.conn.cursor()

	#查询一条数据
	def search_one(self,sql):
		self.cur.execute(sql)
		result = self.cur.fetchone()
		result = json.dumps(result)
		return result
