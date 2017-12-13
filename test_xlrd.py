# -*- coding:utf-8 -*-
import xlrd
import  xlwt
import openpyxl
#设置文件地址
file = "C:/Users/dongxue/Desktop/test.xlsx"
#读取文件
book =xlrd.open_workbook(file)
#通过名字获取sheet
sheet_data= book.sheet_by_name("one")
#通过索引设置sheet
sheet_index=book.sheet_by_index(0)
print sheet_data.name
# b=sheet_data.cell(1,1).value
# print b
nrows = sheet_data.nrows

file1 = xlwt.Workbook()

sheet1 = file1.add_sheet(u"dongxue")
sheet2 = file1.add_sheet(u"lizhi")

row = 0
temp =[u"姓名",u"年龄",u"学校",u"专业"]
for pos,v in enumerate(temp):
    sheet1.write(row,pos,v)
row = row+1
sheet1.write(row,0,u"葡萄")
sheet1.write(row,2,u"北京电影学院")
sheet1.write(row,1,"19")
sheet1.write(row,3,u"计算机科学与技术专业")
file1.save("test1.xls")


