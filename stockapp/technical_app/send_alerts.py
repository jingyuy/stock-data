import os
import smtplib
import json
from datetime import datetime, date, timedelta
from app_api import get_alerts, send_email
from cassandra_api import create_session


def run(event):
    session = create_session.create_cassandra_session()
    end_date = date.today()
    if event.get('date') is not None:
        format_str = '%Y-%m-%d'  # The format
        datetime_obj = datetime.strptime(event['date'], format_str)
        end_date = datetime_obj.date()
    start_date = end_date - timedelta(days=3)
    alerts = []
    while start_date <= end_date:
        alert_date = start_date.strftime('%Y-%m-%d')
        print(alert_date)
        for alert in get_alerts.get_alerts(session, alert_date):
            alerts.append(alert)
        start_date += timedelta(days=1)
    if len(alerts) > 0:
        print(f"Found alerts: {alerts}")
        send_email.send_email('Alert', f"{alert_date} alerts: {alerts} ")
        print(f"Finished sending alerts for {alerts}.")
    else:
        print("Finished: Found no alerts.")

if __name__ == '__main__':
    # run({'date': '2022-01-11'})
    run({})