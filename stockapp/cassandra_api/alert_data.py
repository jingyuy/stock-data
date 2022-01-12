from datetime import datetime

import pytz


def insert_row(session, date_str, alert_type, ticker):
    # print(f"inserting alert: {date_str} {alert_type} {ticker}")
    try:
        session.execute(
            """
            INSERT INTO stockapp.alert (
            date, alert, ticker, updated_time
            )
    
            VALUES (
            %s, %s, %s, %s
            )
            """,
            (date_str, alert_type, ticker, datetime.now().astimezone(pytz.timezone('US/Pacific')).strftime('%Y-%m-%dT%H:%M:%SZ'))
        )
    except Exception as e:
        print(
            f"Error in putting item to alert table. date: {date_str}, alert: {alert_type}, ticker: {ticker}, error: {e}")

def get_alerts(session, date):
    rslt = session.execute(
        """
        SELECT *  from stockapp.alert 
        where date = %s;
        """,
        (date, )
    )
    df = rslt._current_rows
    return df
