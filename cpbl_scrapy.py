import pandas as pd
import requests
from bs4 import BeautifulSoup

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

def statbox_get(url, header):
    '''
    send request and parse html to extract stats box
    '''
    response = requests.get(url, header)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'lxml')
        statbox = soup.find_all("table", class_="std_tb mix_x")
        rows = statbox[0].find_all("tr")
    else:
        print(url, "Request Error", response.status_code)
    return rows

def batting_column_parse(column_set, year):
    '''
    batting stats box parse
    '''
    name = column_set[1].text.strip()
    game = column_set[2].text
    pa = column_set[3].text
    ab = column_set[4].text
    rbi = column_set[5].text
    r = column_set[6].text
    h = column_set[7].text
    single = column_set[8].text
    double = column_set[9].text
    triple = column_set[10].text
    hr = column_set[11].text
    tb = column_set[12].text
    so = column_set[13].text
    sb = column_set[14].text
    obp = column_set[15].text
    slg = column_set[16].text
    avg = column_set[17].text
    gidp = column_set[18].text
    sac = column_set[19].text
    sf = column_set[20].text
    bb = column_set[21].text
    ibb = column_set[22].text
    hbp = column_set[23].text
    cs = column_set[24].text
    go = column_set[25].text
    ao = column_set[26].text
    g_f = column_set[27].text
    sb_percent = column_set[28].text
    ta = column_set[29].text
    ssa = column_set[30].text
    temp_record = [year, name, game, pa, ab, rbi,
                   r, h, single, double, triple, hr,
                   tb, so, sb, obp, slg, avg,
                   gidp, sac, sf, bb, ibb, hbp,
                   cs, go, ao, g_f, sb_percent, ta,
                   ssa]
    return temp_record

def pitching_column_parse(column_set, year):
    '''
    pitching stats box parse
    '''
    name = column_set[1].text.strip()
    game = column_set[2].text
    gs = column_set[3].text
    gr = column_set[4].text
    cg = column_set[5].text
    sho = column_set[6].text
    nbb = column_set[7].text
    w = column_set[8].text
    l = column_set[9].text
    sv = column_set[10].text
    bs = column_set[11].text
    hld = column_set[12].text
    ip = column_set[13].text
    whip = column_set[14].text
    era = column_set[15].text
    bf = column_set[16].text
    np = column_set[17].text
    h = column_set[18].text
    hr = column_set[19].text
    bb = column_set[20].text
    ibb = column_set[21].text
    hbp = column_set[22].text
    so = column_set[23].text
    wp = column_set[24].text
    bk = column_set[25].text
    r = column_set[26].text
    er = column_set[27].text
    go = column_set[28].text
    ao = column_set[29].text
    g_f = column_set[30].text
    temp_record = [year, name, game, gs, gr, cg,
                   sho, nbb, w, l, sv, bs,
                   hld, ip, whip, era, bf, np,
                   h, hr, bb, ibb, hbp, so,
                   wp, bk, r, er, go, ao,
                   g_f]
    return temp_record

# request url parameter
years = ['2020', '2019', '2018', '2017', '2016']
game_type = '&game_type=01'
stat_types = ['&stat=pbat', '&stat=ppit']
online = '&online=0'
sort = '&sort=G'
order = '&order=desc'
pages = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

# main
for stat_type in stat_types:
    record_list = []
    for year in years:
        for page in pages:
            query = '?' + 'year=' + year + game_type + stat_type + online + sort + order + '&per_page=' + page
            tgt_url = BASE_URL + query
            print(tgt_url)
            raw_data = statbox_get(tgt_url, HEADERS)
            for i in range(len(raw_data)-1):
                column_set = raw_data[i+1].find_all("td")
                if stat_type == '&stat=pbat':
                    record = batting_column_parse(column_set, year)
                    record_list.append(record)
                else:
                    record = pitching_column_parse(column_set, year)
                    record_list.append(record)
    if stat_type == '&stat=pbat':
        df = pd.DataFrame(record_list, columns=batting_stats_header)
        df.to_csv('batting_stat.csv', index=False)
    else: 
        df = pd.DataFrame(record_list, columns=pitching_stats_header)
        df.to_csv('pitching_stat.csv', index=False)
    print(df)
