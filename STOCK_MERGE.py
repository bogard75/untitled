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


def gather_to_csv(files, df_func, outfile):
    if files:
        data = df_func(files[0])
        for file in files:
            data.append(df_func(file), ignore_index=True).drop_duplicates(keep='first')
        data.to_csv(outfile, sep='|', index=None, encoding='UTF-8')
        return True
    else:
        return None


def main(argv):
    file_list = []
    for (_, _, fname) in walk('/root/works/untitled/out'):
        file_list.extend(fname)
        break

    print('[STOCK_MERGE] %s files in out directory...' % len(file_list))
    print('[STOCK_MERGE] gathering out_frgn%s files...' % argv[0])

    gather_to_csv(files=glob.glob('out_frgn%s*.txt' % argv), df_func=frgn_to_df, outfile='tot_frgn%s.txt' % argv)
    gather_to_csv(files=glob.glob('out_sise%s*.txt' % argv), df_func=sise_to_df, outfile='sise_frgn%s.txt' % argv)


if __name__ == "__main__":
    main(sys.argv[1:])
