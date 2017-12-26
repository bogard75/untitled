import os
from os import walk
import pandas as pd

#path = os.getcwd()
#path = r'C:\Users\taeil\Documents\GitHub\untitled'

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

# 201712월 frgn → One
def gather(files, df_func, outfile):
    data = pd.concat(map(frgn_to_df, files), ignore_index=True).drop_duplicates(keep='first')
    data.to_csv(outfile, sep='|', index=None, encoding='UTF-8')

file_list = []
for (dirpath, dirnames, filenames) in walk('/root/works/untitled/'):
    file_list.extend(filenames)
    break

gather(files = [name for name in file_list if name[:16] == 'out_frgn20171226'],
       df_func = frgn_to_df,
       outfile = 'tot_frgn20171226.txt')

gather(files = [name for name in file_list if name[:16] == 'out_sise20171226'],
       df_func = sise_to_df,
       outfile = 'tot_sise20171226.txt')