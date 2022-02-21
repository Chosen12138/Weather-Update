import os.path
from urllib.error import HTTPError, URLError
from http.client import IncompleteRead, RemoteDisconnected
import urllib.request
from datetime import date

from lib.config import SUPPORT

__all__ = ["requestImg", "make_paths"]


def make_paths():

    if not os.path.exists(SUPPORT.picture_path):
        os.mkdir(SUPPORT.picture_path)

    if not os.path.exists(SUPPORT.today_pic_path):
        os.mkdir(SUPPORT.today_pic_path)

    return


def requestImg(url: str,
               name: str,
               num_retries: int = 3,
               file_path: str = SUPPORT.today_pic_path,
               ):

    if not os.path.exists(file_path):
        os.mkdir(file_path)

    filename = name + '.jpg'
    img_src = url
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) \
        AppleWebKit/537.36 (KHTML, like Gecko) \
            Chrome/35.0.1916.114 Safari/537.36',
        'Cookie': 'AspxAutoDetectCookieSupport=1'
    }

    req = urllib.request.Request(url=img_src, headers=header) 
    try:
        response = urllib.request.urlopen(req)
        with open(os.path.join(file_path, filename), "wb") as f:
            content = response.read()
            f.write(content)
            response.close()
    except HTTPError as e:
        print(f'HTTP异常:{e.reason}, url:{img_src}')
        raise NotImplementedError
    except URLError as e:
        print(f'URL异常:{e.reason}, url:{img_src}')
        raise NotImplementedError
    except IncompleteRead or RemoteDisconnected as e: 
        if num_retries == 0:
            return
        else:
            requestImg(url, name, num_retries-1)






if __name__ == '__main__':

    this_week_date = "20220215"
    # url = f"https://droughtmonitor.unl.edu/data/png/{this_week_date}/{this_week_date}_conus_none.png"
    # name = f"US_Drought_{this_week_date}"
    # url = "https://www.cpc.ncep.noaa.gov/products/analysis_monitoring/regional_monitoring/cmi.gif"
    # name = f"US_Moisture_{this_week_date}"
    url = "https://www.cpc.ncep.noaa.gov/products/JAWF_Monitoring/GFS/AR_curr.p.gfs1a.gif"
    name = 'AGR'
    requestImg(url, name)