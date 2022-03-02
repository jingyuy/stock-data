from cassandra_api import utils

insert_statement = None
get_statement = None

def insert_row(session, ticker, balancesheettype, balancesheet):
    global insert_statement
    print(f"balancesheet: {ticker} {balancesheettype} {balancesheet['fiscalDateEnding']}")
    numericfieldnames = ('commonStock', 'commonStockSharesOutstanding')
    numericfields = tuple(
        map(lambda fieldname:  utils.getIntOrNull(balancesheet[fieldname]),
            numericfieldnames))
    if insert_statement is None:
        insert_statement = session.prepare(
        """
        INSERT INTO balancesheet (
        ticker, type, 
        fiscalDateEnding, reportedCurrency, 
        commonStock, commonStockSharesOutstanding)

        VALUES (
        ?, ?, 
        ?, ?,
        ?, ?
        )
        """)

    session.execute(insert_statement, (ticker, balancesheettype,
         balancesheet['fiscalDateEnding'], balancesheet['reportedCurrency']) + numericfields
    )

def get_last_balancesheet(session, ticker, balancesheettype):
    global get_statement
    get_statement = session.prepare(
        """
        SELECT *  from stockapp.balancesheet 
        where ticker = ? and  type = ?;
        """)
    rslt = session.execute(get_statement, (ticker, balancesheettype))
    df = rslt._current_rows
    return df
