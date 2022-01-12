import pandas as pd

from cassandra_api.create_session import create_cassandra_session
from cassandra_api.metric_data import get_metrics


def pandas_factory(colnames, rows):
    return pd.DataFrame(rows, columns=colnames)

def get_metric_data(ticker, type, columns):
    session = create_cassandra_session()
    session.row_factory = pandas_factory
    session.default_fetch_size = None

    df = get_metrics(session, ticker, type)
    return df[columns]