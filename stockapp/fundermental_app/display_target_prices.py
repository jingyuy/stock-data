import sys

import numpy
import pandas as pd

from app_api import get_metric_data

numpy.set_printoptions(threshold=sys.maxsize)

def print_full(x):
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', None)
    print(x)

def run():
    # all_stocks = universe.get_all_stocks()
    # all_stocks = ['TSLA', 'HOOD', 'COIN', 'PLTR', 'MQ', 'SE', 'PDD', 'BABA', 'SQ']
    all_stocks = ['SE', 'MQ', 'AMD', 'NVDA']

    columns = ['ticker', 'date', 'totalrevenue', 'totalrevenuegrowthrate',
                                              'operatingexpense', 'operatingexpensegrowthrate', 'commonstocksharesoutstanding',
                                              'targetprice2years20multiples', 'targetprice3years20multiples']

    # columns = ['ticker', 'date', 'targetprice2years20multiples', 'targetprice3years20multiples']

    for ticker in all_stocks:
        df = get_metric_data.get_metric_data(ticker, 'quarterly', columns)
        print_full(df[df['date'] >= '2021-09-30'])

if __name__ == '__main__':
    run()
