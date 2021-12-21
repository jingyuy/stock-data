
def insert_row(session, ticker, incomestatementtype, incomestatement):
    print(f"{ticker} {incomestatementtype} {incomestatement['fiscalDateEnding']}")
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
        map(lambda fieldname: int(incomestatement[fieldname]) if incomestatement[fieldname].isnumeric() else 0,
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
