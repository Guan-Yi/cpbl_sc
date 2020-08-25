import pandas as pd
import requests
import sys
from bs4 import BeautifulSoup
from cpbl_common import statbox_get, batting_column_parse, pitching_column_parse, hr_stat_column_parse

# env
BASE_URL = 'http://www.cpbl.com.tw/stats/all.html'
HEADERS = {
    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'
}

# dataframe header
batting_stats_header = ['year', 'name', 'game', 'pa', 'ab', 'rbi',
                        'r', 'h', 'single', 'double', 'triple', 'hr',
                        'tb', 'so', 'sb', 'obp', 'slg', 'avg',
                        'gidp', 'sac', 'sf', 'bb', 'ibb', 'hbp',
                        'cs', 'go', 'ao', 'g_f', 'sb_percent', 'ta',
                        'ssa']

pitching_stats_header = ['year', 'name', 'game', 'gs', 'gr', 'cg',
                         'sho', 'nbb', 'w', 'l', 'sv', 'bs',
                         'hld', 'ip', 'whip', 'era', 'bf', 'np',
                         'h', 'hr', 'bb', 'ibb', 'hbp', 'so',
                         'wp', 'bk', 'r', 'er', 'go', 'ao',
                         'g_f']

# request url parameter
years = ['2020', '2019', '2018', '2017', '2016', '2015', '2014', '2013', '2012', '2011', '2010',
         '2009', '2008', '2007', '2006', '2005', '2004', '2003', '2002', '2001', '2000']
game_type = '&game_type=01'
stat_types = ['&stat=pbat', '&stat=ppit']
online = '&online=0'
sort = '&sort=G'
order = '&order=desc'
pages = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']


def url_generate(year, stat_type):
    url_list = []
    if year is None:
        year_list = years
    elif str(year) in years:
        year_list = [str(year)]
    else:
        print('The year is error')

    if stat_type is None:
        stat_type_list = stat_types
    elif stat_type == 'b':
        stat_type_list = ['&stat=pbat']
    elif stat_type == 'p':
        stat_type_list = ['&stat=ppit']
    else:
        print('The stat type is error')
    
    print('url parameter:', year_list, stat_type_list)
    
    for st in stat_type_list:
        for yr in year_list:
            for page in pages:
                query = '?' + 'year=' + yr + game_type + st + online + sort + order + '&per_page=' + page
                tgt_url = BASE_URL + query
                url_list.append(tgt_url)
    return url_list


def main():
    if len(sys.argv) == 3:
        print('option:', sys.argv[1], sys.argv[2])
        target_url = url_generate(sys.argv[1], sys.argv[2])
    elif len(sys.argv) == 2:
        print('option:', sys.argv[1])
        if len(sys.argv[1]) > 1:
            stat_type = None
            target_url = url_generate(sys.argv[1], stat_type)
        else:
            year = None
            target_url = url_generate(year, sys.argv[1])
    elif len(sys.argv) == 1:
        year = None
        stat_type = None
        target_url = url_generate(year, stat_type)
    else:
        print(len(sys.argv), 'The option is invalid.')
    print(target_url)

    batting_record_list = []
    pitching_record_list = []
    for url in target_url:
        raw_data = statbox_get(url, HEADERS)
        for i in range(len(raw_data)-1):
            column_set = raw_data[i+1].find_all("td")
            if url[66:70] == 'pbat':
                record = batting_column_parse(column_set, url[43:47])
                batting_record_list.append(record)
            else:
                record = pitching_column_parse(column_set, url[43:47])
                pitching_record_list.append(record)

    if len(batting_record_list) > 0:
        df = pd.DataFrame(batting_record_list, columns=batting_stats_header)
        df.to_csv('batting_stat.csv', index=False)
    if len(pitching_record_list) > 0:    
        df = pd.DataFrame(pitching_record_list, columns=pitching_stats_header)
        df.to_csv('pitching_stat.csv', index=False)
    

if __name__ == '__main__':
    main()
