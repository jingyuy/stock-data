from cassandra_api import utils

def insert_row(session, ticker, balancesheettype, balancesheet):
    print(f"balancesheet: {ticker} {balancesheettype} {balancesheet['fiscalDateEnding']}")
    numericfieldnames = ('commonStock', 'commonStockSharesOutstanding')
    numericfields = tuple(
        map(lambda fieldname:  utils.getIntOrNull(balancesheet[fieldname]),
            numericfieldnames))

    session.execute(
        """
        INSERT INTO balancesheet (
        ticker, type, 
        fiscalDateEnding, reportedCurrency, 
        commonStock, commonStockSharesOutstanding)

        VALUES (
        %s, %s, 
        %s, %s,
        %s, %s
        )
        """,
        (ticker, balancesheettype,
         balancesheet['fiscalDateEnding'], balancesheet['reportedCurrency']) + numericfields
    )

def get_last_balancesheet(session, ticker, balancesheettype):
    rslt = session.execute(
        """
        SELECT *  from stockapp.balancesheet 
        where ticker = %s and  type = %s;
        """,
        (ticker, balancesheettype)
    )
    df = rslt._current_rows
    return df
