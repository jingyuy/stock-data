import pandas as pd
from cassandra_api.create_session import create_cassandra_session
from cassandra_api.income_statement_data import get_last_incomestatement
from cassandra_api.balance_sheet_data import get_last_balancesheet

def pandas_factory(colnames, rows):
    return pd.DataFrame(rows, columns=colnames)

def get_financial_data(ticker, type, columns):
    session = create_cassandra_session()
    session.row_factory = pandas_factory
    session.default_fetch_size = None

    df = get_last_incomestatement(session, ticker, type)
    df_b = get_last_balancesheet(session, ticker, type)
    df['commonstocksharesoutstanding'] = df_b['commonstocksharesoutstanding']
    return df[columns]