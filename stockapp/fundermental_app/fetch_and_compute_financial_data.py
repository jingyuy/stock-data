from app_api import save_financial_data, save_metric_data, get_metric_data
import display_target_prices
import time

def run():
    all_stocks = ['BABA']
    for ticker in all_stocks:
        save_financial_data.save_financial_date(ticker)
        time.sleep(1)

    for ticker in all_stocks:
        save_metric_data.save_metric_date(ticker)

    columns = ['ticker', 'date', 'totalrevenue', 'totalrevenuegrowthrate',
                                              'operatingexpense', 'operatingexpensegrowthrate', 'commonstocksharesoutstanding',
                                              'targetprice2years20multiples', 'targetprice3years20multiples']

    # columns = ['ticker', 'date', 'targetprice2years20multiples', 'targetprice3years20multiples']

    for ticker in all_stocks:
        df = get_metric_data.get_metric_data(ticker, 'quarterly', columns)
        display_target_prices.print_full(df[df['date'] >= '2021-09-30'])


if __name__ == '__main__':
    run()
