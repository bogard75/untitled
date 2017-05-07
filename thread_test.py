import threading
import bs

from time import sleep

class Thread_1(threading.Thread):
    def run(self):
        while True:
            sleep(30)
            bs.write_second_history_of(date_list=['20170504'])
            print(threading.currentThread().getName())

class Thread_2(threading.Thread):
    def run(self):
        while True:
            sleep(10)
            bs.write_current_top_players(outfile='C:/Users/bogard/PycharmProjects/untitled/out_frgn.txt')
            print(threading.currentThread().getName())

class Thread_3(threading.Thread):
    def run(self):
        while True:
            sleep(10)
            bs.write_current_10_quotes(outfile='C:/Users/bogard/PycharmProjects/untitled/out_sise.txt')
            print(threading.currentThread().getName())

t1 = Thread_1(name='write_second_history_of')
t2 = Thread_2(name='write_current_top_players')
t3 = Thread_3(name='write_current_10_quotes')

t1.start()
t2.start()
t3.start()

