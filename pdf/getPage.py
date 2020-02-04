from PyPDF2 import PdfFileWriter, PdfFileReader

# 开始页
start_page = 0

# 截止页
end_page = 5

output = PdfFileWriter()
pdf_file = PdfFileReader(open(r"G:\office\DC19410100464231922_JDCJ_a53f8279-3e0c-4bcd-890d-57c396e98ccd.pdf", "rb"))
pdf_pages_len = pdf_file.getNumPages()

# 保存input.pdf中的1-5页到output.pdf
output.addPage(pdf_file.getPage(2))

outputStream = open("output.pdf", "wb")
output.write(outputStream)