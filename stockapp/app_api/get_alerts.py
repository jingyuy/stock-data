import pandas as pd

from cassandra_api import alert_data


def pandas_factory(colnames, rows):
    return pd.DataFrame(rows, columns=colnames)

def get_alerts(session, alert_date):
    session.row_factory = pandas_factory
    session.default_fetch_size = None

    df = alert_data.get_alerts(session, alert_date)
    return df.values.tolist() #list(df.apply(lambda x: (x['date'], x['alert'])))

