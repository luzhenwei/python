# 有序字典
from collections import OrderedDict
# 存储数据
from pyexcel_xls import save_data


def makeExcelFile(path, data):
    dic = OrderedDict()
    for sheetNum, sheetValue in data.items():
        d = {}
        d[sheetNum] = sheetValue
        dic.update(d)

    save_data(path, dic)


path = r"D:\\workspace\\python\\demo\\20191125\\信息.xlsx"
makeExcelFile(path, {"sheet1": [[20190102, '李四', '男']]})
