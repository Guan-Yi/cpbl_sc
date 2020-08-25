# cpbl_sc
中華職棒球員(投手、野手)年度全紀錄查詢爬蟲

## 簡介
抓取選手年度全紀錄查詢資料，並匯出`.csv`檔
* 資料來源： http://www.cpbl.com.tw/stats/all.html
* 抓取適用年度：2000 ~ 2020
* 匯出檔名：
  * 野手成績：`batting_stat.csv`
  * 投手成績：`pitching_stat.csv`

## 套件
* `Beautiful Soup 4.7.1`
* `pandas 0.24.2`
* `requests 2.21.0`

## 使用
    python cpbl_scrapy.py [year] [stats type]
    ex:
    # 抓取 2020 投手、野手紀錄
    python cpbl_scrapy.py 2020
    
    # 抓取 2018 投手紀錄
    python cpbl_scrapy.py 2018 p

* `year`: 指定年份，非必要，格式：YYYY
* `stat type`: 指定抓取資料類型，非必要，有 `b`(Batting), `p`(Pitching) 兩種
* 未給予任何參數時，則會抓取 2000 ~ 2020 所有投手、野手紀錄資料

## 備註
* 未針對選手姓名進行特殊符號處理(ex: `*`, `#`)
