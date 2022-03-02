
insert_statement = None
get_statement = None
get_first_statement = None

def insert_row(session, ticker, type, date, metrics):
    global insert_statement
    metricsfieldnames = ['totalrevenue', 'totalrevenuegrowthrate', 'operatingexpense', 'operatingexpensegrowthrate',
                         'commonstocksharesoutstanding', 'targetprice2years20multiples', 'targetprice3years20multiples']
    print(f"metrics: {ticker} {type} {date}\n{metrics[metricsfieldnames]}")
    metricsfields = tuple(
        map(lambda fieldname: metrics[fieldname], metricsfieldnames))
    if insert_statement is None:
        insert_statement = session.prepare(
        """
        INSERT INTO stockmetric (
        ticker, type, 
        date, totalrevenue, 
        totalrevenuegrowthrate, operatingexpense, 
        operatingexpensegrowthrate, commonstocksharesoutstanding,
        targetprice2years20multiples, targetprice3years20multiples)

        VALUES (
        ?, ?, 
        ?, ?,
        ?, ?,
        ?, ?,
        ?, ?
        )
        """)
    session.execute(insert_statement, (ticker, type, date) + metricsfields)

def get_metrics(session, ticker, type):
    global get_statement
    if get_statement is None:
        get_statement = session.prepare(
        """
        SELECT *  from stockapp.stockmetric 
        where ticker = ? and  type = ?;
        """)
    rslt = session.execute(get_statement, (ticker, type))
    df = rslt._current_rows
    return df

def get_latest(session, ticker, type):
    global get_first_statement
    if get_first_statement is None:
        get_first_statement = session.prepare(
        """
        SELECT *  from stockapp.stockmetric 
        where ticker = ? and  type = ?;
        """)
    rslt = session.execute(get_first_statement, (ticker, type))
    df = rslt._current_rows
    return df
