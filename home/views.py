from django.shortcuts import render, redirect

from django.http import HttpResponse
from .forms import ContactForm, OptionsForm
from .models import Contact, Options

def home(request):
    contacts = list(Contact.objects.all())
    options = list(Options.objects.all())[0]

    context = {'contact_form': ContactForm(), 'options_form': OptionsForm(), 'contacts': contacts, 'options': options}
    return render(request, 'home.html', context=context)


def add_contact(request):

    f = ContactForm(request.POST)

    if f.is_valid():
        item = Contact(name=f.cleaned_data['contact_name'],
                        relationship=f.cleaned_data['contact_relationship'],
                        carrier=f.cleaned_data['contact_carrier'],
                        number=f.cleaned_data['contact_number'])
        item.save()

    return redirect('home')

def add_options(request):

    f = OptionsForm(request.POST)

    if f.is_valid():

        item = list(Options.objects.all())[0]
        item.number = f.cleaned_data['options_number']
        item.carrier=f.cleaned_data['options_carrier']
        item.cheap = f.cleaned_data['options_cheap']
        item.expensive = f.cleaned_data['options_expensive']
        item.popular = f.cleaned_data['options_popular']
        item.save()

    return redirect('home')
