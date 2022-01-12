from cassandra_api import metric_data
from cassandra_api.create_session import create_cassandra_session
from app_api import get_financial_data
import pandas as pd


def save_metric_date(ticker):
    session = create_cassandra_session()

    df = get_financial_data.get_financial_data(ticker, 'quarterly', ['ticker', 'type', 'fiscaldateending',
                                                                     'totalrevenue', 'operatingincome',
                                                                     'commonstocksharesoutstanding'])
    df['operatingexpense'] = df['totalrevenue'] - df['operatingincome']
    df['date'] = df['fiscaldateending']
    columns_original = ['totalrevenue', 'operatingexpense']
    columns_of_growth_rate = ['totalrevenuegrowthrate', 'operatingexpensegrowthrate']
    for column, new_column in zip(columns_original, columns_of_growth_rate):
        df[new_column] = df[column].pct_change(periods=-4)

    df['targetprice2years20multiples'] = (df['totalrevenue']*(1+ df['totalrevenuegrowthrate'])**2
                                         - df['operatingexpense']*(1+df['operatingexpensegrowthrate'].clip(lower=0))**2)*4/df['commonstocksharesoutstanding']*20
    df['targetprice3years20multiples'] = (df['totalrevenue']*(1+ df['totalrevenuegrowthrate'])**3
                                         - df['operatingexpense']*(1+df['operatingexpensegrowthrate'].clip(lower=0))**3)*4/df['commonstocksharesoutstanding']*20
    for index, row in df.iterrows():
        metric_data.insert_row(session, row['ticker'], row['type'], row['date'], row)