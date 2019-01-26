from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import loader

from .forms import SmsAuthenticationForm

from datetime import datetime, timedelta
from personalcapital import PersonalCapital, RequireTwoFactorException,\
                            TwoFactorVerificationModeEnum

import json

pc = PersonalCapital()

def index(request):
    session = request.session
    session['pc_email'] = ""
    session['pc_password'] = ""
    
    try:
        pc.login(session['pc_email'], session['pc_password'])
    except RequireTwoFactorException:
        pc.two_factor_challenge(TwoFactorVerificationModeEnum.SMS)
        return redirect('two-factor')

    return HttpResponse("Index. It didn't work.")

def two_factor(request):
    if request.method == "POST":
        form = SmsAuthenticationForm(request.POST)
        
        if form.is_valid():
            sms_code = form.cleaned_data['sms_code']
            pc.two_factor_authenticate(TwoFactorVerificationModeEnum.SMS, sms_code)
            pc.authenticate_password(request.session['pc_password'])

            accounts_response = pc.fetch('/newaccount/getAccounts')
            accounts = accounts_response.json()['spData']
            reply = 'Networth: {0}'.format(accounts['networth'])

            return HttpResponse(reply)
        
        else:
            return HttpResponse('Invalid form')

    else:
        form = SmsAuthenticationForm()

    return render(request, "budget/two-factor.html", {'form': form})
    

