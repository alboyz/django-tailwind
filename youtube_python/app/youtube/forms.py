from django import forms

class LoginForm(forms.form):
    username = forms.CharField(label='username',max_length=20)