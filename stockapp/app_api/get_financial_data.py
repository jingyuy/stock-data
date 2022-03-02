from cassandra_api.income_statement_data import get_incomestatements
from cassandra_api.balance_sheet_data import get_last_balancesheet


def get_financial_data(session, ticker, type, columns):
    df = get_incomestatements(session, ticker, type)
    df_b = get_last_balancesheet(session, ticker, type)
    df['commonstocksharesoutstanding'] = df_b['commonstocksharesoutstanding']
    return df[columns]