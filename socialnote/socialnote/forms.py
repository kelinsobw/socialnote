from django import forms

from profiles.models import Gender, Country


# The registration class of the main user data
class RegisterForm(forms.Form):
    first_name = forms.CharField(
        max_length=20, widget=forms.Textarea(attrs={"rows": 1, "cols": 5})
    )
    last_name = forms.CharField(max_length=200)
    email = forms.EmailField()
    password = forms.CharField(min_length=8, widget=forms.PasswordInput())


# Registration class for additional user data
class RegisterForm_2(forms.Form):
    age = forms.IntegerField(required='')
    user_image = forms.ImageField(required='')
    country = forms.ChoiceField(choices=Country.country_choice)
    gender = forms.ChoiceField(choices=Gender.gender_choice)


# Authorization class
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
