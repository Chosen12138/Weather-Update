import fitz
import time
import re
import os

__all__ = ['get_pic_from_pdf']


def get_pic_from_pdf(pdf_path, pic_path, start_page: int = 1):
    """
    # 从pdf中提取图片
    :param start_page: 提取开始页
    :param pdf_path: pdf的路径
    :param pic_path: 图片保存的路径
    :return:
    """
    t0 = time.perf_counter()
    # 使用正则表达式来查找图片
    checkXO = r"/Type(?= */XObject)"
    checkIM = r"/Subtype(?= */Image)"

    # 打开pdf
    doc = fitz.open(pdf_path)
    # 图片计数
    imgcount = 0
    lenXREF = doc.xref_length()

    # 打印PDF的信息
    print("文件名:{}, 页数: {}, 对象: {}".format(pdf_path, len(doc), lenXREF - 1))

    # 遍历每一个对象
    for i in range(start_page, lenXREF):
        # 定义对象字符串
        text = doc.xref_object(i)
        isXObject = re.search(checkXO, text)
        # 使用正则表达式查看是否是图片
        isImage = re.search(checkIM, text)
        # 如果不是对象也不是图片，则continue
        if not isXObject or not isImage:
            continue
        imgcount += 1
        # 根据索引生成图像
        pix = fitz.Pixmap(doc, i)
        # 根据pdf的路径生成图片的名称
        new_name = ("IMG_0{}_".format(imgcount) if imgcount < 10 else "IMG_{}_".format(imgcount)) + pdf_path.split('/')[-1].split('\\')[-1].split('.')[0] + ".jpg"
        new_name = new_name.replace(':', '')

        # 如果pix.n<5,可以直接存为PNG
        if pix.n < 5:
            pix.save(os.path.join(pic_path, new_name))
        # 否则先转换CMYK
        else:
            pix0 = fitz.Pixmap(fitz.csRGB, pix)
            pix0.save(os.path.join(pic_path, new_name))
            pix0 = None
        # 释放资源
        pix = None
        t1 = time.perf_counter()
        print("运行时间:{}s".format(t1 - t0))
        print("提取了{}张图片".format(imgcount))
    return


def get_file_from_url(url_file):
    import requests
    import io
    """not work for malaysia`"""
    send_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
        "Connection": "keep-alive",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8"}
    req = requests.get(url_file, headers=send_headers)  # 通过访问互联网得到文件内容
    bytes_io = io.BytesIO(req.content)  # 转换为字节流
    with open('temp.pdf', 'wb') as file:
        file.write(bytes_io.getvalue())  # 保存到本地
    # import time
    # time.sleep(2) # 最好做一个休眠
    return bytes_io

