from django.shortcuts import render, redirect
from .models import Contacts


def index(request):
    contacts = Contacts.objects.all()
    search_input = request.GET.get('search_area')
    if search_input:
        contacts = Contacts.objects.filter(full_name__icontains=search_input)
    else:
        contacts = Contacts.objects.all()
        search_input = ' '

    return render(request, 'index.html', {'contacts': contacts, 'search_input': search_input})


def add_contact(request):
    if request.method == 'POST':
        new_contact = Contacts(
            full_name=request.POST['fullname'],
            relationship=request.POST['relationship'],
            email=request.POST['email'],
            phone_number=request.POST['phone_number'],
            address=request.POST['address']
        )
        new_contact.save()
        return redirect('/')

    return render(request, 'new.html')


def contact_details(request, pk):
    contact = Contacts.objects.get(id=pk)
    return render(request, 'contact-profile.html', {'contact': contact})


def edit_contact(request, pk):
    contact = Contacts.objects.get(id=pk)

    if request.method == "POST":
        contact.full_name = request.POST['fullname']
        contact.relationship = request.POST['relationship']
        contact.email = request.POST['email']
        contact.phone_number = request.POST['phone_number']
        contact.address = request.POST['address']
        contact.save()

        return redirect('/contact_details/'+str(contact.id))

    return render(request, 'edit.html', {'contact': contact})


def delete_contact(request, pk):
    contact = Contacts.objects.get(id=pk)

    if request.method == "POST":
        contact.delete()
        return redirect(index)

    return render(request, 'delete.html', {'contact': contact})
