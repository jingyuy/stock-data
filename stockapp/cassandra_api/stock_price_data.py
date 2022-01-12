from datetime import datetime

import pytz


def insert_row(session, ticker, date, stockprice):
    input = (ticker, date, datetime.now().astimezone(pytz.timezone('US/Pacific')).strftime('%Y-%m-%dT%H:%M:%SZ'),
         float(round(stockprice['Open'], 2)), float(round(stockprice['High'],2)),
         float(round(stockprice['Low'],2)), float(round(stockprice['Close'],2)),
         float(stockprice['Volume']), float(stockprice['Dividends']),
         float(stockprice['Stock Splits'])
         )
    session.execute(
        """
        INSERT INTO stockprice (
        ticker, date, updated_time,
        open, high,
        low, close,
        volume, dividends,
        stock_splits
        )

        VALUES (
        %s, %s, %s, 
        % s, % s,
        % s, % s,
        % s, % s,
        % s
        )
        """,
        input
    )

def get_stock_price(session, ticker, start_date, end_date):
    rslt = session.execute(
        """
        SELECT *  from stockapp.stockprice 
        where ticker = %s and date >= %s and date <= %s;
        """,
        (ticker, start_date, end_date)
    )
    df = rslt._current_rows
    return df
