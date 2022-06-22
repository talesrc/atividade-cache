from django.shortcuts import render
import requests
from django.conf import settings
# Create your views here.

def home(request):
    return render(request, 'web/home.html')


def usuarios(request):
    # obtendo os dados da API
    base_url = settings.API_URL
    path = '/employee/'
    print(f'Getting {base_url+path}')
    response = requests.get(base_url+path)
    employee_data = response.json()
    context = {
        'employees': employee_data,        
    }
    print(context)
    return render(request, 'web/usuarios.html', context)

def detalhes(request, usuario_id):
    # obtendo os dados da API
    base_url = settings.API_URL
    path = '/employee/' + str(usuario_id)
    print(f'Getting {base_url+path}')
    response = requests.get(base_url+path)
    employee_data = response.json()
    context = {
        'employee': employee_data,        
    }
    print(context)
    return render(request, 'web/detalhes.html', context)