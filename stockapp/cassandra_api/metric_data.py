
def insert_row(session, ticker, type, date, metrics):
    metricsfieldnames = ['totalrevenue', 'totalrevenuegrowthrate', 'operatingexpense', 'operatingexpensegrowthrate',
                         'commonstocksharesoutstanding', 'targetprice2years20multiples', 'targetprice3years20multiples']
    print(f"metrics: {ticker} {type} {date}\n{metrics[metricsfieldnames]}")
    metricsfields = tuple(
        map(lambda fieldname: metrics[fieldname], metricsfieldnames))

    session.execute(
        """
        INSERT INTO stockmetric (
        ticker, type, 
        date, totalrevenue, 
        totalrevenuegrowthrate, operatingexpense, 
        operatingexpensegrowthrate, commonstocksharesoutstanding,
        targetprice2years20multiples, targetprice3years20multiples)

        VALUES (
        %s, %s, 
        %s, %s,
        %s, %s,
        %s, %s,
        %s, %s
        )
        """,
        (ticker, type,
         date) + metricsfields
    )

def get_metrics(session, ticker, type):
    rslt = session.execute(
        """
        SELECT *  from stockapp.stockmetric 
        where ticker = %s and  type = %s;
        """,
        (ticker, type)
    )
    df = rslt._current_rows
    return df
