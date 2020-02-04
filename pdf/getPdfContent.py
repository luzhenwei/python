import pdfplumber
import pandas as pd
import re

with pdfplumber.open(r"G:\office\DC19410100464231951_JDCJ_63a114bc-2621-4859-9c80-f9fd38a97f4d.pdf") as pdf:
    page_count = len(pdf.pages)
    print(page_count)  # 得到页数


    for pdf_table in pdf.pages[2].extract_tables(table_settings={"vertical_strategy": "text",
                                                     "horizontal_strategy": "lines",
                                                    "intersection_tolerance":20}): # 边缘相交合并单元格大小

        # print(pdf_table)
        for row in pdf_table:
            # 去掉回车换行
            print([re.sub('\s+', '', cell) if cell is not None else None for cell in row])
    # str = pdf.pages[2].extract_tables(table_settings={"vertical_strategy": "text",
    #                                             "horizontal_strategy": "lines",
    #                                             "intersection_tolerance": 20})[0][7][1]
    # print(str)