from personalcapital import PersonalCapital, RequireTwoFactorException,\
                            TwoFactorVerificationModeEnum
from datetime import datetime, timedelta

import json

pc = PersonalCapital()

email, password =

try:
    pc.login(email, password)
except RequireTwoFactorException:
    pc.two_factor_challenge(TwoFactorVerificationModeEnum.SMS)
    pc.two_factor_authenticate(TwoFactorVerificationModeEnum.SMS,
            input('code: '))
    pc.authenticate_password(password)

accounts_response = pc.fetch('/newaccount/getAccounts')
accounts = accounts_response.json()

now = datetime.now()
date_format = '%Y-%m-%d'
days = 90
start_date = (now - (timedelta(days=days+1))).strftime(date_format)
end_date = (now - (timedelta(days=1))).strftime(date_format)
transactions_response = pc.fetch('/transaction/getUserTransactions', {
    'sort_cols': 'transactionTime',
    'sort_rev': 'true',
    'page': '0',
    'rows_per_page': '20',
    'startDate': start_date,
    'endDate': end_date,
    'component': 'DATAGRID'
})

transactions = transactions_response.json()

#  print(json.dumps(accounts, indent=4))
print("Add an email and password, uncomment the last two lines, and try\
        again")
#  print(json.dumps(transactions, indent=4))
