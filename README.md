# cpbl_sc
中華職棒球員(投手、野手)年度全紀錄查詢爬蟲

## 簡介
抓取選手年度全紀錄查詢資料，並匯出`.csv`檔
* 資料來源： http://www.cpbl.com.tw/stats/all.html
* 抓取適用年度：2010 ~ 2020
* 匯出檔名：`batting_stat.csv`, `pitching_stat.csv`

## 套件
* `Beautiful Soup 4.7.1`
* `pandas 0.24.2`
* `requests 2.21.0`

## 使用
    python cpbl_scrapy.py

## 備註
* 未針對選手姓名進行特殊符號處理(ex: `*`, `#`)
