import os
from os import walk
import pandas as pd

path = os.getcwd()
#path = r'C:\Users\taeil\Documents\GitHub\untitled'
f = []
for (dirpath, dirnames, filenames) in walk(path):
    f.extend(filenames)
    break

def frgn_to_df(filename):
    df = pd.read_csv(filename,
                     sep='|',
                     dtype=object,
                     names=['입수일시', '종목코드', '매수구분', '거래기관', '거래량', '_'])
    return df

def sise_to_df(filename):
    df = pd.read_csv(filename,
                     sep='|',
                     dtype=object,
                     names=['입수일시', '종목코드', '매도잔량', '매도호가', '매수호가', '매수잔량', '_'])
    return df

# 201712월 frgn → One File로
k = [s for s in f if s[:14] == 'out_frgn201712']
l = pd.concat(map(frgn_to_df, k), ignore_index=True).drop_duplicates(keep='first')

l.to_csv('out_frgn201712.txt', sep='|', index=None, encoding='UTF-8')

k = [s for s in f if s[:14] == 'out_sise201712']
l = pd.concat(map(sise_to_df, k), ignore_index=True).drop_duplicates(keep='first')

l.to_csv('out_sise201712.txt', sep='|', index=None, encoding='UTF-8')