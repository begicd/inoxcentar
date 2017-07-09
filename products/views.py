from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Proizvod



# Create your views here.
def categories(request):

    proizvodi=Proizvod.objects.all().order_by("-id")

    query=request.GET.get('k')
    query1=request.GET.get('m')
    if query:
        proizvodi=proizvodi.filter(
                                    Q(kategorija__icontains=query)

                                    ).distinct()

    if query1:
        proizvodi=proizvodi.filter(
                                    Q(materijal__icontains=query1)

                                    ).distinct()



    context={
        'title':'Bravarsko-zanatska radnja Đorđević-Pregled proizvoda',
        'proizvodi': proizvodi,

    }
    template='categories.html'
    return render(request,template,context)

@login_required
def product_delete(request, id=id):
    template='confirm_delete.html'
    proizvod = get_object_or_404(Proizvod, id=id) 
    confirm_message=None   
    if request.method=='POST':
        confirm_message="Proizvod uspešno obrisan!"   
        proizvod.delete()
        return redirect('success')
    return render(request, template, {'proizvod':proizvod })

@login_required
def success(request):
    template='suuccess.html'
    context={'title':'Uspešno izbrisan proizvod'}
    return render(request, template, context)