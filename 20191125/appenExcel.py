#!/usr/bin/env python
# -*- coding:utf-8 -*-

from xlrd import open_workbook
from xlutils.copy import copy
def appendCont(path):
    r_xls = open_workbook(path) # 读取excel文件
    row = r_xls.sheets()[0].nrows # 获取已有的行数
    excel = copy(r_xls) # 将xlrd的对象转化为xlwt的对象
    table = excel.get_sheet(0) # 获取要操作的sheet

    #对excel表追加一行内容
    table.write(row, 0, '内容1') #括号内分别为行数、列数、内容
    table.write(row, 1, '内容2')
    table.write(row, 2, '内容3')

    excel.save(path) # 保存并覆盖文件'
path = r"D:\\workspace\\python\\demo\\20191125\\new.xlsx"
appendCont(path)