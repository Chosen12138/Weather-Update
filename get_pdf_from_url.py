import urllib.request

important_urls = {"NOAA_拉尼娜_厄尔尼诺气候报告": "https://www.cpc.ncep.noaa.gov/products/analysis_monitoring/lanina/enso_evolution-status-fcsts-web.pdf"}


for name, url in important_urls.items():
    urllib.request.urlretrieve(url, f'{name}.pdf')