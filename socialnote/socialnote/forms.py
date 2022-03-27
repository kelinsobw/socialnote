from django import forms

from profiles.models import Gender, Country


class RegisterForm(forms.Form):
    first_name = forms.CharField(
        max_length=20, widget=forms.Textarea(attrs={"rows": 1, "cols": 5})
    )
    last_name = forms.CharField(max_length=200)
    email = forms.EmailField()
    password = forms.CharField(min_length=8, widget=forms.PasswordInput())


class RegisterForm_2(forms.Form):
    age = forms.IntegerField(required='')
    user_image = forms.ImageField(required='')
    country = forms.ChoiceField(choices=Country.country_choice)
    gender = forms.ChoiceField(choices=Gender.gender_choice)


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(min_length=8, widget=forms.PasswordInput())
