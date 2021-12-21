import requests
import pandas as pd

def get_income_statements(symbol=None):
    API_KEY = "88C5GJD6EJF4QHYA"
    BASE_URL = "https://www.alphavantage.co/query?"
    url = f'{BASE_URL}function=INCOME_STATEMENT&symbol={symbol}&apikey={API_KEY}'
    json = requests.get(url).json()
    annualReports = json['annualReports']
    annual = pd.DataFrame(annualReports)
    quarterlyReports = json['quarterlyReports']
    quarterly = pd.DataFrame(quarterlyReports)
    return (quarterly, annual)
