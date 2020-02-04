import fitz
import time
import re
import os
import xlsxwriter


def pdf2pic(path, pic_path):
    t0 = time.clock()  # 生成图片初始时间
    checkXO = r"/Type(?= */XObject)"  # 使用正则表达式来查找图片
    checkIM = r"/Subtype(?= */Image)"
    doc = fitz.open(path)  # 打开pdf文件
    imgcount = 0  # 图片计数
    lenXREF = doc._getXrefLength()  # 获取对象数量长度

    # 打印PDF的信息
    print("文件名:{}, 页数: {}, 对象: {}".format(path, len(doc), lenXREF - 1))
    imageList=[]
    # 遍历每一个对象
    for i in range(1, lenXREF):
        text = doc._getXrefString(i)  # 定义对象字符串
        isXObject = re.search(checkXO, text)  # 使用正则表达式查看是否是对象
        isImage = re.search(checkIM, text)  # 使用正则表达式查看是否是图片
        if not isXObject or not isImage:  # 如果不是对象也不是图片，则continue
            continue
        imgcount += 1
        # if imgcount != 12:
        #     continue
        pix = fitz.Pixmap(doc, i)  # 生成图像对象
        new_name = "图片{}.png".format(time.time())  # 生成图片的名称
        imageList.append(new_name)
        if pix.n < 5:  # 如果pix.n<5,可以直接存为PNG
            pix.writePNG(os.path.join(pic_path, new_name))
        else:  # 否则先转换CMYK
            pix0 = fitz.Pixmap(fitz.csRGB, pix)
            pix0.writePNG(os.path.join(pic_path, new_name))
            pix0 = None
        pix = None  # 释放资源
        t1 = time.clock()  # 图片完成时间

        print("运行时间:{}s".format(t1 - t0))
        print("提取了{}张图片".format(imgcount))
    imagePath = imageList[-2]
    imageList.pop(len(imageList)-2)
    for image in imageList:
        os.remove(pic_path + '\\' + image)
    book = xlsxwriter.Workbook('pict.xlsx')
    sheet = book.add_worksheet('demo')
    sheet.insert_image('D4',pic_path + '\\' + '图片1580746665.5868943.png')
    book.close()

if __name__ == '__main__':
    # path = r"G:\office\DC19410100464231922_JDCJ_a53f8279-3e0c-4bcd-890d-57c396e98ccd.pdf"
    path = r"G:\office\DC19410100464231922_JDCJ_a53f8279-3e0c-4bcd-890d-57c396e98ccd.pdf"
    # path = r"G:\office\DC19410100464231996_JDCJ_c2b26780-be85-456f-a860-7eaf82783ddf.pdf"
    # path = r"G:\office\DC19410100464231996_JDCJ_c2b26780-be85-456f-a860-7eaf82783ddf.pdf"
    pic_path = r"G:\pythonTmp"
    # 创建保存图片的文件夹
    if os.path.exists(pic_path):
        print("文件夹已存在，不必重新创建！")
        pass
    else:
        os.mkdir(pic_path)
    pdf2pic(path, pic_path)