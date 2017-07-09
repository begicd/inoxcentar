from django.contrib.auth.decorators import login_required

from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404

from .forms import ProizvodForm


# Create your views here.
def index(request):
    context={
         'title':'Bravarsko-zanatska radnja Đorđević-Dobrodošli',
    }
    template='index.html'
    return render(request,template,context)


def about(request):
    context={
         'title':'Bravarsko-zanatska radnja Đorđević-O nama',
    }
    template='about.html'
    return render(request,template,context)

@login_required
def userProfile(request):
    user=request.user
    form=ProizvodForm(request.POST or None,request.FILES or None)
    confirm_message=None
    if form.is_valid():
        instance=form.save(commit=False)
        instance.save()
        confirm_message="Proizvod je zapamćen!"



    context={
         'title':'Bravarsko-zanatska radnja Đorđević-O nama',
         'user': user,
         'form': form,
         'confirm_message':confirm_message,
    }
    template='profile.html'
    return render(request,template,context)
