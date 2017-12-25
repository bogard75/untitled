import threading
import bs

from time import sleep, localtime, strftime


class run_day_log(threading.Thread):
    def run(self):
        count = 0
        name = threading.currentThread().getName()
        while True:
            print("[%s] %s" % (count, name))
            bs.write_day_log(stocks=stocks, dates=['20170508'])
            sleep(wait_seconds)


class run_traders(threading.Thread):
    def run(self):
        self.stocks = stocks
        count = 0
        name = threading.currentThread().getName()
        while True:
            try:
                if '083000' <= strftime("%H%M%S", localtime()) <= '990000':
                    out = 'out_frgn%s.txt' % strftime("%Y%m%d%H%M%S", localtime())
                    print("[%s: %s] %s" % (count, name, out))
                    bs.write_traders(stocks=stocks, outfile=out)
                else:
                    print("[%s: %s] Idle..." % (count, name))
            except:
                pass

            sleep(10)
            count += 1


class run_10_quote(threading.Thread):
    def run(self):
        self.stocks = stocks
        count = 0
        name = threading.currentThread().getName()
        while True:
            try:
                if '083000' <= strftime("%H%M%S", localtime()) <= '990000':
                    out = 'out_sise%s.txt' % strftime("%Y%m%d%H%M%S", localtime())
                    print("[%s: %s] %s" % (count, name, out))
                    bs.write_10_quotes(stocks=stocks, outfile=out)
                else:
                    print("[%s: %s] Idle..." % (count, name))
            except:
                pass

            sleep(10)
            count += 1

#일과 종료 후 한번 실행 (날짜 바꾸고)
#t1 = Thread_1(name='second_history_of')
#t1.start()

stocks = ['139130', '138930', '175330', '192530', '006220', '055550', '105560', '086790', '024110', '000030',
          '005930', '066570', '000660', '030190', '034310', '012510', '036800', '178780', '064090', '036570']

#일과 중 실시간으로 실행 (Thread, 10초 간격)
t2 = run_traders(name="run_traders")  # 10초 간격으로 상위거래 5사 정보 긁기
#t2.run(stocks=stocks)
t2.start()
t3 = run_10_quote(name='run_10_quote')    # 10초 간격으로 매도/매수 10호가 정보 긁기
#t3.run(stocks=stocks)
t3.start()

while True:
    sleep(60)
    print("Count of active thread : %s" % threading.activeCount())


