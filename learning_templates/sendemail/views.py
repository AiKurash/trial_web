from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm

def index(request):
    context_dict = {'text':'hello world','number':100}
    return render(request,'basic_app/index.html',context_dict)

def contactView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['bewater475@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('successView')
    return render(request, 'sendemail/contact.html', {'form': form})

def successView(request):
    return HttpResponse('Success! Thank you for your message.')

# Create your views here.
