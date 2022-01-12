from cassandra_api.create_session import create_cassandra_session
from cassandra_api import income_statement_data, balance_sheet_data
from gateway.alphavantage import get_income_statements, get_balance_sheet
import time

def save_financial_date(ticker):
    session = create_cassandra_session()

    (quarterly, annual) = get_income_statements(ticker)
    for index, row in quarterly.iterrows():
        income_statement_data.insert_row(session, ticker, 'quarterly', row)
    for index, row in annual.iterrows():
        income_statement_data.insert_row(session, ticker, 'annual', row)

    time.sleep(1)

    (quarterly, annual) = get_balance_sheet(ticker)
    for index, row in quarterly.iterrows():
        balance_sheet_data.insert_row(session, ticker, 'quarterly', row)
    for index, row in annual.iterrows():
        balance_sheet_data.insert_row(session, ticker, 'annual', row)