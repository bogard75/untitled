import bs
import time
from threading import Thread
from time import localtime, strftime


class Run_traders(Thread):
    def __init__(self, stocks):
        super().__init__()
        self.stocks = stocks

    def run(self):
        try:
            out = 'out_frgn%s.txt' % strftime("%Y%m%d%H%M%S", localtime())
            print("[%s]" % out)
            bs.write_traders(stocks=stocks, outfile=out)
        except:
            pass


class Run_10_quote(Thread):
    def __init__(self, stocks):
        super().__init__()
        self.stocks = stocks

    def run(self):
        try:
            out = 'out_sise%s.txt' % strftime("%Y%m%d%H%M%S", localtime())
            print("[%s]" % (out))
            bs.write_10_quotes(stocks=stocks, outfile=out)
        except:
            pass


def read_stocks():
    with open('STOCK_CODE', 'r', encoding='UTF-8') as f:
        lines = f.read().splitlines()
    stocks = [line.split('|')[0] for line in lines]
    return stocks


stocks = read_stocks()
print('[1] Count of stocks : %s' % len(stocks))

while True:
    count = 0
    before = time.time()
    print('\rStarting....(strftime : %s)' % strftime("%H%M%S", localtime()), flush=True)
#    if '083000' <= strftime("%H%M%S", localtime()) <= '999999':
    while '000000' <= strftime("%H%M%S", localtime()) <= '999999':
        current = time.time()
        print('\rIn working time....(%s, %s)' % (current, before), end='', flush=True)
        if (current - before) >= 60.0:
            # Run Scraping
            count += 1
            print('\nWorking....(%s)' % count, flush=True)
            thread1 = Run_traders(stocks)
            thread2 = Run_10_quote(stocks)
            thread1.start()
            thread2.start()
            before = current

#print('Exit status', proc.poll())
