from datetime import date, datetime

from technical_app import universe
from app_api import set_alert
from cassandra_api import create_session


def run(input):
    session = create_session.create_cassandra_session()
    end_date = date.today()
    if input.get('end_date') is not None:
        format_str = '%Y-%m-%d'  # The format
        datetime_obj = datetime.strptime(input['end_date'], format_str)
        end_date = datetime_obj.date()
    tickers = []
    if input.get('tickers') is not None:
        tickers = input.get('tickers')
    else:
        tickers = universe.get_growth_stocks()
    set_alert.set_wyckoff_alert(session, tickers, end_date, 30)
    set_alert.set_wyckoff_alert(session, tickers, end_date, 60)
    buffett_tickers = universe.get_buffett_stocks()
    set_alert.set_buffett_alert(session, buffett_tickers, end_date, 120)
    set_alert.set_buffett_alert(session, buffett_tickers, end_date, 250)
    print(f"Finished: tickers: {tickers}, end_date: {end_date}")

if __name__ == '__main__':
    # run({'end_date': '2021-10-27', 'tickers': ['FDX']})
    # run({'end_date': '2021-10-20'})
    # run({'tickers': universe.get_growth_stocks()})
    run({})
