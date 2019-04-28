from django import forms

class ContactForm(forms.Form):

    contact_name = forms.CharField(label='Name', max_length=100)
    contact_relationship = forms.CharField(label='Relationship', max_length=100)
    contact_carrier = forms.ChoiceField(choices=[(m,m) for m in ['att', 'tmobile', 'verizon', 'sprint']])
    contact_number = forms.CharField(label='Number', max_length=100)


class OptionsForm(forms.Form):

    options_number = forms.CharField(label='Number', max_length=100)
    options_carrier = forms.ChoiceField(choices=[(m,m) for m in ['att', 'tmobile', 'verizon', 'sprint']])
    options_cheap = forms.IntegerField(label='Adjust Cheap Threshold')
    options_expensive = forms.IntegerField(label='Adjust Expensive Threshold')
    options_popular = forms.FloatField(label='Adjust Popular Threshold')
