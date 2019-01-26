from django import forms

class SmsAuthenticationForm(forms.Form):
    sms_code = forms.CharField(label='sms code', max_length=4)
