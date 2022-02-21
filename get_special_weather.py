import os
import urllib.request

from lib import *
from lib.to_pdf import paste_and_pdf

make_paths()


def get_southeast_asia_weather_pdf():
    country = '东南亚'
    mapper = SE_ASIA_MapperURL()
    image_columns = (2, 2)

    img_save_path = os.path.join(SUPPORT.today_pic_path, country, '合成')
    file_path = os.path.join(SUPPORT.today_pic_path, country, 'All_Nation')
    for name, url in mapper.fixed_urls.items():
        requestImg(url=url,
                   file_path=file_path,
                   name=name)

    if os.listdir(file_path):
        merge_small_images(image_dir_path=file_path,
                           image_save_path=img_save_path,
                           image_save_name='All_Nation',
                           image_size=1024,
                           image_colnum=image_columns[0])

    area = 'Indonesia'
    file_path = os.path.join(SUPPORT.today_pic_path, country, f'Nation_{area}')

    if_found = False
    max_nums = 0
    while not if_found:
        dynamic_urls = mapper.indonesia_weather_urls
        if max_nums > 30:
            break
        for name, url in dynamic_urls.items():
            try:
                requestImg(url=url,
                           file_path=file_path,
                           name=name)
                if_found = True
            except NotImplementedError:
                mapper.update_date()
                max_nums += 1
                break

    if os.listdir(file_path):
        merge_small_images(image_dir_path=file_path,
                           image_save_path=img_save_path,
                           image_save_name=f'Nation_{area}',
                           image_size=1024,
                           image_colnum=image_columns[1])

    area = 'Malaysia'
    pdf_path = os.path.join(SUPPORT.today_pic_path, country, f'{SUPPORT.today_int}马来西亚月度气候报告.pdf')
    urllib.request.urlretrieve(mapper.malaysia_weather_report_urls['马来西亚月度气候报告'], pdf_path)
    file_path = os.path.join(SUPPORT.today_pic_path, country, f'Nation_{area}')
    if not os.path.exists(file_path):
        os.mkdir(file_path)

    get_pic_from_pdf(pdf_path=pdf_path,
                     pic_path=file_path,
                     start_page=2)

    if os.listdir(file_path):
        all_pics = os.listdir(file_path)
        all_pics.sort()
        if len(all_pics) >= 2:
            os.remove(os.path.join(file_path, all_pics[0]))
            os.remove(os.path.join(file_path, all_pics[1]))
            os.remove(os.path.join(file_path, all_pics[2]))

            merge_small_images(image_dir_path=file_path,
                               image_save_path=img_save_path,
                               image_save_name=f'Nation_{area}',
                               image_size=1024,
                               image_colnum=image_columns[1],
                               )

    paste_and_pdf(path=os.path.join(SUPPORT.today_pic_path, country, '合成'),
                  face=f'封面_{country}',
                  if_parse=1,
                  out_path=os.path.join(SUPPORT.report_path,
                                        f'【{SUPPORT.today_int}】{country}产区天气报告.pdf'))
    return


def get_global_weather_pdf():
    country = '全球'
    mapper = Global_MapperURL()
    image_columns = 2

    img_save_path = os.path.join(SUPPORT.today_pic_path, country, '合成')
    file_path = os.path.join(SUPPORT.today_pic_path, country, 'Overall')
    for name, url in mapper.fixed_urls.items():
        try:
            requestImg(url=url,
                       file_path=file_path,
                       name=name)
        except Exception:
            continue

    if_found = False
    max_nums = 0
    while not if_found:
        dynamic_urls = mapper.dynamic_urls
        if max_nums > 30:
            break
        for name, url in dynamic_urls.items():
            try:
                requestImg(url=url,
                           file_path=file_path,
                           name=name)
                if_found = True
            except NotImplementedError:
                mapper.update_date()
                max_nums += 1
                break

    if os.listdir(file_path):
        merge_small_images(image_dir_path=file_path,
                           image_save_path=img_save_path,
                           image_save_name='Overall',
                           image_size=1024,
                           image_colnum=image_columns)

    paste_and_pdf(path=os.path.join(SUPPORT.today_pic_path, country, '合成'),
                  face=f'封面_{country}',
                  if_parse=1,
                  out_path=os.path.join(SUPPORT.report_path, f'【{SUPPORT.today_int}】全球气候异常报告.pdf'))
    return


if __name__ == '__main__':
    # get_southeast_asia_weather_pdf()
    get_global_weather_pdf()