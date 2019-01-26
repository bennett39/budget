from datetime import datetime, timedelta
from personalcapital import PersonalCapital, RequireTwoFactorException, TwoFactorVerificationModeEnum

import json

def fetch_accounts_json(pc):
    """
    Fetch accounts data from Personal Capital
    https://github.com/haochi/personalcapital
    """
    accounts_response = pc.fetch('/newaccount/getAccounts')
    return accounts_response.json()


def fetch_transactions_json(pc):
    """
    Fetch transaction data from Personal Capital
    https://github.com/haochi/personalcapital
    """
    now = datetime.now()
    date_format = '%Y-%m-%d'
    days = 90
    start_date = (now - (timedelta(days=days+1))).strftime(date_format)
    end_date = (now - (timedelta(days=1))).strftime(date_format)
    transactions_response = pc.fetch('/transaction/getUserTransactions', {
        'sort_cols': 'transactionTime',
        'sort_rev': 'true',
        'page': '0',
        'rows_per_page': '5',
        'startDate': start_date,
        'endDate': end_date,
        'component': 'DATAGRID'
    })

    return transactions_response.json()


