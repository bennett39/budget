from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import loader
 
from .fetchdata import fetch_accounts_json, fetch_transactions_json
from .forms import SmsAuthenticationForm, PersonalCapitalLoginForm

from datetime import datetime, timedelta
from personalcapital import PersonalCapital, RequireTwoFactorException,\
                            TwoFactorVerificationModeEnum

import json

pc = PersonalCapital()

def index(request):
    if request.method == "POST":
        form = PersonalCapitalLoginForm(request.POST)

        if form.is_valid():
            session = request.session
            session['pc_email'] = form.cleaned_data['pc_email']
            session['pc_password'] = form.cleaned_data['pc_password']
            
            try:
                pc.login(session['pc_email'], session['pc_password'])
            except RequireTwoFactorException:
                pc.two_factor_challenge(TwoFactorVerificationModeEnum.SMS)
                return redirect('two-factor')

            accounts = fetch_accounts_json(pc)
            transactions = fetch_transactions_json(pc)
            reply = f"Networth: {accounts['spData']['networth']}"
            reply += "Transaction: "
            reply += f"{transactions['spData']['transactions'][0]['description']}"

            return HttpResponse(reply)

    else:
        form = PersonalCapitalLoginForm()

    return render(request, "budget/personal-capital-login.html",\
            {'form': form})


def two_factor(request):
    """Get two-factor SMS code from user"""
    if request.method == "POST":
        form = SmsAuthenticationForm(request.POST)
        
        if form.is_valid():
            sms_code = form.cleaned_data['sms_code']
            pc.two_factor_authenticate(\
                    TwoFactorVerificationModeEnum.SMS,\
                    sms_code)
            pc.authenticate_password(request.session['pc_password'])

            accounts = fetch_accounts_json(pc)
            transactions = fetch_transactions_json(pc)

            reply = f"Networth: {accounts['spData']['networth']}"
            reply += "Transaction: "
            reply += f"{transactions['spData']['transactions'][0]['description']}"

            return HttpResponse(reply)
        
        else:
            return HttpResponse('Invalid form')

    else: # Via GET
        form = SmsAuthenticationForm()

    return render(request, "budget/two-factor.html", {'form': form})
    

