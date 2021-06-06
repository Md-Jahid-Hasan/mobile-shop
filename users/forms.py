from django import forms


class LogInForm(forms.Form):
    username = forms.CharField(label='Enter your username')
    password = forms.CharField(label="Enter your Password",
                               widget=forms.PasswordInput())
    next_url = forms.CharField(widget=forms.HiddenInput())