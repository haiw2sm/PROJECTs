# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 21:20:10 2021

@author: w2hi
"""
from source.module.confusion.css import ParseEncodedStr
from source.spider.shop import DianPing

try:
	from settings import *
except Exception as e:
	raise e

if __name__ == '__main__':
	dp = DianPing(DATA_DIR, city='suzhou')
	dp.run()