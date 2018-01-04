import sys
from os import walk
import pandas as pd
import glob

# path = os.getcwd()
# path = r'C:\Users\taeil\Documents\GitHub\untitled'


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

def gather(files, df_func):
    if len(files) <= 0:
        return None
    else:
        data = df_func(files[0])
        for file in files:
            data.append(df_func(file), ignore_index=True).drop_duplicates(keep='first')
        return data
    # data.to_csv(outfile, sep='|', index=None, encoding='UTF-8')


def main(argv):
    # Naver linux : /root/works/untitled/
    # Asus Vivonote : c:\\users\\taeil\\

    df = gather(files=glob.glob('out_frgn%s*.txt' % argv), df_func=frgn_to_df)
    df.to_csv('tot_frgn%s.txt' % argv, sep='|', index=None, encoding='UTF-8')

    df = gather(files=glob.glob('out_sise%s*.txt' % argv), df_func=sise_to_df)
    df.to_csv('tot_sise%s.txt' % argv, sep='|', index=None, encoding='UTF-8')


if __name__ == "__main__":
    main(sys.argv[1:])
