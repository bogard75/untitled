import requests
import threading
import numpy as np
import io
from bs4 import BeautifulSoup


def naver_day_log(stock, date):
    data = []

    for c in range(1, 50):
        url = "http://finance.naver.com/item/sise_time.nhn?code=%s&thistime=%s160000&page=%s" \
              % (date, stock, c)
        response = requests.get(url)
        soup = BeautifulSoup(response.text.encode('utf-8'), 'html.parser')
        quotes = soup.find_all('span', {'class': ['tah', 'p10']})

        for li in quotes:
            data.append(li.text.strip())
        if data[-7] == '09:00':
            break
    # 체결시각 체결가 전일비 매도 매수 거래량 변동량
    quote = np.reshape(np.array(data), (-1, 7)).tolist()
    r = [[date] + [stock] + i for i in quote]
    r = np.array(r)
    return r


def write_day_log(stocks, dates):
    # 대구 139130 부산 138930 전북 175330 광주 192530 제주 006220
    # 신한 055550 국민 105560 하나 086790 기업 024110 우리 000030
    # date_list = ['20170424', '20170425', '20170426', '20170427', '20170428', '20170423', '20170422', '20170421']

    for date in dates:
        a = np.array(range(0, 9, 1))
        name = threading.currentThread().getName()
        for stock in stocks:
            print('[%s] (%s) Quoting ... %s' % (name, date, stock))
            quote = naver_day_log(date, stock)
            a = np.append(a, quote)

        r = np.reshape(a, (-1, 9))
        np.savetxt('out_{}.dat'.format(date), r, fmt='%s', delimiter='|')


def naver_10_quotes(stock):
    data = []
    url = "http://finance.naver.com/item/sise.nhn?code=%s&asktype=10" % stock
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')

    # 현재 시각
    timestamp = soup.select('.date')[0].text.strip()

    # 호가
    # list1 : 주요시세 list2 호가 list3
    quotes = soup.select('table.type2')[1].select('.num')
    for li in quotes:
        data.append(li.text.strip())

    quotes_list = np.reshape(np.array(data), (-1, 4)).tolist()
    code_quotes_list = [[timestamp] + [stock] + i for i in quotes_list]

    r = np.array(code_quotes_list)
    return r


def write_10_quotes(stocks, outfile):
    out = io.open(outfile, "w", encoding='utf-8')
    for stock in stocks:
        quotes_of_code = naver_10_quotes(stock).tolist()
        for quotes in quotes_of_code:
            for q in quotes:
                out.write(q + '|' )
            out.write('\n')
    out.close()


def naver_traders(stock):
    data = []
    url = "http://finance.naver.com/item/frgn.nhn?code=%s" % stock
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')

    # 현재 시각
    timestamp = soup.select('.date')[0].text.strip()

    #투자자별 매매동향 - 투자자, 거래량
    quotes = soup.select('table.type2')[0].select('.title, .num')
    for li in quotes:
        data.append(li.text.strip())

    quotes_lst0 = [timestamp] * 12                    # 조회시각
    quotes_lst1 = [stock] * 12                        # 업체코드
    quotes_lst2 = ['매도', '매수'] * 6                 # 매매구분
    quotes_lst3 = data[0:10] + ['외국추정', '외국추정'] # 거래기관
    quotes_lst4 = data[11:23]                         # 거래량

    r = np.array([quotes_lst0, quotes_lst1, quotes_lst2, quotes_lst3, quotes_lst4]).transpose()
    return r


def write_traders(stocks, outfile):
    out = io.open(outfile, "w", encoding='utf-8')
    for stock in stocks:
        traders_of_code = naver_traders(stock).tolist()
        for traders in traders_of_code:
            for t in traders:
                out.write(t + '|')
            out.write('\n')
    out.close()



"""
#write_10_quotes(stocks=['000030'], outfile='out_000030_2.txt')
#write_traders(stocks=['000030'], outfile='out_000030.txt')
"""

