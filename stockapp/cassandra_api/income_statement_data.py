from cassandra_api import utils

def insert_row(session, ticker, incomestatementtype, incomestatement):
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

    session.execute(
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
        %s, %s, 
        %s, %s,
        %s, %s, 
        %s, %s,
        %s, %s, 
        %s, %s,
        %s, %s, 
        %s, %s,
        %s, %s, 
        %s, %s,
        %s, %s, 
        %s, %s,
        %s, %s, 
        %s, %s
        )
        """,
        (ticker, incomestatementtype,
         incomestatement['fiscalDateEnding'], incomestatement['reportedCurrency']) + numericfields
    )

def get_incomestatements(session, ticker, incomestatementtype):
    rslt = session.execute(
        """
        SELECT *  from stockapp.incomestatement 
        where ticker = %s and  type = %s;
        """,
        (ticker, incomestatementtype)
    )
    df = rslt._current_rows
    return df
