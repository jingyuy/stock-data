from app_api import save_financial_data, get_financial_data
import universe.universe


def run():
    # all_stocks = universe.universe.get_all_stocks()
    # for ticker in all_stocks:
    #     save_financial_data.save_financial_date(ticker)
    result = get_financial_data.get_financial_data('TSLA', 'quarterly', ['ticker', 'type', 'fiscaldateending', 'commonstocksharesoutstanding'])
    return result

if __name__ == '__main__':
    run()
