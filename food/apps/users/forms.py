from django import forms


class RegisterForm(forms.Form):
    user_name = forms.CharField(required=True)
    pass_word = forms.CharField(required=True, min_length=8)
    email = forms.EmailField(required=True)


class LoginForm(forms.Form):
    user_name = forms.CharField(required=True)
    pass_word = forms.CharField(required=True,min_length=8)