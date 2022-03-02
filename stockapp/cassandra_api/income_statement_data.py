from cassandra_api import utils

insert_statement = None
get_statement = None

def insert_row(session, ticker, incomestatementtype, incomestatement):
    global insert_statement
    print(f"incomestatement: {ticker} {incomestatementtype} {incomestatement['fiscalDateEnding']}")
    numericfieldnames = ('grossProfit', 'totalRevenue',
                         'costOfRevenue', 'costofGoodsAndServicesSold',
                         'operatingIncome', 'sellingGeneralAndAdministrative',
                         'researchAndDevelopment', 'operatingExpenses',
                         'investmentIncomeNet', 'netInterestIncome',
                         'interestIncome', 'interestExpense',
                         'nonInterestIncome', 'otherNonOperatingIncome',
                         'depreciation', 'depreciationAndAmortization',
                         'incomeBeforeTax', 'incomeTaxExpense',
                         'interestAndDebtExpense', 'netIncomeFromContinuingOperations',
                         'comprehensiveIncomeNetOfTax', 'ebit',
                         'ebitda', 'netIncome')
    numericfields = tuple(
        map(lambda fieldname: utils.getIntOrNull(incomestatement[fieldname]),
            numericfieldnames))
    if insert_statement is None:
        insert_statement = session.prepare(
        """
        INSERT INTO incomestatement (
        ticker, type, 
        fiscalDateEnding, reportedCurrency, 
        grossProfit, totalRevenue, 
        costOfRevenue, costofGoodsAndServicesSold, 
        operatingIncome, sellingGeneralAndAdministrative,
        researchAndDevelopment, operatingExpenses, 
        investmentIncomeNet, netInterestIncome, 
        interestIncome, interestExpense,
        nonInterestIncome, otherNonOperatingIncome, 
        depreciation, depreciationAndAmortization, 
        incomeBeforeTax, incomeTaxExpense, 
        interestAndDebtExpense, netIncomeFromContinuingOperations, 
        comprehensiveIncomeNetOfTax, ebit, 
        ebitda, netIncome)

        VALUES (
        ?, ?, 
        ?, ?,
        ?, ?, 
        ?, ?,
        ?, ?, 
        ?, ?,
        ?, ?, 
        ?, ?,
        ?, ?, 
        ?, ?,
        ?, ?, 
        ?, ?,
        ?, ?, 
        ?, ?
        )
        """)
    session.execute(insert_statement,
        (ticker, incomestatementtype,
         incomestatement['fiscalDateEnding'], incomestatement['reportedCurrency']) + numericfields
    )

def get_incomestatements(session, ticker, incomestatementtype):
    global get_statement
    if get_statement is None:
        get_statement = session.prepare(
        """
        SELECT *  from stockapp.incomestatement 
        where ticker = ? and  type = ?;
        """)
    rslt = session.execute(get_statement, (ticker, incomestatementtype))
    df = rslt._current_rows
    return df
