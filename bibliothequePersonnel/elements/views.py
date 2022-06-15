from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import get_object_or_404

from .forms import ElementForm
from .models import Element

def elements_view(request):
    elements = Element.objects.all().order_by('-date_publication')
    return render(request, 'elements/liste.html', context={'elements':elements})

def film_view(request):
    elements = Element.objects.filter(type_element='F').order_by('-date_publication')
    return render(request, 'elements/liste.html', context={'elements':elements})
    
def series_view(request):
    elements = Element.objects.filter(type_element='S').order_by('-date_publication')
    return render(request, 'elements/liste.html', context={'elements':elements})
   
def disney_view(request):
    elements = Element.objects.filter(type_element='D').order_by('-date_publication')
    return render(request, 'elements/liste.html', context={'elements':elements})
   
def favori_view(request):
    elements = Element.objects.filter(favori=True).order_by('-date_publication')
    return render(request, 'elements/liste.html', context={'elements':elements})
   
def decouvrir_view(request):
    elements = Element.objects.filter(decouvrir=True).order_by('-date_publication')
    return render(request, 'elements/liste.html', context={'elements':elements})
   
def revoir_view(request):
    elements = Element.objects.filter(revoir=True).order_by('-date_publication')
    return render(request, 'elements/liste.html', context={'elements':elements})

def acheter_view(request):
    elements = Element.objects.filter(acheter=True).order_by('-date_publication')
    return render(request, 'elements/liste.html', context={'elements':elements})
   
def creer_view(request):
    form = ElementForm()
    return render(request,'elements/creer.html',context={'form': form})

def details_view(request, idelement):
     element = get_object_or_404(Element,id=idelement)
     return render(request, 'elements/detail.html', context={'element':element})
   

def search_view(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        elements = Element.objects.filter(titre__contains=searched).order_by('-date_publication')
        return render(request, 'elements/liste.html', context={'elements':elements})
    

def remerciements_view(request):
    return HttpResponse('Merci de nous avoir contactez')

def update_view(request):
    if request.method == 'POST':
        idelement = request.POST.getList('') ['id']        
        Element.objects.filter(id=idelement).update(favori='False')
        element = get_object_or_404(Element,id=idelement)
        return render(request, 'elements/detail.html', context={'element':element})
   

# def update2_view(request, idelement):
#     if request.method == 'POST':
#         Element.objects.filter(id=idelement).update(favori='False')
#         return HttpResponse('')
        


def update2_view(request):
        idelement = request.GET.get('idelement',None)
        Element.objects.filter(id=idelement).update(favori='False')
        response = {
        'fullname': idelement
         }
        return JsonResponse(response)