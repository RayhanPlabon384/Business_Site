from django.shortcuts import render
from .models import Contact,ContactForm

# Create your views here.
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        contactformdata = ContactForm(name=name,email=email,subject=subject,message=message)
        contactformdata.save()
    contactdata = Contact.objects.all()[0]
    context = {
        'contact':contactdata
    }
    return render(request,'contact.html',context)
