import requests
import threading
import numpy as np
import io
from bs4 import BeautifulSoup
from datetime import datetime


def naver_daily_second_hist_of(stock_code, working_date):
    data = []

    for c in range(1, 50):
        url = "http://finance.naver.com/item/sise_time.nhn?code=%s&thistime=%s160000&page=%s" \
              % (working_date, stock_code, c)
        response = requests.get(url)
        soup = BeautifulSoup(response.text.encode('utf-8'), 'html.parser')
        quotes = soup.find_all('span', {'class': ['tah', 'p10']})

        for li in quotes:
            data.append(li.text.strip())
        if data[-7] == '09:00':
            break
    # 체결시각 체결가 전일비 매도 매수 거래량 변동량
    quote = np.reshape(np.array(data), (-1, 7)).tolist()
    r = [[working_date] + [stock_code] + i for i in quote]
    r = np.array(r)
    return r


def naver_current_10_quote_of(stock_code):
    data = []

    url = "http://finance.naver.com/item/sise.nhn?code=%s&asktype=10" % stock_code
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')

    # 현재 시각
    QUOTIME = soup.select('.date')[0].text.strip()

    # 호가
    # list1 : 주요시세 list2 호가 list3
    quotes = soup.select('table.type2')[1].select('.num')
    for li in quotes:
        data.append(li.text.strip())

    quotes_list = np.reshape(np.array(data), (-1, 4)).tolist()
    code_quotes_list = [[QUOTIME] + [stock_code] + i for i in quotes_list]

    r = np.array(code_quotes_list)
    return r


def naver_current_top_players_of(stock_code):
    data = []
    url = "http://finance.naver.com/item/frgn.nhn?code=%s" % stock_code
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')

    # 현재 시각
    current_time = soup.select('.date')[0].text.strip()

    #투자자별 매매동향 - 투자자, 거래량
    quotes = soup.select('table.type2')[0].select('.title, .num')
    for li in quotes:
        data.append(li.text.strip())

    quotes_lst0 = [current_time] * 12                 # 조회시각
    quotes_lst1 = [stock_code] * 12                   # 업체코드
    quotes_lst2 = ['매도', '매수'] * 6                 # 매매구분
    quotes_lst3 = data[0:10] + ['외국추정', '외국추정'] # 거래기관
    quotes_lst4 = data[11:23]                         # 거래량

    r = np.array([quotes_lst0, quotes_lst1, quotes_lst2, quotes_lst3, quotes_lst4]).transpose()
    return r


def write_second_history_of(date_list):
    # 대구 139130 부산 138930 전북 175330 광주 192530 제주 006220
    # 신한 055550 국민 105560 하나 086790 기업 024110 우리 000030
    # date_list = ['20170424', '20170425', '20170426', '20170427', '20170428', '20170423', '20170422', '20170421']
    stock_code = ['139130','138930','175330','192530','006220','055550','105560','086790','024110','000030',
                  '005930','066570','000660','030190','034310','012510','036800','178780','064090','036570']
    stock_code.sort()

    for to_day in date_list:
        a = np.array(range(0, 9, 1))
        for code in stock_code:
            print('[%s] (%s) Quoting ... %s' % (threading.currentThread().getName(), to_day, code))
            quote = naver_daily_second_hist_of(to_day, code)
            a = np.append(a, quote)

        r = np.reshape(a, (-1, 9))
        np.savetxt('out_{}.dat'.format(to_day), r, fmt='%s', delimiter='|')


def write_current_10_quotes(outfile):
    stock_code = ['139130','138930','175330','192530','006220','055550','105560','086790','024110','000030',
                  '005930','066570','000660','030190','034310','012510','036800','178780','064090','036570']
    stock_code.sort()

    output_file = io.open(outfile, "w", encoding='utf-8')
    for code in stock_code:
        #print('[%s] Quoting ... %s' % (threading.currentThread().getName(), code))
        quotes_of_code = naver_current_10_quote_of(code).tolist()
        for quotes in quotes_of_code:
            for q in quotes:
                output_file.write(q + '|')
            output_file.write('\n')
    output_file.close()


def write_current_top_players(outfile):
    stock_code = ['139130','138930','175330','192530','006220','055550','105560','086790','024110','000030',
                  '005930','066570','000660','030190','034310','012510','036800','178780','064090','036570']
    stock_code.sort()

    output_file = io.open(outfile, "w", encoding='utf-8')
    for code in stock_code:
        #print('[%s] Quoting ... %s' % (threading.currentThread().getName(), code))
        r = naver_current_top_players_of(code).tolist()
        for li in r:
            for i in li:
                output_file.write(i + '|')
            output_file.write('\n')
    output_file.close()

"""
write_second_history_of(date_list=['20170504'])
write_current_10_quotes(outfile='out_sise.txt')
write_current_top_players(outfile='out_frgn.txt')
"""