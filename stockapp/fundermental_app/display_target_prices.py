import sys

import numpy
import pandas as pd

from app_api import get_metric_data
from cassandra_api import create_session

numpy.set_printoptions(threshold=sys.maxsize)

def print_full(x):
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', None)
    print(x)

def run():
    session = create_session.create_cassandra_session()
    # all_stocks = universe.get_all_stocks()
    # all_stocks = ['TSLA', 'HOOD', 'COIN', 'PLTR', 'MQ', 'SE', 'PDD', 'BABA', 'SQ']
    all_stocks = ['TSLA', 'NVDA']

    columns = ['ticker', 'date', 'totalrevenue', 'totalrevenuegrowthrate',
                                              'operatingexpense', 'operatingexpensegrowthrate', 'commonstocksharesoutstanding',
                                              'targetprice2years20multiples', 'targetprice3years20multiples']

    # columns = ['ticker', 'date', 'targetprice2years20multiples', 'targetprice3years20multiples']

    for ticker in all_stocks:
        df = get_metric_data.get_metric_data(session, ticker, 'quarterly', columns)
        print_full(df[df['date'] >= '2021-09-30'])

if __name__ == '__main__':
    run()
