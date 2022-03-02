from cassandra_api import alert_data


def get_alerts(session, alert_date):
    df = alert_data.get_alerts(session, alert_date)
    return df.values.tolist() #list(df.apply(lambda x: (x['date'], x['alert'])))

