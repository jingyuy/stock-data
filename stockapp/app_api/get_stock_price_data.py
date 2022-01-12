import pandas as pd

from cassandra_api.stock_price_data import get_stock_price


def pandas_factory(colnames, rows):
    return pd.DataFrame(rows, columns=colnames)

def get_stock_price_data(session, ticker, start_date, end_date):
    session.row_factory = pandas_factory
    session.default_fetch_size = None

    df = get_stock_price(session, ticker, start_date, end_date)
    return df