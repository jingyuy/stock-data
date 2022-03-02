from cassandra_api.metric_data import get_metrics


def get_metric_data(session, ticker, type, columns):
    df = get_metrics(session, ticker, type)
    return df[columns]