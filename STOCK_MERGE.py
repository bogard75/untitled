import os
from os import walk
import pandas as pd

#path = os.getcwd()
#path = r'C:\Users\taeil\Documents\GitHub\untitled'
file_list = []
for (dirpath, dirnames, filenames) in walk('/root/works/untitled/'):
    file_list.extend(filenames)
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
files = [name for name in file_list if name[:16] == 'out_frgn20171226']
pd.concat(map(frgn_to_df, files), ignore_index=True).drop_duplicates(keep='first').to_csv('tot_frgn20171226.txt', sep='|', index=None, encoding='UTF-8')

files = [name for name in file_list if name[:16] == 'out_sise20171226']
pd.concat(map(sise_to_df, files), ignore_index=True).drop_duplicates(keep='first').to_csv('tot_sise20171226.txt', sep='|', index=None, encoding='UTF-8')



