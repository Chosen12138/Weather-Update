import os.path
import numpy as np
import pandas as pd
import urllib
import requests

from lib import *


crop = "大豆"
country = "巴西"


def get_VHI_data(crop="大豆", country="巴西"):
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) \
        AppleWebKit/537.36 (KHTML, like Gecko) \
            Chrome/35.0.1916.114 Safari/537.36',
        'Cookie': 'AspxAutoDetectCookieSupport=1'
    }

    if not os.path.exists(SUPPORT.data_path):
        os.mkdir(SUPPORT.data_path)

    if not os.path.exists(os.path.join(SUPPORT.data_path, country)):
        os.mkdir(os.path.join(SUPPORT.data_path, country))
    try:
        crop_symbol = VHIMapper.crop[crop]
        country_symbol = VHIMapper.country[country]
        province_id_max = VHIMapper.province_id_max[country]
    except Exception:
        return

    for province_id in range(1, province_id_max+1):

        url = f"https://www.star.nesdis.noaa.gov/smcd/emb/vci/VH/get_TS_admin.php?provinceID" \
              f"={province_id}&country={country_symbol}&yearlyTag=Weekly&" \
              f"type=Mean&TagCropland={crop_symbol}&year1=1982&year2={SUPPORT.this_year}"
        print(url)
        try:
            req = urllib.request.Request(url=url, headers=header)
            response = urllib.request.urlopen(req)

            with open(f"{os.path.join(SUPPORT.data_path, country)}/VHI_{country}_{province_id}.csv", "wb") as f:
                content = response.read()
                f.write(content)
                response.close()
        except Exception:
            continue
        try:
            df = pd.read_csv(f"{os.path.join(SUPPORT.data_path, country)}/VHI_{country}_{province_id}.csv", skiprows=1)
            df = df.reset_index()
            df = df.iloc[1:-1]
            df = df.iloc[:, :-1]
            df.columns = ['YEAR', 'WEEK', 'SMN', 'SMT', 'VCI', 'TCI', 'VHI']
            df = df.replace(-1, np.nan)
            df["YEAR"] = df.YEAR.astype(int)
            df["WEEK"] = df.WEEK.astype(int)
            df = df[df.YEAR > 2000]

            df = df.set_index(["YEAR", "WEEK"])
            with pd.ExcelWriter(f"{os.path.join(SUPPORT.data_path, country)}/VH_{crop}_{country}_{province_id}.xlsx") as writer:
                for col in df.columns:
                    df_output = df[col].unstack(level=0)
                    df_output_copy = df_output.copy()
                    df_output['历史最大值'] = df_output_copy.iloc[:, :-1].max(axis=1)
                    df_output['历史最小值'] = df_output_copy.iloc[:, :-1].min(axis=1)
                    df_output['历史均值'] = np.nanmean(df_output_copy.iloc[:, :-1], axis=1)
                    df_output['近5年均值'] = np.nanmean(df_output_copy.iloc[:, -6:-1], axis=1)
                    df_output[f'上一年度:{SUPPORT.last_year}'] = df_output_copy[int(SUPPORT.last_year)]
                    df_output[f'当前年度:{SUPPORT.this_year}'] = df_output_copy[int(SUPPORT.this_year)]
                    df_output.to_excel(writer,
                                       sheet_name=f"{crop}_{country}_{province_id}_{col}",
                                       )
            writer.save()
            writer.close()
        except Exception:
            continue
    return


if __name__ == "__main__":
    for country in ["巴西", "美国", "阿根廷"]:
        get_VHI_data(country=country)