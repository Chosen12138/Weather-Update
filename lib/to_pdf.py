import os

from PIL import Image, ImageDraw
from lib import *

__all__ = ['paste_and_pdf']


def paste_and_pdf(path, face='封面', width=3300, show=False, if_parse=None, out_path=rf'{SUPPORT.project_path}.pdf'):

    imgs = [os.path.join(path, name) for name in os.listdir(path)]
    imgs.insert(0, os.path.join(SUPPORT.project_path, 'cover', f'{face}.jpg'))
    size_list, img_list = [], []
    hight = 20 + 5*len(img_list)
    for im in imgs:

        img = Image.open(im).convert('RGB')
        img = img.resize((width, int(img.size[1] * width/img.size[0])), Image.ANTIALIAS)
        img_list.append(img)
        if if_parse:
            size_list.append(list(img.size))
            hight += img.size[1]
    if if_parse:
        size_lt = sorted(size_list, key=lambda x: x[0])
        width = size_lt[-1][0] + 10
        canv = Image.new('RGB', (width, hight), (255, 255, 255))
        y = 10
        for i in range(len(img_list)):

            size = size_list[i]
            dx = (width - size[0])//2
            canv.paste(img_list[i], (dx, y))
            img_list[i].close()
            y += size[1]+5
    else:
        canv = Image.new('RGB', (10 + img_list[0].size[0], 20 + len(img_list)*(img_list[0].size[1] + 5)), (255, 255, 255))
        for i in range(len(img_list)):
            canv.paste(img_list[i], (5, 10 + i*(5+img_list[0].size[1])))
            img_list[i].close()
    draw = ImageDraw.Draw(canv)
    draw.rectangle((0, 0, canv.size[0]-1, canv.size[1]-1), outline='black', width=5)
    canv.save(out_path, 'PDF', resolution=100.0, save_all=True)
    if show:
        canv.show()
    return


if __name__ == '__main__':
    path = os.path.join(SUPPORT.today_pic_path, '巴西', '合成')
    out_path = '巴西产区天气报告.pdf'
    paste_and_pdf(path, face='封面_巴西', if_parse=1, out_path=out_path)

