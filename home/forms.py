from django import forms

class ContactForm(forms.Form):

    contact_name = forms.CharField(label='Name', max_length=100)
    contact_relationship = forms.CharField(label='Relationship', max_length=100)
    contact_number = forms.CharField(label='Number', max_length=100)
