from cassandra_api.stock_price_data import get_stock_price


def get_stock_price_data(session, ticker, start_date, end_date):
    df = get_stock_price(session, ticker, start_date, end_date)
    return df