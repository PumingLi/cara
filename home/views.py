from django.shortcuts import render, redirect

from django.http import HttpResponse
from .forms import ContactForm
from .models import Contact

def home(request):
    contacts = list(Contact.objects.all())

    context = {'contact_form': ContactForm(), 'contacts': contacts}
    return render(request, 'home.html', context=context)


def add_contact(request):

    f = ContactForm(request.POST)
    if f.is_valid():
        item = Contact(name=f.cleaned_data['contact_name'],
                        relationship=f.cleaned_data['contact_relationship'],
                        number=f.cleaned_data['contact_number'])
        item.save()

    return redirect('home')
