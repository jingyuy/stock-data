from datetime import datetime

import pytz

insert_statement = None
get_statement = None

def insert_row(session, date_str, alert_type, ticker):
    global insert_statement
    if insert_statement is None:
        insert_statement = session.prepare(
            """
            INSERT INTO stockapp.alert (
            date, alert, ticker, updated_time
            )
    
            VALUES (
            ?, ?, ?, ?
            )
            """)
    try:
        session.execute(insert_statement,
                        (date_str, alert_type, ticker, datetime.now().astimezone(pytz.timezone('US/Pacific')).strftime('%Y-%m-%dT%H:%M:%SZ'))
        )
    except Exception as e:
        print(
            f"Error in putting item to alert table. date: {date_str}, alert: {alert_type}, ticker: {ticker}, error: {e}")

def get_alerts(session, date):
    global get_statement
    if get_statement is None:
        get_statement = session.prepare(
        """
        SELECT *  from stockapp.alert 
        where date = ?;
        """
        )
    rslt = session.execute(get_statement, (date, ))
    df = rslt._current_rows
    return df
