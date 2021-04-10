from django.shortcuts import render, HttpResponse
from accounts.models import Tabla_test
# Create your views here.

def home(request):
    numbers = [1,2,3,4,5]
    name = 'Cris'

    data = {}
    data['myName'] = name
    data['numbers'] = numbers
    #data['testItem'] = Tabla_test.objects.get(pk=1)

    return render(request, 'home.html', data)