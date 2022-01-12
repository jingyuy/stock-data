
def get_all_stocks():
    all_stocks = set()
    all_stocks.update(get_growth_stocks())
    return all_stocks

def get_growth_stocks():
    return ['TSLA', 'HOOD', 'COIN', 'PLTR', 'COUR', 'NVDA', 'AMD', 'MQ', 'SE', 'PDD', 'BABA', 'ESTC', 'PATH', 'SQ', 'UBER']