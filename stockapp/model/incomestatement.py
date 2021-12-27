from cassandra.stockapp import columns
from cassandra.stockapp.models import Model

class Incomestatement(Model):
    ticker = columns.Text(primary_key=True)
    totalRevenue  = columns.Integer()
    operatingIncome = columns.Integer()