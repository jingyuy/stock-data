
def get_all_stocks():
    all_stocks = set()
    all_stocks.update(get_growth_stocks())
    all_stocks.update(get_buffett_stocks())
    return all_stocks

def get_buffett_stocks():
    return [ 'RH',
             'STOR',
             'DVA',
             'BK',
             'KR',
             'KHC',
             'BAC',
             'AXP',
             'MCO',
             'VRSN',
             'LSXMK',
             'KO',
             'AAPL',
             'ITOCF',
             'BYDDF',
             'LSXMA',
             'LILA',
             'USB']

def get_growth_stocks():
    return ['BABA',
 'TSLA',
 'VZ',
 'JD',
 'HUYA',
 'TAL',
 'CAN',
 'KWEB',
 'EDU',
 'ZM',
 'PLTR',
 'FDX',
 'PYPL',
 'BILI',
 'TCEHY',
 'DIDI',
 'API',
 'NTES',
 'PDD',
 'MSFT',
 'ABNB',
  'NVDA',
  'AMD']