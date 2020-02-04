# 首先得登录上，记住请求的时候用post，然后拿到cookies
import requests
import time
import html
import json
from bs4 import BeautifulSoup
from xlrd import open_workbook
from xlutils.copy import copy
import xlsxwriter

# 国抽
from requests_html import HTMLSession

session = HTMLSession()

# 获取获取检验数据列表  需在网页登陆后获取
pageUrl = r'http://spcjinsp.gsxt.gov.cn/test_platform/api/food/getFood?order=desc&offset=0&limit=1600&dataType=8&startDate=2019-11-04&endDate=2020-02-04&taskFrom=%E9%83%91%E5%B7%9E%E5%B8%82%E5%B8%82%E5%9C%BA%E7%9B%91%E7%9D%A3%E7%AE%A1%E7%90%86%E5%B1%80&samplingUnit=&testUnit=&enterprise=&sampledUnit=&foodName=&province=&reportNo=&bsfla=&bsflb=%E9%A3%9F%E5%A0%82&sampleNo=&foodType1=&foodType4=&sampleNo_index=1&_=1580823934475'
# 获取检验数据详情
infoUrl = r'http://spcjinsp.gsxt.gov.cn/test_platform/foodTest/foodDetail/%s'
# 请求头信息 需在网页登陆后获取
headers_1 = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Cookie': 'JSESSIONID=6CB01FFF7E8600061825CAC04B0099E6; sod=78BfmGxCj499kLYsDQEjJubNB8yIgWPL6NnOMji9m6Oi27UOyxhjeremyRshwVFPjMyxhjeremy8OFdIYik5yxhjeremyUB64XA=',
    'Host': 'spcjinsp.gsxt.gov.cn',
    'Referer': 'http://spcjinsp.gsxt.gov.cn/test_platform/?d=2259',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'

}
pathUrl = r'G:\pythonProject\getUrlData\test.xlsx'


def getData(infoUrl):
    # 有密码的请求一定要用post()
    response = session.get(infoUrl, headers=headers_1)
    html_doc = response.text
    soup = BeautifulSoup(html_doc, "lxml")
    # print(soup.prettify())
    divs = soup.find_all('div', class_="ibox float-e-margins")
    # print(len(divs))
    address = []
    for div in divs:
        if div.text.find('抽检场所信息') >= 0 and div.text.find('所在地：') >= 0:
            textStr = div.text
            startNum = textStr.find("所在地：")
            endNum = textStr.find("区域类型：")
            address.append(textStr[startNum + 4:endNum].strip())
        elif div.text.find('生产企业信息') >= 0 and div.text.find('所在地：') >= 0:
            textStr = div.text
            startNum = textStr.find("所在地：")
            endNum = textStr.find("企业地址：")
            address.append(textStr[startNum + 4:endNum].strip())
    return address


#
def getAllPageData(pageUrl):
    response = session.get(pageUrl, headers=headers_1)
    infoJson = json.loads(response.text)  # 先把字典转成json
    infoList = []
    num = 1

    for info in infoJson['rows']:
        # oneList = [info['id'], info['sp_s_16']]
        oneList = [info['sp_s_16']]
        # print(info['id'])
        # print(info['sp_s_16'])
        oneList.extend(getData(infoUrl % info['id']))
        print(oneList)
        updateExcel(sheet, num, oneList)
        num += 1
        infoList.append(oneList)
    return infoList


def updateExcel(sheet, num, aList):
    sheet.write('A' + str(num + 1), aList[0])
    sheet.write('B' + str(num + 1), aList[1])
    sheet.write('C' + str(num + 1), aList[2])


if __name__ == "__main__":

    book = xlsxwriter.Workbook('test.xlsx')
    sheet = book.add_worksheet('sheet1')
    sheet.write('A1', '抽样单号')
    sheet.write('B1', '被抽检单位所在县（市、区）')
    sheet.write('C1', '标称生产企业所属省份城市')
    getAllPageData(pageUrl)
    book.close()
    print("======执行完毕，请查看文件======")

