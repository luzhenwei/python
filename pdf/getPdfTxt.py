import pdfplumber
import pandas as pd

with pdfplumber.open(r"G:\office\DC19410100464231922_JDCJ_a53f8279-3e0c-4bcd-890d-57c396e98ccd.pdf") as pdf:
    str = pdf.pages[2].extract_text()
    # print(str)
    startNum = str.find("抽样单编号")
    endNum = str.find("检查封样人员")
    # print(startNum)
    print(str[startNum:endNum].replace("抽样单编号",'').strip())
    # page_count = len(pdf.pages)
    # print(page_count)  # 得到页数
    # for page in pdf.pages:
    #     print('---------- 第[%d]页 ----------' % page.page_number)
    #     # 获取当前页面的全部文本信息，包括表格中的文字
    #     print(page[3].extract_text())
