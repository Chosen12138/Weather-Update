import os
from lib import *


make_paths()


def get_weather_pdf(country):
    #   if case
    if country == '巴西':
        mapper = BRAMapperURL()
        image_columns = (2, 2)
    elif country == '美国':
        mapper = USAMapperURL()
        image_columns = (3, 2)
    elif country == '阿根廷':
        mapper = ARGMapperURL()
        image_columns = (2, 2)
    else:
        return
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

    for area in mapper.areas:
        file_path = os.path.join(SUPPORT.today_pic_path, country, f'State_{area}')
        dynamic_urls = mapper.ag_weather_urls(area)
        for name, url in dynamic_urls.items():
            requestImg(url=url,
                       file_path=file_path,
                       name=name)

        if os.listdir(file_path):
            merge_small_images(image_dir_path=file_path,
                               image_save_path=img_save_path,
                               image_save_name=f'State_{area}',
                               image_size=1024,
                               image_colnum=image_columns[1])

    paste_and_pdf(path=os.path.join(SUPPORT.today_pic_path, country, '合成'),
                  face=f'封面_{country}',
                  if_parse=1,
                  out_path=os.path.join(SUPPORT.report_path,
                                        f'【{SUPPORT.today_int}】{country}产区天气报告.pdf'))
    return


if __name__ == '__main__':
    get_weather_pdf('巴西')
    get_weather_pdf('阿根廷')
    get_weather_pdf('美国')