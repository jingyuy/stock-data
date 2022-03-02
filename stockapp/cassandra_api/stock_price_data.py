from datetime import datetime

import pytz

insert_statement = None
get_statement = None

def insert_row(session, ticker, date, stockprice):
    global insert_statement
    input = [ticker, date, datetime.now().astimezone(pytz.timezone('US/Pacific')).strftime('%Y-%m-%dT%H:%M:%SZ'),
         float(round(stockprice['Open'], 2)), float(round(stockprice['High'],2)),
         float(round(stockprice['Low'],2)), float(round(stockprice['Close'],2)),
         float(stockprice['Volume']), float(stockprice['Dividends']),
         float(stockprice['Stock Splits'])
         ]
    if insert_statement is None:
        insert_statement = session.prepare(
            """
            INSERT INTO stockprice (
            ticker, date, updated_time,
            open, high,
            low, close,
            volume, dividends,
            stock_splits
            )

            VALUES (
            ?, ?, ?, 
            ?, ?,
            ?, ?,
            ?, ?,
            ?
            )
            """)
    session.execute(insert_statement, input)

def get_stock_price(session, ticker, start_date, end_date):
    global get_statement
    if get_statement is None:
        get_statement = session.prepare(
            """
            SELECT *  from stockapp.stockprice 
            where ticker = ? and date >= ? and date <= ?;
            """)
    rslt = session.execute(
        get_statement,
        [ticker, start_date, end_date]
    )
    df = rslt._current_rows
    return df
