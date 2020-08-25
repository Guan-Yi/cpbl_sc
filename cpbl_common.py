import requests
from bs4 import BeautifulSoup

# function
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


def hr_stat_column_parse(column_set):
    '''
    home run stats box parse
    '''
    number = column_set[0].text
    year = column_set[1].text
    game_no = column_set[2].text
    date = column_set[3].text
    stadium = column_set[4].text
    batter = column_set[5].text
    batter_team = column_set[6].text
    pitcher = column_set[7].text
    pitcher_team = column_set[8].text
    rbi = column_set[9].text
    remark = column_set[10].text
    temp_record = [number, year, game_no, date, stadium, batter,
                   batter_team, pitcher, pitcher_team, rbi, remark,
                   remark]
    return temp_record