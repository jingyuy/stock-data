from datetime import timedelta

from app_api import get_stock_price_data
from cassandra_api import alert_data


def load_data(session, ticker, start_date, end_date):
    df = get_stock_price_data.get_stock_price_data(session, ticker, start_date, end_date)
    return df.set_index('date')

def to_date_str(date):
    return date.strftime('%Y-%m-%d')

def should_alert_wyckoff(long_percentile, short_percentile):
    return long_percentile < 20 and short_percentile >= 95

def get_alert(session, long_window, short_window, ticker, end_date):
    start_date = end_date - timedelta(days=int(long_window / 4 * 7))
    df = load_data(session, ticker, to_date_str(start_date), to_date_str(end_date))
    df_long_max = df['close'].rolling(window=long_window).max()
    df_long_min = df['close'].rolling(window=long_window).min()
    df_short_max = df['close'].rolling(window=short_window).max()
    df_short_min = df['close'].rolling(window=short_window).min()
    # print(f"current: {df['close'][-1]}, short min: {df_short_min[-1]}, short_max: {df_short_max[-1]}")
    long_percentile = (df['close'] - df_long_min) / (df_long_max - df_long_min) * 100
    short_percentile = (df['close'] - df_short_min) / (df_short_max - df_short_min) * 100
    return df.index[-1], long_percentile[-1], short_percentile[-1]

def should_alert_buffett(short_percentile):
    return short_percentile < 20

def set_wyckoff_alert(session, tickers, end_date, short_window):
    long_window = 200
    alert_type = "wychoff" + str(short_window)
    for ticker in tickers:
        # print(f"processing {ticker}")
        date_str, long_percentile, short_percentile = get_alert(session, long_window, short_window,
                                                                ticker, end_date)
        if should_alert_wyckoff(long_percentile, short_percentile):
            print(
                f"found {alert_type} for {ticker} on {date_str}: long percentile {long_percentile}, short percentile {short_percentile}")
            alert_data.insert_row(session, date_str, alert_type, ticker)
        # else:
        #     print(
        #         f"found NO {alert_type} for {ticker} on {date_str}: long percentile {long_percentile}, short percentile {short_percentile}")

def set_buffett_alert(session, tickers, end_date, short_window):
    long_window = 200
    alert_type = "buffett" + str(short_window)
    for ticker in tickers:
        # print(f"processing {ticker}")
        date_str, long_percentile, short_percentile = get_alert(session, long_window, short_window,
                                                                ticker, end_date)
        if should_alert_buffett(short_percentile):
            print(
                f"found {alert_type} for {ticker} on {date_str}: long percentile {long_percentile}, short percentile {short_percentile}")
            alert_data.insert_row(session, date_str, alert_type, ticker)
        # else:
        #     print(
        #         f"found NO {alert_type} for {ticker} on {date_str}: long percentile {long_percentile}, short percentile {short_percentile}")

