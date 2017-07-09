from django.shortcuts import render
from django.core.mail import  send_mail
from django.conf import settings
from .forms import contactForm

# Create your views here.
def contact(request):
    title='Bravarsko-zanatska radnja Đorđević-Kontakt'
    form=contactForm(request.POST or None)
    confirm_message=None

    if form.is_valid():
        #print request.POST
        #print form.cleaned_data['email']

        name=form.cleaned_data['Ime']
        comment=form.cleaned_data['Komentar']
        subject='Message from MYSITE'
        message='%s %s'%(comment,name)
        emailFrom=form.cleaned_data['Email']
        emailTo=[settings.EMAIL_HOST_USER]
        send_mail(subject,message,emailFrom,emailTo, fail_silently=True)

        title='Hvala!'
        confirm_message='Hvala na poruci, uskoro će te biti kontaktirani!'
        form=None

    context={
        'title': title ,
        'form': form,
        'confirm_message': confirm_message,
    }
    template='contact.html'
    return render(request,template,context)
