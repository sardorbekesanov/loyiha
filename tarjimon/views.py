from django.shortcuts import render
from django.http import HttpResponse
from .models import Lugat


# Create your views here.
def index(request):
    soz = request.GET.get('q', '')
    if soz and soz!=' ':
        natija=Lugat.objects.filter(inglizcha__contains=soz).all()[:5] 
    else:
        natija=None

    return render(request,'index.html', {'q':soz, 'natija':natija })
    