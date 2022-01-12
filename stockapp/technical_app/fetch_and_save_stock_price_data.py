from datetime import date, datetime, timedelta

import universe
from app_api import fetch_and_save_stock_price
from cassandra_api import create_session


def run(input):
    session = create_session.create_cassandra_session()
    end_date = date.today()
    start_date = end_date - timedelta(days=7)
    if input.get('end_date') is not None:
        format_str = '%Y-%m-%d' # The format
        datetime_obj = datetime.strptime(input['end_date'], format_str)
        end_date = datetime_obj.date()
    if input.get('start_date') is not None:
        format_str = '%Y-%m-%d' # The format
        datetime_obj = datetime.strptime(input['start_date'], format_str)
        start_date = datetime_obj.date()
    tickers = []
    if input.get('tickers') is not None:
        tickers = input.get('tickers')
    else:
        tickers = universe.get_all_stocks()
    fetch_and_save_stock_price.fetch_and_save(tickers, start_date, end_date, session)
    print(f"Finished: start_date: {start_date}, end_date: {end_date}, tickers: {tickers}")

if __name__ == '__main__':
    # run({'start_date': '2019-09-01', 'end_date': '2022-01-11'})
    # run({'start_date': '2019-01-01', 'tickers': universe.get_growth_stocks()})
    run({'start_date': '2019-01-01', 'end_date': '2022-01-11', 'tickers': ['NVDA', 'AMD']})
    # run({})

