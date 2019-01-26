from django import forms

class SmsAuthenticationForm(forms.Form):
    sms_code = forms.CharField(label="SMS Code", max_length=4)

class PersonalCapitalLoginForm(forms.Form):
    pc_email = forms.EmailField(label="Email")
    pc_password = forms.CharField(label="Password",\
            widget=forms.PasswordInput)
