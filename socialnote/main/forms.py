from django import forms


class AddDatabase(forms.Form):
    type_choice = [
        ("Ch", 'Ch'),
        ("F", 'Female')]
    privates = [
        ("None", "None"),
        ("Friends", "Friends"),
        ("Absolutely", "Absolutely")
    ]
    table_name = forms.CharField()
    table_description = forms.CharField()
    table_privates = forms.ChoiceField(choices=privates)
    base_1 = forms.CharField()
    type_1 = forms.ChoiceField(choices=type_choice)
    base_2 = forms.CharField(required=False)
    type_2 = forms.ChoiceField(choices=type_choice)
    base_3 = forms.CharField(required=False)
    type_3 = forms.ChoiceField(choices=type_choice)
    base_4 = forms.CharField(required=False)
    type_4 = forms.ChoiceField(choices=type_choice)
    base_5 = forms.CharField(required=False)
    type_5 = forms.ChoiceField(choices=type_choice)
    base_6 = forms.CharField(required=False)
    type_6 = forms.ChoiceField(choices=type_choice)
    base_7 = forms.CharField(required=False)
    type_7 = forms.ChoiceField(choices=type_choice)
    base_8 = forms.CharField(required=False)
    type_8 = forms.ChoiceField(choices=type_choice)

