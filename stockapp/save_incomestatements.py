from cassandra_api.create_session import create_cassandra_session
from cassandra_api.income_statement_data import insert_row
from gateway.alphavantage import get_income_statements

def run():
    ticker = 'TSLA'
    (quarterly, annual) = get_income_statements('TSLA')
    session = create_cassandra_session()
    for index, row in quarterly.iterrows():
        insert_row(session, ticker, 'quarterly', row)
    for index, row in annual.iterrows():
        insert_row(session, ticker, 'annual', row)

if __name__ == '__main__':
    run()
