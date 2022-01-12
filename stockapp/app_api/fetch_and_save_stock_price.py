from cassandra_api import stock_price_data
import yfinance as yf

def fetch_and_save(tickers, start_date, end_date, session):
    for ticker in tickers:
        print(f"Saving data for {ticker} from {start_date} to {end_date}")
        # get data on this ticker
        tickerData = yf.Ticker(ticker)
        # get the historical prices for this ticker
        df = tickerData.history(period='1d', start=start_date.strftime('%Y-%m-%d'), end=end_date.strftime('%Y-%m-%d'))
        for index, row in df.iterrows():
            date = index.date().strftime('%Y-%m-%d')
            try:
                stock_price_data.insert_row(session, ticker, date, row)
                print(f"saved {ticker} data for {date} close: {row['Close']} ")
            except Exception as e:
                print(
                    f"Error in putting item to price table. ticker: {ticker}, date: {date}." +
                    f" exception: {str(e)}")
                raise e