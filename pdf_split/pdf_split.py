import os
from PyPDF2 import PdfWriter, PdfReader



def pdf_split(pdf_in, pdf_out, start, end):
    # 初始化一个pdf
    output = PdfWriter()
    # 读取pdf
    with open(pdf_in, 'rb') as in_pdf:
        pdf_file = PdfReader(in_pdf)
        # 从pdf中取出指定页
        for i in range(start, end):
            output.add_page(pdf_file.pages[i])
        # 写出pdf
        with open(pdf_out, 'ab') as out_pdf:
            output.write(out_pdf)


if __name__ == '__main__':
    pdf_in  = './main.pdf'
    pdf_file = PdfReader(pdf_in)
    
    pdf_out_0 = './Graphical Abstract.pdf'
    pdf_out_1 = './HightLights.pdf'
    pdf_split(pdf_in, pdf_out_0, start=0, end=1)
    pdf_split(pdf_in, pdf_out_1, start=1, end=2)
