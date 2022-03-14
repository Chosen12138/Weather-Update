import os
from datetime import datetime, timedelta, date

__all__ = ["SUPPORT",
           "VHIMapper",
           "FixedMapperURL",
           "BRAMapperURL",
           "USAMapperURL",
           "ARGMapperURL",
           "SE_ASIA_MapperURL",
           "Global_MapperURL"]


class SUPPORT:

    project_path = "C:/Users/be_be/Desktop/Weather Update"
    picture_path = os.path.join(project_path, "pic")
    report_path = os.path.join(project_path, "report")
    data_path = os.path.join(project_path, "data")
    now_datetime = datetime.now()
    yesterday_now_datetime = datetime.now() - timedelta(days=1)

    today = datetime.now().date()
    today_str_ = datetime.now().strftime("%Y-%m-%d")
    today_str = datetime.now().strftime("%Y%m%d")
    today_int = int(today_str)

    this_year = datetime.now().year
    this_month = datetime.now().month
    this_day = datetime.now().day

    last_year = this_year - 1
    last_month_year = (datetime.now().replace(day=1) - timedelta(days=1)).year
    last_month = (datetime.now().replace(day=1) - timedelta(days=1)).month

    today_pic_path = os.path.join(picture_path, today_str)

    ag_weather_date_num = (datetime.now().date() - date(2012, 7, 27)).days


class VHIMapper:
    crop = {"大豆": "SOYB"}
    country = {"巴西": "BRA",
               "美国": "USA",
               "阿根廷": "ARG"}
    province_id_max = {"巴西": 27,
                       "美国": 51,
                       "阿根廷": 24}


class FixedMapperURL:

    GLOBAL_urls = {"A_最近一月全球土壤湿度异常": "https://www.cpc.ncep.noaa.gov/products/Global_Monsoons/Figures/curr.w.monthly.figb.gif",
                   "B_最近30D全球累计降雨异常": "https://www.cpc.ncep.noaa.gov/products/Global_Monsoons/Figures/curr.p.30day.figb.gif",
                   "C_最近30D全球地表温度异常": "https://www.cpc.ncep.noaa.gov/products/Global_Monsoons/Figures/curr.sst.monthly.figb.gif",
                   "D_未来两周气候灾害预测": "https://www.cpc.ncep.noaa.gov/products/precip/CWlink/ghazards/images/gth_full.png",
                   "E_IOD指数时间序列": "http://www.bom.gov.au/climate/enso/monitoring/iod1.png",
                   "F_NINO指数时间序列": "https://psl.noaa.gov/enso/mei/img/meiv2.timeseries.png"}

    USA_urls = {"M_美国作物湿度": "https://www.cpc.ncep.noaa.gov/products/analysis_monitoring/regional_monitoring/cmi.gif",
                "E_美国干旱程度": "https://droughtmonitor.unl.edu/data/png/current/current_usdm.png",
                "A_美国过去一周累计降水": "https://www.cpc.ncep.noaa.gov/products/analysis_monitoring/regional_monitoring/cltrain.png",
                "B_美国过去一周温度异常": "https://www.cpc.ncep.noaa.gov/products/analysis_monitoring/regional_monitoring/clrtanom.png",
                "C_美国过去一周土层湿度": "https://www.cpc.ncep.noaa.gov/products/Drought/Figures/weekly_web_fig/weekly_SMprof_mosaic.gif",

                "H_美国3-7D灾害预测": "https://www.wpc.ncep.noaa.gov/threats/final/hazards_d3_7_contours.png",
                "I_美国6-10D温度预测": "https://www.cpc.ncep.noaa.gov/products/predictions/610day/610temp.new.gif",
                "K_美国6-10D降水预测": "https://www.cpc.ncep.noaa.gov/products/predictions/610day/610prcp.new.gif",
                "J_美国8-14D温度预测": "https://www.cpc.ncep.noaa.gov/products/predictions/814day/814temp.new.gif",
                "L_美国8-14D降水预测": "https://www.cpc.ncep.noaa.gov/products/predictions/814day/814prcp.new.gif",
                "F_美国月度干旱展望": "https://www.cpc.ncep.noaa.gov/products/expert_assessment/month_drought.png",
                "G_美国季度干旱展望": "https://www.cpc.ncep.noaa.gov/products/expert_assessment/season_drought.png",
                "N_美国近月天气展望": "https://www.cpc.ncep.noaa.gov/products/predictions/multi_season/13_seasonal_outlooks/color/page2.gif",
                "O_美国远月气温展望": "https://www.cpc.ncep.noaa.gov/products/predictions/multi_season/13_seasonal_outlooks/color/t.gif",
                "P_美国远月降水展望": "https://www.cpc.ncep.noaa.gov/products/predictions/multi_season/13_seasonal_outlooks/color/p.gif",

                "Q_美国过去一周SPI指数": "https://data.chc.ucsb.edu/products/CHIRPS-2.0/moving_01pentad/pngs/northern_latin_america/SPI_01PentAccum_Current.png",
                "R_美国月SPI指数含预测": "https://data.chc.ucsb.edu/products/CHIRPS-2.0+Forecasts/moving_05pentad/pngs/northern_latin_america/SPI_05PentAccum_Current.png"}

    ARG_urls = {"阿根廷过去一周累计降水": "https://www.cpc.ncep.noaa.gov/products/analysis_monitoring/regional_monitoring/wcpcp8.png",
                "阿根廷过去一周温度异常": "https://www.cpc.ncep.noaa.gov/products/analysis_monitoring/regional_monitoring/wctan8.png",
                "阿根廷最近一月降水异常": "https://www.cpc.ncep.noaa.gov/products/analysis_monitoring/regional_monitoring/1cpnp8.png",
                "阿根廷最近一月温度异常": "https://www.cpc.ncep.noaa.gov/products/analysis_monitoring/regional_monitoring/1ctan8.png",
                "阿根廷1-7D累计降水预测": "https://www.cpc.ncep.noaa.gov/products/JAWF_Monitoring/GFS/AR_curr.p.gfs1a.gif",
                "阿根廷8-14D累计降水预测": "https://www.cpc.ncep.noaa.gov/products/JAWF_Monitoring/GFS/AR_curr.p.gfs2a.gif",
                "阿根廷1-7D累计降水异常": "https://www.cpc.ncep.noaa.gov/products/JAWF_Monitoring/GFS/AR_curr.p.gfs1b.gif",
                "阿根廷8-14D累计降水异常": "https://www.cpc.ncep.noaa.gov/products/JAWF_Monitoring/GFS/AR_curr.p.gfs2b.gif",
                }

    BRA_urls = {"南美过去一周SPI指数": "https://data.chc.ucsb.edu/products/CHIRPS-2.0/moving_01pentad/pngs/south_america/SPI_01PentAccum_Current.png",
                "南美月SPI指数含预测": "https://data.chc.ucsb.edu/products/CHIRPS-2.0+Forecasts/moving_05pentad/pngs/south_america/SPI_05PentAccum_Current.png",
                "巴西过去一周累计降水": "https://www.cpc.ncep.noaa.gov/products/analysis_monitoring/regional_monitoring/wcpcp15.png",
                "巴西过去一周温度异常": "https://www.cpc.ncep.noaa.gov/products/analysis_monitoring/regional_monitoring/wctan15.png",
                "巴西最近一月累计降水": "https://www.cpc.ncep.noaa.gov/products/analysis_monitoring/regional_monitoring/1cpnp15.png",
                "巴西最近一月温度异常": "https://www.cpc.ncep.noaa.gov/products/analysis_monitoring/regional_monitoring/1ctan15.png",
                "巴西1-7D累计降水预测": "https://www.cpc.ncep.noaa.gov/products/JAWF_Monitoring/GFS/BR_curr.p.gfs1a.gif",
                "巴西8-14D累计降水预测": "https://www.cpc.ncep.noaa.gov/products/JAWF_Monitoring/GFS/BR_curr.p.gfs2a.gif",
                "巴西1-7D累计降水异常": "https://www.cpc.ncep.noaa.gov/products/JAWF_Monitoring/GFS/BR_curr.p.gfs1b.gif",
                "巴西8-14D累计降水异常": "https://www.cpc.ncep.noaa.gov/products/JAWF_Monitoring/GFS/BR_curr.p.gfs2b.gif",
                }

    SE_AISA_urls = {"东南亚过去一周SPI指数": "https://data.chc.ucsb.edu/products/CHIRPS-2.0/moving_01pentad/pngs/asia_southeast/SPI_01PentAccum_Current.png",
                    "东南亚月SPI指数含预测": "https://data.chc.ucsb.edu/products/CHIRPS-2.0+Forecasts/moving_05pentad/pngs/asia_southeast/SPI_05PentAccum_Current.png",
                    "东南亚过去一周累计降水": "https://www.cpc.ncep.noaa.gov/products/analysis_monitoring/regional_monitoring/wcpcp5.png",
                    "东南亚过去一周温度异常": "https://www.cpc.ncep.noaa.gov/products/analysis_monitoring/regional_monitoring/wctan5.png",
                    "东南亚最近一月累计降水": "https://www.cpc.ncep.noaa.gov/products/analysis_monitoring/regional_monitoring/1cpcp5.png",
                    "东南亚最近一月温度异常": "https://www.cpc.ncep.noaa.gov/products/analysis_monitoring/regional_monitoring/1ctan5.png",
                    "东南亚1-7D累计降水预测": "https://www.cpc.ncep.noaa.gov/products/JAWF_Monitoring/GFS/SEAsia_curr.p.gfs1a.gif",
                    "东南亚8-14D累计降水预测": "https://www.cpc.ncep.noaa.gov/products/JAWF_Monitoring/GFS/SEAsia_curr.p.gfs1b.gif",
                    "东南亚1-7D累计降水异常": "https://www.cpc.ncep.noaa.gov/products/JAWF_Monitoring/GFS/SEAsia_curr.p.gfs2a.gif",
                    "东南亚8-14D累计降水异常": "https://www.cpc.ncep.noaa.gov/products/JAWF_Monitoring/GFS/SEAsia_curr.p.gfs2b.gif",
                    }


class DynamicURL(object):

    def __init__(self, today=date(2022, 2, 15)):
        self.today = today
        self.today_str = self.today.strftime('%Y%m%d')
        self.today_str_dot = self.today.strftime('%Y.%m.%d')
        self.today_int = int(self.today_str)
        self.year = self.today.year
        self.month = self.today.month
        self.day = self.today.day
        self.ag_weather_date_num = (self.today - date(2012, 7, 27)).days

    def update_date(self, days=1):
        self.today = self.today - timedelta(days=days)
        self.today_str = self.today.strftime('%Y%m%d')
        self.today_str_dot = self.today.strftime('%Y.%m.%d')
        self.today_int = int(self.today_str)
        self.year = self.today.year
        self.month = self.today.month
        self.day = self.today.day
        self.ag_weather_date_num = (self.today - date(2012, 7, 27)).days

    @property
    def mapper(self):
        return {'澳气象局_IOD预测': f"http://www.bom.gov.au/climate/enso/wrap-up/archive/{self.today_str}.sstOutlooks_iod.png",
                '澳气象局_NINO预测': f"http://www.bom.gov.au/climate/enso/wrap-up/archive/{self.today_str}.sstOutlooks_nino34.png",
                }


class BRAMapperURL(DynamicURL):

    """巴西气候URL实例, 含静态和动态"""
    def __init__(self, today=SUPPORT.today):
        super().__init__(today)
        if not os.path.exists(os.path.join(SUPPORT.today_pic_path, '巴西')):
            os.mkdir(os.path.join(SUPPORT.today_pic_path, '巴西'))
        self.areas = ('riograndedosul', 'parana', 'matogrosso', 'goias')

    @property
    def fixed_urls(self):
        return FixedMapperURL.BRA_urls

    def ag_weather_urls(self, area='riograndedosul'):
        return {f"A_巴西{area}_未来15D降水": f"http://www.worldagweather.com/crops/fcstwx/fcstpcp_soybeans_{area}_{self.ag_weather_date_num}.png",
                f"C_巴西{area}_过去60D降水": f"http://www.worldagweather.com/crops/pastwx/pastpcp_soybeans_{area}_60day_{self.ag_weather_date_num+8}.png",
                f"E_巴西{area}_过去180D降水": f"http://www.worldagweather.com/crops/pastwx/pastpcp_soybeans_{area}_180day_{self.ag_weather_date_num+8}.png",
                f"B_巴西{area}_未来15D气温": f"http://www.worldagweather.com/crops/fcstwx/fcsttmp_soybeans_{area}_{self.ag_weather_date_num}.png",
                f"D_巴西{area}_过去60D气温": f"http://www.worldagweather.com/crops/pastwx/pasttmp_soybeans_{area}_60day_{self.ag_weather_date_num + 6}.png",
                f"F_巴西{area}_过去180D气温": f"http://www.worldagweather.com/crops/pastwx/pasttmp_soybeans_{area}_180day_{self.ag_weather_date_num + 6}.png",
        }


class USAMapperURL(DynamicURL):

    """美国气候URL实例, 含静态和动态"""
    def __init__(self, today=SUPPORT.today):
        super().__init__(today)
        if not os.path.exists(os.path.join(SUPPORT.today_pic_path, '美国')):
            os.mkdir(os.path.join(SUPPORT.today_pic_path, '美国'))
        self.areas = ('illinois', 'iowa', 'minnesota', 'indiana', 'nebraska')

    @property
    def fixed_urls(self):
        return FixedMapperURL.USA_urls

    def ag_weather_urls(self, area='illinois'):
        return {f"A_美国{area}_未来15D降水": f"http://www.worldagweather.com/crops/fcstwx/fcstpcp_soybeans_{area}_{self.ag_weather_date_num}.png",
                f"C_美国{area}_过去60D降水": f"http://www.worldagweather.com/crops/pastwx/pastpcp_soybeans_{area}_60day_{self.ag_weather_date_num+8}.png",
                f"E_美国{area}_过去180D降水": f"http://www.worldagweather.com/crops/pastwx/pastpcp_soybeans_{area}_180day_{self.ag_weather_date_num+8}.png",
                f"B_美国{area}_未来15D气温": f"http://www.worldagweather.com/crops/fcstwx/fcsttmp_soybeans_{area}_{self.ag_weather_date_num}.png",
                f"D_美国{area}_过去60D气温": f"http://www.worldagweather.com/crops/pastwx/pasttmp_soybeans_{area}_60day_{self.ag_weather_date_num + 6}.png",
                f"F_美国{area}_过去180D气温": f"http://www.worldagweather.com/crops/pastwx/pasttmp_soybeans_{area}_180day_{self.ag_weather_date_num + 6}.png",
        }


class ARGMapperURL(DynamicURL):

    """阿根廷气候URL实例, 含静态和动态"""
    def __init__(self, today=SUPPORT.today):
        super().__init__(today)
        if not os.path.exists(os.path.join(SUPPORT.today_pic_path, '阿根廷')):
            os.mkdir(os.path.join(SUPPORT.today_pic_path, '阿根廷'))
        self.areas = ('buenosaires', 'cordoba', 'santafe', 'entrerios', 'santiagodelestero')

    @property
    def fixed_urls(self):
        return FixedMapperURL.ARG_urls

    def ag_weather_urls(self, area='buenosaires'):
        return {f"A_阿根廷{area}_未来15D降水": f"http://www.worldagweather.com/crops/fcstwx/fcstpcp_soybeans_{area}_{self.ag_weather_date_num}.png",
                f"C_阿根廷{area}_过去60D降水": f"http://www.worldagweather.com/crops/pastwx/pastpcp_soybeans_{area}_60day_{self.ag_weather_date_num+8}.png",
                f"E_阿根廷{area}_过去180D降水": f"http://www.worldagweather.com/crops/pastwx/pastpcp_soybeans_{area}_180day_{self.ag_weather_date_num+8}.png",
                f"B_阿根廷{area}_未来15D气温": f"http://www.worldagweather.com/crops/fcstwx/fcsttmp_soybeans_{area}_{self.ag_weather_date_num}.png",
                f"D_阿根廷{area}_过去60D气温": f"http://www.worldagweather.com/crops/pastwx/pasttmp_soybeans_{area}_60day_{self.ag_weather_date_num + 6}.png",
                f"F_阿根廷{area}_过去180D气温": f"http://www.worldagweather.com/crops/pastwx/pasttmp_soybeans_{area}_180day_{self.ag_weather_date_num + 6}.png",
        }


class SE_ASIA_MapperURL(DynamicURL):

    """东南亚气候URL实例, 含静态和动态"""
    def __init__(self, today=SUPPORT.today):
        super().__init__(today)
        if not os.path.exists(os.path.join(SUPPORT.today_pic_path, '东南亚')):
            os.mkdir(os.path.join(SUPPORT.today_pic_path, '东南亚'))

    @property
    def fixed_urls(self):
        return FixedMapperURL.SE_AISA_urls

    @property
    def malaysia_weather_report_urls(self):
        return {"马来西亚月度气候报告": "https://www.met.gov.my/data/climate/tinjauancuacajangkapanjang.pdf"}

    def malaysia_weather_urls(self):
        pass

    @property
    def indonesia_weather_urls(self):
        next_month_date = self.today + timedelta(days=30)
        this_month = '0' + str(self.month) if int(self.month) < 10 else str(self.month)
        next_month = '0' + str(next_month_date.month) if int(next_month_date.month) < 10 else str(self.month)
        if 5 < self.day < 15:
            urls = {"A_印尼未来1旬降水预测": f"https://cdn.bmkg.go.id/Web/pch_det.{self.year}.{this_month}.das_.2_ver_{self.today_str_dot}.png",
                    "B_印尼未来2旬降水预测": f"https://cdn.bmkg.go.id/Web/pch_det.{self.year}.{this_month}.das_.3_ver_{self.today_str_dot}.png"}
        elif 15 <= self.day < 25:
            urls = {"A_印尼未来1旬降水预测": f"https://cdn.bmkg.go.id/Web/pch_det.{self.year}.{this_month}.das_.3_ver_{self.today_str_dot}.png",
                    "B_印尼未来2旬降水预测": f"https://cdn.bmkg.go.id/Web/pch_det.{next_month_date.year}.{next_month}.das_.1_ver_{self.today_str_dot}.png"}
        elif 25 <= self.day:
            urls = {"A_印尼未来1旬降水预测": f"https://cdn.bmkg.go.id/Web/pch_det.{next_month_date.year}.{next_month}.das_.1_ver_{self.today_str_dot}.png",
                    "B_印尼未来2旬降水预测": f"https://cdn.bmkg.go.id/Web/pch_det.{next_month_date.year}.{next_month}.das_.2_ver_{self.today_str_dot}.png"}
        elif self.day <= 5:
            urls = {"A_印尼未来1旬降水预测": f"https://cdn.bmkg.go.id/Web/pch_det.{self.year}.{this_month}.das_.1_ver_{self.today_str_dot}.png",
                    "B_印尼未来2旬降水预测": f"https://cdn.bmkg.go.id/Web/pch_det.{self.year}.{this_month}.das_.2_ver_{self.today_str_dot}.png"}
        else:
            urls = {}
        urls.update({"C_印尼无雨记录": "https://cews.bmkg.go.id/Peta/Hari_Tanpa_Hujan.bmkg"})
        return urls


class Global_MapperURL(DynamicURL):

    """全球气候URL实例, 含静态和动态"""
    def __init__(self, today=SUPPORT.today):
        super().__init__(today)
        if not os.path.exists(os.path.join(SUPPORT.today_pic_path, '全球')):
            os.mkdir(os.path.join(SUPPORT.today_pic_path, '全球'))

    @property
    def fixed_urls(self):
        return FixedMapperURL.GLOBAL_urls

    @property
    def dynamic_urls(self):
        return {"IOD_指数预测": f"http://www.bom.gov.au/climate/ocean/outlooks/archive/{self.today_str}//plumes/sstOutlooks.iod.hr.png",
                "NINO_指数预测": f"http://www.bom.gov.au/climate/ocean/outlooks/archive/{self.today_str}//plumes/sstOutlooks.nino34.hr.png"}


if __name__ == '__main__':
    mapper = SE_ASIA_MapperURL()