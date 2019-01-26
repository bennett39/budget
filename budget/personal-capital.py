from datetime import datetime, timedelta
from personalcapital import PersonalCapital, RequireTwoFactorException,\
                            TwoFactorVerificationModeEnum

import getpass
import json
import logging
import os

pc = PersonalCapital()

email, password = "EMAIL_HERE", "PASSWORD_HERE"

try:
  pc.login(email, password)
except RequireTwoFactorException:
  mode = TwoFactorVerificationModeEnum.SMS
  pc.two_factor_challenge(mode)
  pc.two_factor_authenticate(mode, input('code: '))
  pc.authenticate_password(password)

accounts_response = pc.fetch('/newaccount/getAccounts')
accounts = accounts_response.json()['spData']

print('Networth: {0}'.format(accounts['networth']))
