import pandas as pd
import glob


def write_frgn_to_txt(file_list, outfile):
    df = pd.DataFrame([])

    for quote_file in file_list:
        print('adding... %s' % quote_file)

        try:
            df_quote = pd.read_csv(quote_file, sep='|', index_col=False
                                   , converters={'stock_code': lambda x: str(x)}
                                   , names=['time', 'stock_code', 'sell_buy', 'player', 'quote'])
            # 파일생성일시 추가
            df_quote['create_time'] = quote_file[quote_file.find('.txt')-14: quote_file.find('.txt')]
        except IndexError as e:
            print(e)
            continue
        else:
            df = pd.concat([df, df_quote])
    df.drop_duplicates().to_csv(path_or_buf=outfile, sep='|', na_rep='~', index=False)


def write_sise_to_txt(file_list, outfile):
    df = pd.DataFrame([])

    for quote_file in file_list:
        print('adding... %s' % quote_file)

        try:
            df_quote = pd.read_csv(quote_file, sep='|', index_col=False
                                   , converters={'stock_code': lambda x: str(x)}
                                   , names=['time', 'stock_code', 'sell_amt', 'sell_quote', 'buy_quote', 'buy_amt'])
            # 파일생성일시 추가
            df_quote['create_time'] = quote_file[quote_file.find('.txt')-14: quote_file.find('.txt')]
        except IndexError as e:
            print(e)
            continue
        else:
            df = pd.concat([df, df_quote])
    df.drop_duplicates().to_csv(path_or_buf=outfile, sep='|', na_rep='~', index=False)


write_frgn_to_txt(file_list=glob.glob("./NAVER_STOCK_SISE/out_frgn*.txt"), outfile="./out_frgn_summary_170508.txt")
write_sise_to_txt(file_list=glob.glob("./NAVER_STOCK_SISE/out_sise*.txt"), outfile="./out_sise_summary_170508.txt")