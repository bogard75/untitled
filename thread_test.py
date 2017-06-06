import threading
import bs

from time import sleep, localtime, strftime


class Thread_1(threading.Thread):
    def run(self):
        run_count = 0
        while True:
            print("[%s] %s" % (++run_count, threading.currentThread().getName()))
            bs.write_second_history_of(date_list=['20170508'])
            sleep(wait_seconds)


class Thread_2(threading.Thread):
    def run(self):
        run_count = 0
        while True:
            try:
                out_file_name = 'out_frgn%s.txt' % strftime("%Y%m%d%H%M%S", localtime())
                print("[%s] %s" % (run_count, threading.currentThread().getName()))
                bs.write_current_top_players(outfile=out_file_name)
            except:
                pass

            sleep(10)
            run_count = run_count + 1


class Thread_3(threading.Thread):
    def run(self):
        run_count = 0
        while True:
            try:
                out_file_name = 'out_sise%s.txt' % strftime("%Y%m%d%H%M%S", localtime())
                print("[%s] %s" % (run_count, threading.currentThread().getName()))
                bs.write_current_10_quotes(outfile=out_file_name)
            except:
                pass

            sleep(10)
            run_count = run_count + 1

#일과 종료 후 한번 실행 (날짜 바꾸고)
#t1 = Thread_1(name='second_history_of')
#t1.start()

#일과 중 실시간으로 실행 (Thread, 10초 간격)
t2 = Thread_2(name='current_top_players')  # 10초 간격으로 상위거래 5사 정보 긁기
t2.start()
t3 = Thread_3(name='current_10_quotes')    # 10초 간격으로 매도/매수 10호가 정보 긁기
t3.start()

while True:
    sleep(60)
    print("Count of active thread : %s" % threading.activeCount())


