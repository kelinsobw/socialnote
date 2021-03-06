from django import forms


# A form for adding a new table to the database.
class AddDatabase(forms.Form):
    # Specify the supported data types
    type_choice = [
        ("INTEGER", 'INTEGER'),
        ("SERIAL", 'SERIAL'),
        ("CHAR", 'CHAR'),
        ("VARCHAR", 'VARCHAR'),
        ("TEXT", 'TEXT'),
        ("BOOLEAN", 'BOOLEAN')]
    # Specify the supported privacy settings
    privates = [
        ("None", "None"),
        ("Friends", "Friends"),
        ("Absolutely", "Absolutely")
    ]
    # The limit on the number of columns in the table is 8.
    # We declare all possible ones, and on the frontend we will
    # fill in only the required number
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
